import json
import sys

if len(sys.argv) < 3:
    # Končí sa chybovým stavom
    print("Príliš málo argumentov")
    exit(1)

filename_import = sys.argv[1]
filename_export = sys.argv[2]

try:
    with open(filename_import, encoding='utf-8') as f:
        geojson = json.load(f)
except FileNotFoundError:
    print("Vstupný súbor nie je možné otvoriť")
    exit(2)


def delenie_bodov(bbox, vstup):
    """Delenie bodov pomocou mechanizmu quadtree. Iba pre inicializačný beh"""
    minx = bbox[0]
    miny = bbox[1]
    maxx = bbox[2]
    maxy = bbox[3]
    pocet_1, pocet_2, pocet_3, pocet_4 = 0, 0, 0, 0
    cluster_id_1, cluster_id_2, cluster_id_3, cluster_id_4 = 0, 0, 0, 0
    x_mean = (maxx+minx)/2
    y_mean = (maxy+miny)/2

    for p in vstup['features']:
        """Samotné roztriedenie na 4 oblasti a následné priradenie cluster_id atribútu"""
        if p['geometry']['coordinates'][0] < x_mean and p['geometry']['coordinates'][1] > y_mean:
            pocet_1 += 1
            cluster_id_1 = pridanie_cluster_id(p, 1)
        if p['geometry']['coordinates'][0] > x_mean and p['geometry']['coordinates'][1] > y_mean:
            pocet_2 += 1
            cluster_id_2 = pridanie_cluster_id(p, 2)
        if p['geometry']['coordinates'][0] < x_mean and p['geometry']['coordinates'][1] < y_mean:
            pocet_3 += 1
            cluster_id_3 = pridanie_cluster_id(p, 3)
        if p['geometry']['coordinates'][0] > x_mean and p['geometry']['coordinates'][1] < y_mean:
            pocet_4 += 1
            cluster_id_4 = pridanie_cluster_id(p, 4)
    """Zisťovanie, či je počet bodov v jednom  clustri nad 50. Pokiaě áno, delenie bodov sa opakuje už opakovacou
    deliacou funkciou"""
    if pocet_1 > 50:
        bbox_1 = [minx, y_mean, x_mean, maxy]
        delenie_bodov_opakovane(cluster_id_1, bbox_1, vstup)
    if pocet_2 > 50:
        bbox_2 = [x_mean, y_mean, maxx, maxy]
        delenie_bodov_opakovane(cluster_id_2, bbox_2, vstup)
    if pocet_3 > 50:
        bbox_3 = [minx, miny, x_mean, y_mean]
        delenie_bodov_opakovane(cluster_id_3, bbox_3, vstup)
    if pocet_4 > 50:
        bbox_4 = [x_mean, miny, maxx, y_mean]
        delenie_bodov_opakovane(cluster_id_4, bbox_4, vstup)


def delenie_bodov_opakovane(cluster_id, bbox, vstup):
    """Delenie bodov pomocou mechanizmu quadtree. Iba pre pokračujúci beh (musí existovať atribút cluster_id)"""
    minx = bbox[0]
    miny = bbox[1]
    maxx = bbox[2]
    maxy = bbox[3]
    pocet_1, pocet_2, pocet_3, pocet_4 = 0, 0, 0, 0
    cluster_id_1, cluster_id_2, cluster_id_3, cluster_id_4 = 0, 0, 0, 0
    x_mean = (maxx + minx) / 2
    y_mean = (maxy + miny) / 2

    for p in vstup['features']:
        """Samotné roztriedenie na 4 oblasti a následné priradenie cluster_id atribútu"""
        if p['geometry']['coordinates'][0] < x_mean and p['geometry']['coordinates'][1] > y_mean and p['properties']['cluster_id'] == cluster_id:
            pocet_1 += 1
            cluster_id_1 = pridanie_cluster_id(p, 1)
        if p['geometry']['coordinates'][0] > x_mean and p['geometry']['coordinates'][1] > y_mean and p['properties']['cluster_id'] == cluster_id:
            pocet_2 += 1
            cluster_id_2 = pridanie_cluster_id(p, 2)
        if p['geometry']['coordinates'][0] < x_mean and p['geometry']['coordinates'][1] < y_mean and p['properties']['cluster_id'] == cluster_id:
            pocet_3 += 1
            cluster_id_3 = pridanie_cluster_id(p, 3)
        if p['geometry']['coordinates'][0] > x_mean and p['geometry']['coordinates'][1] < y_mean and p['properties']['cluster_id'] == cluster_id:
            pocet_4 += 1
            cluster_id_4 = pridanie_cluster_id(p, 4)
    """Zisťovanie, či je počet bodov v jednom  clustri nad 50. Pokiaě áno, delenie bodov sa opakuje"""
    if pocet_1 > 50:
        bbox_1 = [minx, y_mean, x_mean, maxy]
        delenie_bodov_opakovane(cluster_id_1, bbox_1, vstup)
    if pocet_2 > 50:
        bbox_2 = [x_mean, y_mean, maxx, maxy]
        delenie_bodov_opakovane(cluster_id_2, bbox_2, vstup)
    if pocet_3 > 50:
        bbox_3 = [minx, miny, x_mean, y_mean]
        delenie_bodov_opakovane(cluster_id_3, bbox_3, vstup)
    if pocet_4 > 50:
        bbox_4 = [x_mean, miny, maxx, y_mean]
        delenie_bodov_opakovane(cluster_id_4, bbox_4, vstup)


def pridanie_cluster_id(vstup, cluster_id):
    """Vstup jednej feature zo zoznamu, pridava cluster id podľa kľúča v dokumentácii"""
    zaznam = vstup['properties']
    try:
        var = zaznam['cluster_id']
    except KeyError:
        var = 0
    new_cluster_id = var*10 + cluster_id
    zaznam.update({'cluster_id': new_cluster_id})
    return new_cluster_id


def calculator_bbox(vstup):
    """Zistí bbox a vracia ho ako zoznam minx, miny, maxx, maxy"""
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


delenie_bodov(calculator_bbox(geojson), geojson)

with open(filename_export, 'w') as geojson_file:
    json.dump(geojson, geojson_file)