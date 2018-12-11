import geojson

with open("Elektricky_Bratislava.geojson", encoding='utf-8') as f:
    gj = geojson.load(f)
features = gj['features'][10]
print(features)

#Vypísanie geometrie
y = gj['features'][102]['geometry']['coordinates']
print(y)



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