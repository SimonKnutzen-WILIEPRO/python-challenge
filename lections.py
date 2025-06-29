## Lektion 1
# In dieser Lektion starten wir mit den Grundlagen der Programmierung mit Python.
# Wir lernen die grundlegenden Konzepte der Programmierung kennen,
# wie Befehle, Variablen und den sequentiellen Ablauf von Befehlen.
# Wir werden
# Wie verarbeitet der Computer unseren Befehlscode?
# Sequentieller Ablauf von Befehlen:
# Jede Zeile beinhaltet einen Befehl, der nacheinander ausgeführt wird.
# Der Computer führt die Befehle in der Reihenfolge aus, in der sie geschrieben sind.
# Der Computer macht exakt das, was wir ihm sagen. D.h. wir müssen sehr genau sein.
# (Der Computer macht was wir ihm sagen, nicht was wir meinen.

print("Hallo Welt")
print("Hallo Welt 2")

# Python beherrscht von sich aus viele grundlegende Befehle wie z.B. print,
# was Text auf dem Bildschirm ausgibt, oder grundrechenarten wie Addition,
# Subtraktion, Multiplikation und Division.

print(2 + 3)  # Addition

# Darüber hinaus gibt es viele weitere (komplexere) Befehle, 
# die in Python verwendet werden können.
# Viele dieser Befehle stehen nicht direkt zur verfügung, sondern sind in 
# sogenannten Bibliotheken (oder Modulen) enthalten,
# aus denen diese erst importiert werden müssen, um sie nutzen zu können. 
# Viele dieser Bibliotheken sind bereits in Python enthalten,
# andere müssen separat installiert werden.

# Beispiel: Aktuelles Datum und Uhrzeit abrufen
# Importieren des datetime-Modul.
# Das datetime-Modul ist eine Standardbibliothek in Python,
# und ist bereits in der Python-Installation enthalten.
# Diese Bibliothek ermöglicht es uns, mit Datums- und Zeitangaben zu arbeiten.
from datetime import datetime
print(datetime.now()) 
# Der Befehl 'now()' gibt das aktuelle Datum und die aktuelle Uhrzeit zurück.

# Zur Syntax der meisten Befehle in Python gehört, dass sie mit einem
# Namen beginnen, gefolgt von Klammern, die Parameter enthalten können.
# Sollte der Befehl keine Parameter benötigen, können die Klammern leer bleiben.
# Da der now()-Befehl aus dem datetime-Modul stammt,
# muss er mit dem Modulnamen (datetime) und einem Punkt (.) aufgerufen werden.
# Hierzu später mehr.

# Jeder Befehl, der ein Ergebnis liefert, muss so geschrieben werden, 
# dass mit dem Ergebnis etwas gemacht wird, da das Ergebnis sonst verloren geht.
2+3  # Das Ergebnis wird nicht angezeigt, da es nicht mit print ausgegeben wird.

## Variablen
# Anstatt Werte direkt zu verwenden, können wir sie in Variablen speichern.
# Variablen sind wie Kisten, in denen wir Werte speichern können.

ergebnis = 2 + 3  # Das Ergebnis der Addition wird in der Variable 'ergebnis' gespeichert.
# Die Variable 'ergebnis' kann nun später verwendet werden, um den Wert anzuzeigen oder weiter zu verarbeiten.
print(ergebnis)  # Ausgabe des Wertes der Variable 'ergebnis'

# # Datentypen von Variablen

# Variablen können verschiedene Datentypen besitzen. 

# Einen ersten Datentyp haben wir bereits in der ersten Lektion kennengelernt: _string_ (Dieser wird benutzt, um Text in Variablen abzuspeichern)

# Der Datentyp einer Variablen muss in Python nicht explizit angegeben werden.
# Python erkennt den Datentyp automatisch, basierend auf dem zugewiesenen Wert. 
# Wird die Variable später mit einem anderen Datentyp überschrieben, ändert sich der Datentyp der Variable entsprechend.
# Die beiden anderen wichtigen Datentypen, die wir in dieser Lektion kennenlernen, sind _integer_ (Ganzzahlen) und _float_ (Gleitkommazahlen).
# Ein Integer ist eine ganze Zahl, z.B. 1, 2, 3, -1, -2, -3.
# Ein Float ist eine Zahl mit Dezimalstellen, z.B. 1.0, 2.5, -3.14, 0.001.

# Wenn wir eine Variable in einem Befehl verwenden, wird der Datentyp der Variable automatisch erkannt und entsprechend verarbeitet. 
# Verwenden wir beispielsweise eine Variable, die einen String enthält, in einer mathematischen Operation, wird Python einen Fehler ausgeben.