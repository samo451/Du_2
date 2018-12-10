import geojson

with open("Elektricky_Bratislava.geojson", encoding='utf-8') as f:
    gj = geojson.load(f)
features = gj['features'][102]
print(features)

#Vypísanie geometrie
y = gj['features'][102]['geometry']['coordinates']
print(y)

#for feature in gj['features']:
#    print(feature)


