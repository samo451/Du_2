import json
from abc import ABC, abstractmethod


class Body(ABC):
    pass

class Quadrtree(Body):
    def __init__(self, obalka_ll, obalka_ur):


def otvorenie_geojson (vstup):
    with open


def ulozenie_geojson:
    with open('file.geojson', 'w') as geojson_file:
        data = json.load(geojson_file)


def delenie_bodov:
    m = 1


def pridanie_cluster_id(vstup):
    for feature in vstup['features']:
        feature.update({"cluster_id": "4"})
    return vstup

