import asyncio

class RickAndMortyChallenge:

    async def main():

        char_counter_task = await char_counter.get_exercise_results()
        episode_locations_task = await episode_locations.get_exercise_results()
        final_results= [char_counter_task, episode_locations_task]
        
        print(final_results)



if __name__ == "__main__":
    import sys
    from os import path
    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
    from controllers import char_counter
    from controllers import episode_locations
    asyncio.run(RickAndMortyChallenge.main())