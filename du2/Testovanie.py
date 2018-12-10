import geojson

with open("Elektricky_Bratislava.geojson", encoding='utf-8') as f:
    gj = geojson.load(f)
features = gj['features'][10]
print(features)

#Vypísanie geometrie
y = gj['features'][102]['geometry']['coordinates']
print(y)



# Pridavanie cluster id aj s updatom
def pridanie_cluster_id(vstup):
    #for feature in vstup['features']:
    #    var = "5"
    #    feature.update({"cluster_id": var})
    try:
        var = feature["cluster_id"]
    except:
        var = "1"
    for feature in vstup['features']:
        vari = var + "8"
        feature.update({"cluster_id": vari})
    return vstup

test = pridanie_cluster_id(gj)

features2 = test['features'][14]
print(features2)