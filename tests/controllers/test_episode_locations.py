import pytest
import sys
import os
cwd = os.getcwd()
sys.path.append(cwd)
from app.controllers.episode_locations import *


@pytest.mark.asyncio
async def test_get_resources():
    resources_data = [
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
    
    result = await get_resources(resources_data)
    expected_result =  [
            [
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
                },                   
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
                },
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
                },
            ],
            [
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
                },
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
                },
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
                },
            ],
            [
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
                },
                {
                   
                    "id":2,
                    "name":"Abadango",
                    "type":"Cluster",
                    "dimension":"unknown",
                    "residents":[
                        "https://rickandmortyapi.com/api/character/6",
                    ]
                },
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
                },
            ],
        ]

    assert result == expected_result

@pytest.mark.asyncio
async def test_get_resource():
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


    result = await get_resource(resource_data)
    expected_result =  [
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
                },                   
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
                },
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
                },
            ]

    assert result == expected_result

@pytest.mark.asyncio
async def test_get_characters():
    resources_results = [
        [
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
                },                   
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
                },
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
                },
            ],
            [
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
                },
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
                },
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
                },
            ],
            [
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
                },
                {
                   
                    "id":2,
                    "name":"Abadango",
                    "type":"Cluster",
                    "dimension":"unknown",
                    "residents":[
                        "https://rickandmortyapi.com/api/character/6",
                    ]
                },
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
                },
            ],
        ]
    resources = ['character', 'episode', 'location']

    result = await get_characters(resources_results, resources)
    expected_result = [
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
                },                   
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
                },
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
                },
            ]

    assert result == expected_result

@pytest.mark.asyncio
async def test_get_episodes():
    resources_results = [
        [
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
                },                   
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
                },
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
                },
            ],
            [
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
                },
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
                },
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
                },
            ],
            [
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
                },
                {
                   
                    "id":2,
                    "name":"Abadango",
                    "type":"Cluster",
                    "dimension":"unknown",
                    "residents":[
                        "https://rickandmortyapi.com/api/character/6",
                    ]
                },
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
                },
            ],
        ]
    resources = ['character', 'episode', 'location']

    result = await get_episodes(resources_results, resources)
    expected_result = [
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
                },
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
                },
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
                },
            ]

    assert result == expected_result

@pytest.mark.asyncio
async def test_get_episode_characters_ids():
    episodes_characters = [
                {
                    "id":1,
                    "name":"Pilot",
                    "episode":"S01E01",
                    "characters": [
                        "https://rickandmortyapi.com/api/character/1",
                        "https://rickandmortyapi.com/api/character/2",
                        "https://rickandmortyapi.com/api/character/35",
                    ]
                },
                {
            
                    "id":2,
                    "name":"Lawnmower Dog",
                    "episode":"S01E02",
                    "characters": [
                        "https://rickandmortyapi.com/api/character/1",
                        "https://rickandmortyapi.com/api/character/2",
                        "https://rickandmortyapi.com/api/character/38",
                    ]
                },
                {
                    "id":3,
                    "name":"Anatomy Park",
                    "episode":"S01E03",
                    "characters": [
                        "https://rickandmortyapi.com/api/character/1",
                        "https://rickandmortyapi.com/api/character/2",
                        "https://rickandmortyapi.com/api/character/12",
                    ]
                },
            ]

    result = await get_episode_characters_ids(episodes_characters)
    expected_result = [
                {
                    "id":1,
                    "name":"Pilot",
                    "episode":"S01E01",
                    "characters_ids": [
                        "1",
                        "2",
                        "35",
                    ]
                },
                {
            
                    "id":2,
                    "name":"Lawnmower Dog",
                    "episode":"S01E02",
                    "characters_ids": [
                        "1",
                        "2",
                        "38",
                    ]
                },
                {
                    "id":3,
                    "name":"Anatomy Park",
                    "episode":"S01E03",
                    "characters_ids": [
                        "1",
                        "2",
                        "12",
                    ]
                },
            ]

    assert result == expected_result

@pytest.mark.asyncio
async def test_get_episode_characters_origin():
    episodes_characters_ids = [
                {
                    "id":1,
                    "name":"Pilot",
                    "episode":"S01E01",
                    "characters_ids": [
                        "1",
                        "2",
                        "35",
                    ]
                },
                {
            
                    "id":2,
                    "name":"Lawnmower Dog",
                    "episode":"S01E02",
                    "characters_ids": [
                        "1",
                        "2",
                        "38",
                    ]
                },
                {
                    "id":3,
                    "name":"Anatomy Park",
                    "episode":"S01E03",
                    "characters_ids": [
                        "1",
                        "2",
                        "12",
                    ]
                },
            ]
    characters = [
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
                },                   
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
                },
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
                        }                      
                },
                {
                    "id":12,
                    "name":"Alexander",
                    "status":"Dead",
                    "species":"Human",
                    "type":"",
                    "gender":"Male",
                    "origin":{
                        "name":"Earth (C-137)",
                        "url":"https://rickandmortyapi.com/api/location/1"
                        }
                },
                {
                    "id":35,
                    "name":"Bepisian",
                    "status":"Alive",
                    "species":"Alien",
                    "type":"Bepisian",
                    "gender":"unknown",
                    "origin":{
                        "name":"Bepis 9",
                        "url":"https://rickandmortyapi.com/api/location/11"
                    }
                },
                {
                    "id":38,
                    "name":"Beth Smith",
                    "status":"Alive",
                    "species":"Human",
                    "type":"",
                    "gender":"Female",
                    "origin":{
                        "name":"Earth (C-137)",
                        "url":"https://rickandmortyapi.com/api/location/1"
                    }
                }
            ]

    result = await get_episode_characters_origin(characters, episodes_characters_ids)
    expected_result = [
        {
            'name': 'Pilot', 
            'episode': 'S01E01', 
            'locations': [
                'Earth (C-137)', 
                'unknown', 
                'Bepis 9',
                ]
        }, 
        {
            'name': 'Lawnmower Dog', 
            'episode': 'S01E02', 
            'locations': [
                'Earth (C-137)', 
                'unknown',
                ]
        }, 
        {
            'name': 'Anatomy Park', 
            'episode': 'S01E03', 
            'locations': [
                'Earth (C-137)', 
                'unknown',
                ]
        }
    ]

    assert result == expected_result