"""
Faceti un program care cere de la utilizator (in consola de executie) date despre cursantii de la SDA
(exemplu: nume, prenume, varsta, ocupatie, hobby, email, telefon)

Apoi inregistrati aceste date in fisiere individuale atat de format json cat si csv.
La final creati un fisier json si csv care sa le contina pe toate celelalte individuale.

incarcati repozitorul pe github din comenzi "git" din consola.
Adaugati o validare de numar de telefon si email prin regex (import re).
 Acest feature sa fie intr-un branch diferit pe github, la fel creat din prin comenzi git.

 Faceti un fisier json de statistica al tuturor cursantilor inregistrati, care sa contina date ce caracterizeaza grupa, de exemplu dar nu limitat la:
-numar de studenti total
-cel mai lung prenume
-persoana cu cele mai multe vocale in prenume
-intervalul de varsta- min&max
-lista de ocupatii
-o lista cu domeniile de email folosite, unice (ex: ['gmail', 'yahoo'] etc)
-și/sau alte date care le considerati relevante din structura care ati construit-o despre cursanti
Acest feature sa fie pe un alt branch pe github, la fel ”uploaded” prin consola cu instructiuni git
"""

import json
import csv


print("Introduceți datele cursantului SDA:")

nume = input("Nume: ")
prenume = input("Prenume: ")
varsta = input("Varsta: ")
ocupatie = input("Ocupatie: ")
hobby = input("Hobby: ")
email = input("Email: ")
telefon = input("Telefon: ")

cursant = {"Nume": nume,
           "Prenume": prenume,
           "Varsta": varsta,
           "Ocupatie": ocupatie,
           "Hobby": hobby,
           "Email": email,
           "Telefon": telefon}

with open(nume + "_" + prenume + ".json", "a") as f:
    json.dump(cursant, f, indent=4)


with open(nume + "_" + prenume + ".csv", "a", newline="") as f:
    writer = csv.writer(f)
    for key, value in cursant.items():
        writer.writerow([key, value])


cursanti = []
cursanti.append(cursant)


with open("cursanti.json", "a") as f:
    json.dump(cursanti, f, indent=4)


with open("cursanti.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(cursanti[0].keys())
    for cursant in cursanti:
        writer.writerow(cursant.values())

print("Datele au fost înregistrate cu succes!")
