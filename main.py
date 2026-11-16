#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Number Guessing Game
Beschreibung: Der Computer wählt eine Zufallszahl zwischen 1 und 100.
Der Spieler muss diese in maximal 7 gültigen Versuchen mit den Hinweisen „Too Low“ / „Too High“ erraten.
"""

import random

def spiel_starten():
    # Endlosschleife für den Wiederholungs-Modus (Nochmal spielen-Bonus)
    while True:
        print("\n" + "=" * 50)
        print(" Willkommen beim Number Guessing Game! ")
        print("=" * 50)
        print("Wählen Sie den Schwierigkeitsgrad:")
        print("1. Leicht (10 Versuche)")
        print("2. Normal (7 Versuche)")
        print("3. Schwer (5 Versuche)")
        
        # Auswahl des Schwierigkeitsgrads (Schwierigkeitsgrad-Bonus)
        try:
            schwierigkeitsgrad = int(input("Geben Sie die Nummer des Schwierigkeitsgrads ein (1-3) : "))
            if schwierigkeitsgrad == 1:
                max_versuche = 10
            elif schwierigkeitsgrad == 3:
                max_versuche = 5
            else:
                max_versuche = 7  # Standard (Normal)
        except ValueError:
            max_versuche = 7  # Standard bei falscher Eingabe
            print("Ungültige Eingabe. Standard-Modus (7 Versuche) wird gewählt.")

        # 1. Generierung der geheimen Zufallszahl zwischen 1 und 100
        geheimzahl = random.randint(1, 100)
        
        # Initialisierung des Zählers für gültige Versuche
        verbleibende_versuche = max_versuche
        # Initialisierung der Historie (Historie-Bonus)
        historie_versuche = []
        
        print(f" Ich habe eine Zahl zwischen 1 und 100 ausgewählt.")
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
                
            # Zur Historie hinzufügen (Historie-Bonus)
            historie_versuche.append(vorschlag)
                
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
                
        # 4. Spielende bei Niederlage (wenn alle Versuche aufgebraucht wurden)
        if verbleibende_versuche == 0:
            print("\n" + "x" * 50)
            print(" Schade! Sie haben alle Ihre Versuche aufgebraucht.")
            print(f" Die geheime Zahl lautet : {geheimzahl}")
            print("x" * 50)
            
        # Historie am Ende der Partie anzeigen (Historie-Bonus)
        print(f"\nIhre Versuche in dieser Partie : {historie_versuche}")
        
        # Nochmal spielen (Wiederholungs-Bonus)
        nochmal_spielen = input("\nMöchten Sie noch einmal spielen? (j/n) : ").strip().lower()
        if nochmal_spielen != 'j' and nochmal_spielen != 'ja':
            print("Vielen Dank fürs Spielen. Auf Wiedersehen!")
            break

# Einstiegspunkt des Programms
if __name__ == "__main__":
    spiel_starten()