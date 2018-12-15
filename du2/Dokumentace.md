# Dokumentácia k DÚ č. 2
# Delenie bodov metódou quadtree
## Charakteristika programu.
Program slúži na delenie bodov pomocou metódy quadtree na bloky o počte maximálne 50 bodov pre blok. Každému bodu pridelí 
atribút cluster_id, kde sa daná hodnota clustru uloží (podľa schémy nižšie). V prípade opakovaní sa vrámci väčšieho štvorca
vytvorí ďalší štvorec, s atribútami podľa rovnakej schémy (tj. pre štvorec č. 1 sa vytvoria ďalšie atribúty podľa 
schémy 1x). V prípade, že budú body na deliacej línii, program pridelí body na nej automaticky k skupine na východ, 
alebo na juh od nej.

1 | 2 \
--+-- \
3 | 4

###Spustenie programu:
Prvým argumentom je názov programu Du2.py, ktorý chceme spúšťať, druhým argumentom je vstupná bodová vrstva 
vo formáte geoJSON a tretím je výstupná vrstva vo formáte geoJSON, ktorá sa vytvorí.
######Príklad spustenia:
Du2.py vstupny.geojson vystupny.geojson 

####Vstup do programu:
GeoJSON súbor s bodovou vrstvou.

####Výstup programu:
GeoJSON súbor s bodovou vrstvou doplnený o atribút cluster_id.

####Beh programu:
Po spustení programu zistí program, či je počet vstupných parametrov dostatočný a či spĺňaju náležitosti programu.
Následne program zistí bbox okolo bodov a následne spustí delenie pomocou quadtree až po bod, kedy sa na všetkých podskupinách 
nenachádza maximálne 50 bodov. Následne program uloží výsledok vo formáte geojson.

####Exit kódy programu:
1) Nedostatočný počet argumentov - postupujte podľa príkladu behu programu uvedenému vyššie
2) Vstupný súbor nie je možné otvoriť
3) Chybný vstupný súbor - vás súbor je pravdepodobne poškodený
4) Chyba pri zápise - neexistuje cesta k súboru.
5) Neplatný geoJSON súbor - neobsahuje súradnice v: ['features']'geometry']['coordinates']
6) Chyba pri zápise - nie je povolený zápis