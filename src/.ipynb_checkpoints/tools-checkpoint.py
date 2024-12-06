import os
import csv

def gen(skip=False):
    regions = ("at", "bo", "ch", "cl", "da", "kc", "mi", "ny", "ph", "ri", "sf", "sl", "su")
    for year in range(2010, 2025):
        os.makedirs(f"../data/beige_books/txt/{year}", exist_ok=True)
        for month in range(1, 13):
            os.makedirs(f"../data/beige_books/txt/{year}/{month:02d}", exist_ok=True)
            for region in regions:
                yield year, month, region

def get_txt_file(t):
    return f"../data/beige_books/txt/{t[0]}/{t[1]:02d}/{t[0]}-{t[1]:02d}-{t[2]}.txt"

def get_txt_string(year, month, region, printing=False):
    if printing: print(f"{year} {month:02d} {region}") # pylint: disable=multiple-statements
    filename = get_txt_file((year, month, region))
    with open(filename, "r") as f:
        s = f.read()
    return s
