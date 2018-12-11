import json

with open("Elektricky_Bratislava.geojson", encoding='utf-8') as f:
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
    zaznam = vstup
    try:
        var = zaznam["cluster_id"]
    except KeyError:
        var = 0
    new_cluster_id = var*10 + cluster_id
    zaznam.update({"cluster_id": new_cluster_id})
    return zaznam

q = calculator_bbox(gj)
print(q)

pridanie_cluster_id(features, 8)
print(features)

def delenie_bodov(bbox, vstup):
    minx = bbox[0]
    miny = bbox[1]
    maxx = bbox[2]
    maxy = bbox[3]
    x_mean = (maxx+minx)/2
    y_mean = (maxy+miny)/2
    print(x_mean, y_mean)
    for p in vstup['features']:
        if p['geometry']['coordinates'][0] < x_mean and p['geometry']['coordinates'][1] > y_mean:
            pridanie_cluster_id(p, 1)
        if p['geometry']['coordinates'][0] > x_mean and p['geometry']['coordinates'][1] > y_mean:
            pridanie_cluster_id(p, 2)
        if p['geometry']['coordinates'][0] < x_mean and p['geometry']['coordinates'][1] < y_mean:
            pridanie_cluster_id(p, 3)
        if p['geometry']['coordinates'][0] > x_mean and p['geometry']['coordinates'][1] < y_mean:
            pridanie_cluster_id(p, 4)

delenie_bodov(calculator_bbox(gj), gj)
#print(gj)
featur = gj['features'][101]
print(featur)
for i in gj['features']:
    print(i)

print(gj)