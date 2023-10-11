import pytest
import sys
import os
cwd = os.getcwd()
sys.path.append(cwd)

from app.controllers.char_counter import *


@pytest.mark.asyncio
async def test_get_resources_names():
    resource_data = [
            [
                {
                    'info':{
                        'count': 826,
                        'pages': 42,
                        'next': 'https://rickandmortyapi.com/api/character?page=2',
                        'prev': None
                        },
                    'results':[
                        {
                            'id':1,
                            'name':'Rick Sanchez',
                            'status':'Alive',
                            'species':'Human',
                            'type':'',
                            'gender':'Male',
                            'origin':{
                                'name':'Earth (C-137)',
                                'url':'https://rickandmortyapi.com/api/location/1'
                            }
                        }
                    ]
                },
                {
                    'info':{
                        'count': 826,
                        'pages': 42,
                        'next': 'https://rickandmortyapi.com/api/character?page=2',
                        'prev': None
                        },
                    'results':[
                        {
                            'id':2,
                            'name':'Morty Smith',
                            'status':'Alive',
                            'species':'Human',
                            'type':'',
                            'gender':'Male',
                            'origin':{
                                'name':'unknown',
                                'url':''
                            }
                        }
                    ]
                },
                {
                    'info':{
                        'count': 826,
                        'pages': 42,
                        'next': 'https://rickandmortyapi.com/api/character?page=2',
                        'prev': None
                        },
                    'results':[
                        {
                            'id':3,
                            'name':'Summer Smith',
                            'status':'Alive',
                            'species':'Human',
                            'type':'',
                            'gender':'Female',
                            'origin':{
                                'name':'Earth (Replacement Dimension)',
                                'url':'https://rickandmortyapi.com/api/location/20'
                                },
                        }
                    ]
                },
            ],
            [
                {
                    'info':{
                        "count":51,
                        "pages":3,
                        "next":"https://rickandmortyapi.com/api/episode/?page=2",
                        "prev":None
                        },
                    'results':[
                        {
                            "id":1,
                            "name":"Pilot",
                            "air_date":"December 2, 2013",
                            "episode":"S01E01",
                            "characters": [
                                "https://rickandmortyapi.com/api/character/1",
                                "https://rickandmortyapi.com/api/character/2",
                                "https://rickandmortyapi.com/api/character/35",
                            ]
                        }
                    ]
                },
                {
                    'info':{
                        "count":51,
                        "pages":3,
                        "next":"https://rickandmortyapi.com/api/episode/?page=2",
                        "prev":None
                        },
                    'results':[
                        {
                            "id":2,
                            "name":"Lawnmower Dog",
                            "air_date":"December 9, 2013",
                            "episode":"S01E02",
                            "characters": [
                                "https://rickandmortyapi.com/api/character/1",
                                "https://rickandmortyapi.com/api/character/2",
                                "https://rickandmortyapi.com/api/character/38",
                            ]
                        }
                    ]
                },
                {
                    'info':{
                        "count":51,
                        "pages":3,
                        "next":"https://rickandmortyapi.com/api/episode/?page=2",
                        "prev":None
                        },
                    'results':[
                        {
                            "id":3,
                            "name":"Anatomy Park",
                            "air_date":"December 16, 2013",
                            "episode":"S01E03",
                            "characters": [
                                "https://rickandmortyapi.com/api/character/1",
                                "https://rickandmortyapi.com/api/character/2",
                                "https://rickandmortyapi.com/api/character/12",
                            ]
                        }
                    ]
                },
            ],
            [
                {
                    "info":{
                        "count":126,
                        "pages":7,
                        "next":"https://rickandmortyapi.com/api/location/?page=2",
                        "prev":None
                        },
                    'results':[
                        {
                            "id":1,
                            "name":"Earth (C-137)",
                            "type":"Planet",
                            "dimension":"Dimension C-137",
                            "residents":[
                                "https://rickandmortyapi.com/api/character/38",
                                "https://rickandmortyapi.com/api/character/45",
                                "https://rickandmortyapi.com/api/character/71"
                            ]
                        }
                    ]
                },
                {
                    "info":{
                        "count":126,
                        "pages":7,
                        "next":"https://rickandmortyapi.com/api/location/?page=2",
                        "prev":None
                        },
                    'results':[
                        {
                            "id":2,
                            "name":"Abadango",
                            "type":"Cluster",
                            "dimension":"unknown",
                            "residents":[
                                "https://rickandmortyapi.com/api/character/6",
                            ]
                        }
                    ]
                },
                {
                    "info":{
                        "count":126,
                        "pages":7,
                        "next":"https://rickandmortyapi.com/api/location/?page=2",
                        "prev":None
                        },
                    'results':[
                        {
                            "id":3,
                            "name":"Citadel of Ricks",
                            "type":"Space station",
                            "dimension":"unknown",
                            "residents":[
                                "https://rickandmortyapi.com/api/character/8",
                                "https://rickandmortyapi.com/api/character/14",
                                "https://rickandmortyapi.com/api/character/15"
                            ]
                        }
                    ]
                },
            ],
        ]
    
    result = await get_resources_names(resource_data)
    expected_result = [['Rick Sanchez', 'Morty Smith', 'Summer Smith'], ['Pilot','Lawnmower Dog','Anatomy Park'], ['Earth (C-137)','Abadango','Citadel of Ricks']]

    assert result == expected_result

