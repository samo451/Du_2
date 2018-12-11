import json
from abc import ABC, abstractmethod

filename_import = sys.argv[1]
filename_export = sys.argv[2]

class Body(ABC):
    pass

class Quadrtree(Body):
    def __init__(self, obalka_ll, obalka_ur):


def otvorenie_geojson:
    with open(filename_import, encoding='utf-8') as f:
        geojson = json.load(f)
    return geojson

def ulozenie_geojson (wxport):
    with open(filename_export, 'w') as geojson_file:



def delenie_bodov:
    m = 1


def pridanie_cluster_id(vstup, cluster_id):
    for feature in vstup['features']:
        try:
            var = feature["cluster_id"]
        except KeyError:
            var = 0
        new_cluster_id = var*10 + cluster_id
        feature.update({"cluster_id": new_cluster_id})
    return vstup

