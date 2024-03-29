configuration = {
"text_size": 300, 
"tile_size": 80, 
"type": "load", #random
"seed": None,
"file": "./student/map.txt",
"map_size": [10, 5],
"delay": 0.1,
"debugMap": False,
"debug": False,
"save": False, #True
"hazards": False,
"basicTile": "street",
"maxBags": 2, 
"agent":{
    "graphics":{ 
        "default": "game/graphics/logistics/bicycle100.png"
        },
    "id": "agent",
    "marker": 'A',
    "start": [0,0],
    },
"maptiles": {
    "street": {
        "graphics":{ 
            "default": "game/graphics/logistics/street100.png",
            "traversed": "game/graphics/logistics/street100Traversed.png"
            },
        "id":  "street",
        "marker": 'T',
        "num": 0,
        "state":
            {"agent":None,"image": "default"},
        "attributes":
            {"cost": 1},
        },
    "forest": {
        "graphics":{ 
            "default": "game/graphics/terrains/forest100.png",
            "traversed": "game/graphics/terrains/forestTraversed100.png"
            },
        "id":  "forest",
        "marker": 'F',
        "num": 0,
        "state":
            {"agent":None,"image": "default"},
        "attributes":
            {"cost": 3},
        },
    "hill": {
        "graphics":{ 
            "default": "game/graphics/terrains/hills100.png",
            "traversed": "game/graphics/terrains/hillsTraversed100.png"
            },
        "id":  "hill",
        "marker": 'H',
        "num": 0,
        "state":
            {"agent":None,"image": "default"},
        "attributes":
            {"cost": 2},
        },
    "plain": {
        "graphics":{ 
            "default": "game/graphics/terrains/plains100.png",
            "traversed": "game/graphics/terrains/plainsTraversed100.png"
            },
        "id":  "plain",
        "marker": 'P',
        "num": 0,
        "state":
            {"agent":None,"image": "default"},
        "attributes":
            {"cost": 1},
        },
    "desert": {
        "graphics":{ 
            "default": "game/graphics/terrains/desert100.png",
            "traversed": "game/graphics/terrains/desertTraversed100.png"
            },
        "id":  "desert",
        "marker": 'D',
        "num": 0,
        "state":
            {"agent":None,"image": "default"},
        "attributes":
            {"cost": 3},
        },
    "sea": {
        "graphics":{ 
            "default": "game/graphics/terrains/sea100.png",
            "traversed": "game/graphics/terrains/seaTraversed100.png"
            },
        "id":  "sea",
        "marker": 'S',
        "num": 0,
        "state":
            {"agent":None,"image": "default"},
        "attributes":
        {"cost": 1, "blocked": True},
        },
    "pizza": {
        "graphics":{ 
            "default": "game/graphics/logistics/restaurant100.png",
            "traversed": "game/graphics/logistics/restaurant100.png"
            },
        "id":  "pizza",
        "marker": 'Z',
        "num": 0,
        "state":
            {"agent":None,"image": "default"},
        "attributes":
            {"cost": 1},
        },
    "customer0": {
        "graphics":{ 
            "default": "game/graphics/logistics/customer100.png",
            "traversed": "game/graphics/logistics/customer100.png"
            },
        "id":  "customer0",
        "marker": '0',
        "num": 0,
        "state":
            {"agent":None,"image": "default"},
        "attributes":
            {"cost": 1, "unload": True, "objects": 0},
        },
    "customer1": {
        "graphics":{ 
            "default": "game/graphics/logistics/customer100_1.png",
            "traversed": "game/graphics/logistics/customer100_1.png"
            },
        "id":  "customer1",
        "marker": '1',
        "num": 0,
        "state":
            {"agent":None,"image": "default"},
        "attributes":
            {"cost": 1, "unload": True, "objects": 1},
        },
    "customer2": {
        "graphics":{ 
            "default": "game/graphics/logistics/customer100_2.png",
            "traversed": "game/graphics/logistics/customer100_2.png"
            },
        "id":  "customer2",
        "marker": '2',
        "num": 0,
        "state":
            {"agent":None,"image": "default"},
        "attributes":
            {"cost": 1, "unload": True, "objects": 2},
        },
    "customer3": {
        "graphics":{ 
            "default": "game/graphics/logistics/customer100_3.png",
            "traversed": "game/graphics/logistics/customer100_3.png"
            },
        "id":  "customer3",
        "marker": '3',
        "num": 3,
        "state":
            {"agent":None,"image": "default"},
        "attributes":
            {"cost": 1, "unload": True, "objects": 3},
        },
    "start": {
        "graphics":{ 
            "default": "game/graphics/logistics/base100.png",
            "traversed": "game/graphics/logistics/base100.png"
            },
        "id":  "start",
        "marker": 'W',
       "num": 0,
        "state":
            {"agent":None,"image": "default"},
        "attributes":
            {"cost": 1},
        },
    "building": {
        "graphics":{ 
            "default": "game/graphics/logistics/building100.png",
            "traversed": "game/graphics/logistics/building100.png"
            },
        "id":  "building",
        "marker": 'X',
        "num": 0,
        "state":
            {"agent":None,"image": "default"},
        "attributes":
            {"cost": 1, "blocked": True},
        }
    }   
}
