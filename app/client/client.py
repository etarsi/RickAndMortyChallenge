import time
import asyncio
import httpx
import sys
import os
cwd = os.getcwd()
sys.path.append(cwd)

    
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

async def get_all_resources_data(resources: list) -> list:
    """
    General function that covers the process of requesting apis for every given resource name to return its entire data by page.

    Args:
        resources (list): Resources names.

    Returns:
        list: Complete resource data for given resources.
    """
    initial_data = await get_initial_data(resources)
    resources_pages_amount = await get_resources_pages(initial_data)
    resources_info = await update_resources_pages(resources_pages_amount, resources)
    resources_data_by_page = await get_resources_data(resources_info)

    return resources_data_by_page

async def get_initial_data(resources: list) -> list:
    """
    Awaits and gathers initial data (api response) for every given resource.

    Args:
        resources (list): Resources names.

    Returns:
        list: Initial unprocessed/unfiltered data for given resources.
    """
    tasks = [get_resource_initial_data(resource) for resource in resources]
    return await asyncio.gather(*tasks)

async def get_resource_initial_data(resource: str) -> dict:
    """
    Retrieve initial data for given resource name.

    Args:
        resource (str): Resource name.

    Returns:
        dict: Initial unprocessed/unfiltered data for given resource name.
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(f'https://rickandmortyapi.com/api/{resource}')
        response_data = response.json()
        return response_data

async def get_resources_pages(initial_data: list) -> list:
    """
    Awaits and gathers filtered initial data by amount of pages for every resource.

    Args:
        initial_data (list): Initial data from every resource.

    Returns:
        list: Amount of pages for every resource.
    """
    tasks = [get_resource_pages(resource_data) for resource_data in initial_data]
    return await asyncio.gather(*tasks)

async def get_resource_pages(resource_data: dict) -> dict:
    """
    Return amount of pages in the "info" key from the resource data for given resource.

    Args:
        resource_data (dict): Initial resource data from every resource.

    Returns:
        dict: Amount of pages for every resource.
    """
    for key, value in resource_data['info'].items():
        if key == "pages":
            resource_pages = {"pages": value}

    return resource_pages

async def update_resources_pages(resources_pages_amount: list, resources: list) -> list:
    """
    Updates resources pages amount collection by adding its corresponding name (key and value)

    Args:
        resources_pages_amount (list): Initial resource data from every resource.
        resources (list): Resources names.

    Returns:
        list: Collection for every resource with its corresponding pages amount
    """
    resources_info_updated = [{**pages_amount, 'resource': resource} for resource, pages_amount in zip(resources, resources_pages_amount)]
    return resources_info_updated

async def get_resources_data(resources_info: list) -> list:
    """
    Splits the requests by resource before retrieving by page data.

    Args:
        resources_info (list): Resource name and pages amount for every resource item.

    Returns:
        list: By page data for every resource.
    """
    tasks = [get_resource_data_by_resource(resource) for resource in resources_info]
    return await asyncio.gather(*tasks)

async def get_resource_data_by_resource(resource_info: dict) -> list:
    """
    Splits the requests by page before retrieving resource entire data.

    Args:
        resource_info (dict): Resource name and pages amount.

    Returns:
        list: Singular resource by page data.
    """
    tasks = [get_resource_data_by_page(resource_info, page) for page in range(1, resource_info['pages'] + 1)]
    return await asyncio.gather(*tasks)
    
async def get_resource_data_by_page(resource_info: dict, page: int) -> dict:
    """
    Retrieves data for given resource and page number

    Args:
        resource_info (dict): Resource name and pages amount.
        page (int): Corresponding page to complete request url.

    Returns:
        list: Resource page data.
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(f'https://rickandmortyapi.com/api/{resource_info["resource"]}?page={page}')
        response_data = response.json()
        return response_data