#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Number Guessing Game
Beschreibung: Der Computer wählt eine Zufallszahl zwischen 1 und 100.
Der Spieler muss diese in maximal 7 gültigen Versuchen mit den Hinweisen „Too Low“ / „Too High“ erraten.
"""

import random

def spiel_starten():
    # 1. Generierung der geheimen Zufallszahl zwischen 1 und 100
    geheimzahl = random.randint(1, 100)
    
    # Initialisierung des Zählers für gültige Versuche
    max_versuche = 7
    verbleibende_versuche = max_versuche
    
    print("=" * 50)
    print(" Willkommen beim Number Guessing Game! ")
    print(" Ich habe eine Zahl zwischen 1 und 100 ausgewählt.")
    print(f" Sie haben maximal {max_versuche} gültige Versuche.")
    print("=" * 50)
    
    # 2. Hauptspielschleife (läuft, solange noch gültige Versuche übrig sind)
    while verbleibende_versuche > 0:
        print(f"\nVerbleibende Versuche : {verbleibende_versuche}/{max_versuche}")
        
        # Fehlerbehandlung bei ungültiger Benutzereingabe (z. B. Text statt einer Zahl)
        try:
            eingabe = input("Geben Sie eine Zahl ein : ")
            vorschlag = int(eingabe)
        except ValueError:

            # Eine ungültige Eingabe verbraucht keinen Versuch
            print("Fehler : Bitte geben Sie eine gültige ganze Zahl ein. (Dieser Fehler verbraucht keinen Versuch).")
            continue
            
        # Überprüfung, ob die Zahl im gültigen Bereich [1, 100] liegt
        if vorschlag < 1 or vorschlag > 100:
            # Eine Zahl außerhalb des Bereichs verbraucht ebenfalls keinen Versuch
            print("Fehler : Die Zahl muss zwischen 1 und 100 liegen. (Dieser Fehler verbraucht keinen Versuch).")
            continue
            
        # 3. Vergleich der Eingabe mit der geheimen Zahl und Ausgabe der Hinweise
        if vorschlag == geheimzahl:

            # Sofortiger Sieg, wenn die Zahl erraten wurde
            print(f"🎉 Herzlichen Glückwunsch! Sie haben die geheime Zahl {geheimzahl} erfolgreich erraten!")
            break
        elif vorschlag < geheimzahl:

            print("Too Low (Zu niedrig)!")
            verbleibende_versuche -= 1
        else:
            
            print("Too High (Zu hoch)!")
            verbleibende_versuche -= 1
            
    # 4. Spielende bei Niederlage (wenn alle 7 Versuche aufgebraucht wurden)
    if verbleibende_versuche == 0:
        print("\n" + "x" * 50)
        print(" Schade! Sie haben alle Ihre Versuche aufgebraucht.")
        print(f" Die geheime Zahl lautet : {geheimzahl}")
        print("x" * 50)

# Einstiegspunkt des Programms
if __name__ == "__main__":
    spiel_starten()