@pytest.mark.asyncio
async def test_get_resource_names():
    resource_data = [
                {
                    'info':{
                        'count': 826,
                        'pages': 42,
                        'next': 'https://rickandmortyapi.com/api/character?page=2',
                        'prev': None
                        },
                    'results':[
                        {
                            'id':1,
                            'name':'Rick Sanchez',
                            'status':'Alive',
                            'species':'Human',
                            'type':'',
                            'gender':'Male',
                            'origin':{
                                'name':'Earth (C-137)',
                                'url':'https://rickandmortyapi.com/api/location/1'
                            }
                        }
                    ]
                },
                {
                    'info':{
                        'count': 826,
                        'pages': 42,
                        'next': 'https://rickandmortyapi.com/api/character?page=2',
                        'prev': None
                        },
                    'results':[
                        {
                            'id':2,
                            'name':'Morty Smith',
                            'status':'Alive',
                            'species':'Human',
                            'type':'',
                            'gender':'Male',
                            'origin':{
                                'name':'unknown',
                                'url':''
                            }
                        }
                    ]
                },
                {
                    'info':{
                        'count': 826,
                        'pages': 42,
                        'next': 'https://rickandmortyapi.com/api/character?page=2',
                        'prev': None
                        },
                    'results':[
                        {
                            'id':3,
                            'name':'Summer Smith',
                            'status':'Alive',
                            'species':'Human',
                            'type':'',
                            'gender':'Female',
                            'origin':{
                                'name':'Earth (Replacement Dimension)',
                                'url':'https://rickandmortyapi.com/api/location/20'
                                },
                        }
                    ]
                },
            ]


    result = await get_resource_names(resource_data)
    expected_result = ['Rick Sanchez', 'Morty Smith', 'Summer Smith']

    assert result == expected_result

@pytest.mark.asyncio
async def test_get_resources_names_count():
    resources_names = [['Rick Sanchez', 'Morty Smith', 'Summer Smith'], ['Pilot','Lawnmower Dog','Anatomy Park'], ['Earth (C-137)','Abadango','Citadel of Ricks']]
    chars = ['c', 'e', 'l']

    result = await get_resources_names_count(resources_names, chars)
    expected_result = [2, 1, 1]

    assert result == expected_result
    
@pytest.mark.asyncio
async def test_get_resource_names_count():
    resource_names = ['Rick Sanchez', 'Morty Smith', 'Summer Smith']
    char = 'c'

    result = await get_resource_names_count(resource_names, char)
    expected_result = 2

    assert result == expected_result

@pytest.mark.asyncio
async def test_update_resources_names_count():
    resources_names_count = [2, 1, 1]
    resources = ['character', 'episode', 'location']
    chars = ['c', 'e', 'l']

    result = await update_resources_names_count(resources_names_count, resources, chars)
    expected_result = [
        {
            'char': 'c',
            'count': 2,
            'resource': 'character'
        },
        {
            'char': 'e',
            'count': 1,
            'resource': 'episode'
        },
        {
            'char': 'l',
            'count': 1,
            'resource': 'location'
        }
    ]

    assert result == expected_result