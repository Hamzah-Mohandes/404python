String = 'Python is 404 :D'

# capitalize(): Wandelt den ersten Buchstaben eines Strings in einen Großbuchstaben um.
# lower(): Wandelt alle Buchstaben in einem String in Kleinbuchstaben um.
# upper(): Wandelt alle Buchstaben in einem String in Großbuchstaben um.
# title(): Wandelt den ersten Buchstaben jedes Wortes in einem String in einen Großbuchstaben um.
# swapcase(): Wandelt Großbuchstaben in Kleinbuchstaben und umgekehrt um.
# strip(): Entfernt führende und abschließende Leerzeichen aus einem String.
# split(): Teilt einen String anhand eines bestimmten Trennzeichens in eine Liste von Teilstrings auf.
# join(): Verbindet Elemente einer Liste zu einem String, indem ein bestimmtes Trennzeichen zwischen den Elementen eingefügt wird.
# replace(): Ersetzt alle Vorkommen eines bestimmten Substrings in einem String durch einen anderen Substring.
# find(): Sucht nach dem ersten Vorkommen eines Substrings in einem String und gibt den Index zurück, an dem es gefunden wurde (falls vorhanden).
# startswith(): Überprüft, ob ein String mit einem bestimmten Substring beginnt.
# endswith(): Überprüft, ob ein String mit einem bestimmten Substring endet.
# len(): Gibt die Länge eines Strings zurück.

print (String.capitalize())
print (String.lower())
print (String.upper())
print (String.title())
print (String.swapcase())
print (String.strip())
print (String.split()) ## keine Leerzeichen am anfang oder ende

liste_of_words = ['Hallo', 'Welt']
print (", nachdem das fügt an ".join(liste_of_words))
print(String.replace('Python', 'Java'))
print(String)
print(String.find('is'))
print(String.startswith('Python'))
print(String.endswith('D'))
print(len(String))