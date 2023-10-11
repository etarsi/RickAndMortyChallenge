import time
import asyncio
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from client.client import *

async def main():
    print(await get_exercise_results())

def get_start_time() -> float:
    """
    Returns actual time.

    Returns:
        float: Actual time.
    """   
    return time.time()

def get_elapsed_time(start_time: float) -> float:
    """
    Returns time elapsed between given time and actual time.

    Args:
        start_time (float): Given time.

    Returns:
        float: Elapsed time.
    """ 
    end_time = time.time()

    return end_time - start_time

async def get_results() -> list:
    """
    General function that covers the entire process of gathering and processing the information to deliver partial results.

    Args:

    Returns:
        list: Partial results.
    """
    resources = ['character', 'episode']
    resource_data = await get_all_resources_data(resources)  
    resources_results = await get_resources(resource_data)
    characters = await get_characters(resources_results, resources)
    episodes = await get_episodes(resources_results, resources)
    episodes_characters_ids = await get_episode_characters_ids(episodes)
    episodes_locations = await get_episode_characters_origin(characters, episodes_characters_ids)

    return episodes_locations

async def get_resources(resources_data: list) -> list:
    """
    Gathers the processed data from every given resource.

    Args:
        resources_data (list): All the raw api responses by page by resoruce.

    Returns:
        list: All resources results.
    """
    tasks = [get_resource(resource) for resource in resources_data]

    return await asyncio.gather(*tasks)

async def get_resource(resource_data: list) -> list:
    """
    Process given resource-specific collection of api responses (by page) to extract the resource "results" collection and dumping the "info" collection, from every item.

    Args:
        resource_data (list): All the raw api responses by page for given resoruce.

    Returns:
        list: Resource "results" by page for given resource.
    """
    resource = []
    for data in resource_data:
            for results in data['results']:
                resource.append(results)
    return resource

async def get_characters(resources_results: list, resources: list) -> list:
    """
    Iterates both given lists to return "results" only for the resource: "character"

    Args:
        resources_results (list): All the resource results for every resource
        resources (list): Resource names

    Returns:
        list: Entire information for "character" resource.
    """
    characters = []

    for data, resource in zip(resources_results, resources):
        if resource == 'character':
            characters = data

    return characters

async def get_episodes(resources_results: list, resources) -> list:
    """
    Iterates both given lists to return "results" only for the resource: "episode"

    Args:
        resources_results (list): All the resource results for every resource
        resources (list): Resource names

    Returns:
        list: All records from "episode" resource.
    """
    episodes = []

    for data, resource in zip(resources_results, resources):
        if resource == 'episode':
            episodes = data

    return episodes
    
async def get_episode_characters_ids(episodes: list) -> list:
    """
    For each episode, replaces characters api url for their respective ids

    Args:
        episodes (list): All records from "episode" resource.

    Returns:
        list: All records from "episode" resource.
    """
    common_prefix = "https://rickandmortyapi.com/api/character/"
    episode_characters_ids = []

    for epi in episodes:

        characters_ids = [character.replace(common_prefix, '') for character in epi['characters']]   
        
        episode = {
            'id': epi['id'],
            'name': epi['name'],
            'episode': epi['episode'],
            'characters_ids': characters_ids
        }
        episode_characters_ids.append(episode)

    return episode_characters_ids

async def get_episode_characters_origin(characters: list, episode_characters_ids: list) -> list:
    """
    For each episode, replaces characters ids for their origin name.
    In detail, for each episode compares its characters ids to each record in given characters list. If match, retrieves origin name.

    Args:
        characters (list): All records from "episode" resource.
        episode_characters_ids (list): All records from "episode" resource.

    Returns:
        list: All records from "episode" resource.
    """
    episode_characters_origin = []

    for epi in episode_characters_ids:
        
        characters_origin = []

        for character_id in epi['characters_ids']:
            for char in characters:
                if char['id'] == int(character_id):
                    if char['origin']['name'] not in characters_origin:
                        characters_origin.append(char['origin']['name'])

        episode = {
            'name': epi['name'],
            'episode': epi['episode'],
            'locations': characters_origin
        }
        episode_characters_origin.append(episode)
    
    return episode_characters_origin

async def get_exercise_results() -> dict:
    """
    Delivers exercise final results in the corresponding output format by putting together the partial results and the calculated elapsed time.
    
    Args:

    Returns:
        dict: Final results with corresponding output format.
    """

    start_time = get_start_time() 
    results = await get_results()
    elapsed_time = get_elapsed_time(start_time)

    in_time = False
    if elapsed_time < 3: in_time = True
    final_results = {
        'exercise_name': 'Episode locations',
        'time': f'{elapsed_time} seconds',
        'in_time': in_time,
        'results': results
    }

    return final_results

if __name__ == "__main__":
    asyncio.run(main())