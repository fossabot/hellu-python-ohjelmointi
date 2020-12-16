# Kirjoita ratkaisu tähän
kirjain1 = input("Anna 1. kirjain: ")
kirjain2 = input("Anna 2. kirjain: ")
kirjain3 = input("Anna 3. kirjain: ")

if kirjain2 < kirjain1 < kirjain3 or kirjain3 < kirjain1 < kirjain2:
    print("Keskimmäinen kirjain on", kirjain1)
if kirjain1 < kirjain2 < kirjain3 or kirjain3 < kirjain2 < kirjain1:
    print("Keskimmäinen kirjain on", kirjain2)
if kirjain1 < kirjain3 < kirjain2 or kirjain2 < kirjain3 < kirjain1:
    print("Keskimmäinen kirjain on", kirjain3)