import json
import turtle

with open("Elektricky_Praha.geojson", encoding='utf-8') as f:
    gj = json.load(f)
features = gj['features'][100]
print(features)

#Vypísanie geometrie
y = gj['features'][102]['geometry']['coordinates']
print(y)


"""
# Pridavanie cluster id aj s updatom
def pridanie_cluster_id(vstup, cluster_id):
    #for feature in vstup['features']:
    #    var = "5"
    #    feature.update({"cluster_id": var})
    for feature in vstup['features']:
        try:
            var = feature["cluster_id"]
        except KeyError:
            var = 0
        new_cluster_id = var*10 + cluster_id
        feature.update({"cluster_id": new_cluster_id})
    return vstup

test = pridanie_cluster_id(gj, 1)

features2 = test['features'][14]
print(features2)
test2 = pridanie_cluster_id(test, 2)
features3 = test2['features'][14]
print(features3)
print(features)
"""

def calculator_bbox(vstup):
    """Returnuje Rectangle bbox"""
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
    bbox = [minx, miny,maxx, maxy]
    print(minx, miny, maxx, maxy)
    return bbox

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

q = calculator_bbox(gj)
print(q)

pridanie_cluster_id(features, 8)
print(features)

def delenie_bodov(bbox, vstup):
    minx = bbox[0]
    miny = bbox[1]
    maxx = bbox[2]
    maxy = bbox[3]
    pocet_1, pocet_2, pocet_3, pocet_4 = 0, 0, 0, 0
    cluster_id_1, cluster_id_2, cluster_id_3, cluster_id_4 = 0, 0, 0, 0
    x_mean = (maxx+minx)/2
    y_mean = (maxy+miny)/2
    print(x_mean, y_mean)

    for p in vstup['features']:

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
    print(pocet_1, pocet_2, pocet_4, pocet_3)
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
    minx = bbox[0]
    miny = bbox[1]
    maxx = bbox[2]
    maxy = bbox[3]
    pocet_1, pocet_2, pocet_3, pocet_4 = 0, 0, 0, 0
    x_mean = (maxx + minx) / 2
    y_mean = (maxy + miny) / 2
    print(x_mean, y_mean)
    for p in vstup['features']:
        coordinates = p['geometry']['coordinates']
        turtle_kresli_body(coordinates, bbox)
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
    print(pocet_1, pocet_2, pocet_4, pocet_3)
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

def turtle_kresli_body(coordinates, bbox):
    minx = bbox[0]
    miny = bbox[1]
    maxx = bbox[2]
    maxy = bbox[3]
    x, y = coordinates[0], coordinates[1]

    turtle.penup()
    turtle.goto(x, y)
    turtle.pencolor("white")
    turtle.dot(5)
    turtle.goto(0, 0)


turtle.screensize(5000,5000,"black")
delenie_bodov(calculator_bbox(gj), gj)
#print(gj)
featur = gj['features'][101]
print(featur)


def ulozenie_geojson (export):
    with open('export_praha_zastavky.geojson', 'w') as geojson_file:
        json.dump(export, geojson_file)


ulozenie_geojson(gj)




turtle.screensize(5000,500,"black")
turtle.pencolor("white")
turtle.dot(1)
turtle.exitonclick()
#for i in gj['features']:
#    print(i)

#print(gj)