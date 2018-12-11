import json

filename_import = sys.argv[1]
filename_export = sys.argv[2]


def otvorenie_geojson:
    with open(filename_import, encoding='utf-8') as f:
        geojson = json.load(f)
    return geojson


def ulozenie_geojson (export):
    with open(filename_export, 'w') as geojson_file:



def delenie_bodov(bbox, vstup):
    minx = bbox[0]
    miny = bbox[1]
    maxx = bbox[2]
    maxy = bbox[3]



def pridanie_cluster_id(vstup, cluster_id):
    for feature in vstup['features']:
        try:
            var = feature["cluster_id"]
        except KeyError:
            var = 0
        new_cluster_id = var*10 + cluster_id
        feature.update({"cluster_id": new_cluster_id})
    return vstup

def calculator_bbox(vstup):
    """Vracia zoznam (bbox) minx,miny, maxx, maxy"""
    minx, miny = float("inf"), float("inf")
    maxx, maxy = float("-inf"), float("-inf")
    for p in vstup['features']:
        if p['geometry']['coordinates'][0] < minx:
            minx = p['geometry']['coordinates'][0]
        if p['geometry']['coordinates'][1] < miny:
            miny = p['geometry']['coordinates'][1]
        if p['geometry']['coordinates'][0] > maxx:
            maxx = p['geometry']['coordinates'][0]
        if p['geometry']['coordinates'][1] > maxy:
            maxy = p['geometry']['coordinates'][1]
    bbox = [minx, miny, maxx, maxy]
    return bbox
