import time
import asyncio
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from client.client import get_all_resources_data

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
    General function that covers the entire process of gathering and processing the information to deliver parcial results.

    Args:

    Returns:
        list: Parcial results.
    """
    resources = ['character', 'episode', 'location']
    chars = ['c', 'e', 'l']
    resources_data = await get_all_resources_data(resources)
    resources_names = await get_resources_names(resources_data)
    resources_names_count = await get_resources_names_count(resources_names, chars)
    rnc_updated = await update_resources_names_count(resources_names_count, resources, chars)

    return rnc_updated

async def get_resources_names(resources_data: list) -> list:
    """
    Gathers all the names for all the resources.

    Args:
        resources_data (list): All the raw api responses by page by resoruce.

    Returns:
        list: All resources names.
    """
    tasks = [get_resource_names(resource) for resource in resources_data]

    return await asyncio.gather(*tasks)

async def get_resource_names(resource_data: list) -> list:
    """
    Process given resource-specific collection of api responses (by page) to extract resource names from every item.

    Args:
        resource_data (list): All the raw api responses by page for given resoruce.

    Returns:
        list: Resource names by page for corresponding resource.
    """
    resource_name = []
    for page in resource_data:
        for results in page['results']:
            for key, value in results.items():
                if key == 'name':
                    resource_name.append(value)
    return resource_name

async def get_resources_names_count(resources_names: list, chars: list) -> list:
    """
    Awaits and gathers character count for every resource name.

    Args:
        resources_names (list): All the resources names by resource type.
        chars (list): Given characters to count.

    Returns:
        list: Character count by resource.
    """
    tasks = [get_resource_names_count(resource_names, char) for resource_names, char in zip(resources_names, chars)]

    return await asyncio.gather(*tasks)

async def get_resource_names_count(resource_names: list, char: str) -> int:
    """
    Awaits and gathers character count for every resource name.

    Args:
        resources_names (list): All the resources names by resource type.
        chars (str): Given characters to count.

    Returns:
        int: Character count by resource.
    """
    lower_case_list = [character.lower() for character in resource_names]
    target_character = char
    count = sum(character.count(target_character) for character in lower_case_list)

    return count

async def update_resources_names_count(resources_names_count: list, resources: list, chars: list) -> list:
    """
    Updates the resources names COUNT by adding the resource NAME and the CHAR counted to each RESOURCE TYPE.
    # rnc resources name count

    Args:
        resources_names_count (list): All the resources names count by resource type.
        resources (list): List of strings containing corresponding resources name.
        chars (list): Given characters to count.

    Returns:
        list: Resulting information for every resource.
    """
    rnc_updated = [{'char': char, 'count': rnc, 'resource': res} for char, rnc, res in zip(chars, resources_names_count, resources)]
    return rnc_updated

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
        'exercise_name': 'Char counter',
        'time': f'{elapsed_time} seconds',
        'in_time': in_time,
        'results': results
    }

    return final_results

if __name__ == "__main__":
    asyncio.run(main())