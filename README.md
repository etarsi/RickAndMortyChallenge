# RickAndMortyChallenge

## Objective

You have to request all the `character`, `locations` and `episodes` of https://rickandmortyapi.com/ and indicate:

1. Char counter:
    - how many times the letter **"l"** appears in the names of all the `location`
    - how many times the letter **"e"** appears in the names of all the `episode`
    - how many times the letter **"c"** appears in the names of all the `character`
    - How long did the program take 👆 in total (from start of execution to delivery of results)

2. Episode locations:
    - for each `episode`, indicate the quantity and a list with the `location` (`origin`) of all the `character` that appeared in that `episode` (without repeating)
    - How long did the program take 👆 in total (from start of execution to delivery of results)

3. Output in json format with this structure:
```json
[
    {
        "exercise_name": "Char counter",
        "time": "2s 545.573272ms",
        "in_time": true,
        "results": [
            {
                "char": "l",
                "count": 12345,
                "resource": "location"
            },
            {
                "char": "e",
                "count": 12345,
                "resource": "episode"
            },
            {
                "char": "c",
                "count": 12345,
                "resource": "character"
            }
        ]
    },
    {
        "exercise_name": "Episode locations",
        "time": "1s 721.975698ms",
        "in_time": true,
        "results": [
            {
                "name": "Pickle Rick",
                "episode": "S03E03",
                "locations": [
                  "Earth (C-137)",
                  "Earth (Replacement Dimension)",
                  "unknown"
                ]
            }
        ]
    }
]
```


## Requirements

#### Libraries: 
- pytest
- pytest-asyncio


## Execution

#### Application

Execute from root directory:

```
python .\app\main\main.py
```

#### Tests

Execute inside directory

```
pytest
```
