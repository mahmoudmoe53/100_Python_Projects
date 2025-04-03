import pandas

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

file1 = pandas.read_csv("nato_phonetic_alphabet.csv")

nato = pandas.DataFrame(file1)

nato_dict = {row["letter"]:row["code"] for (index, row) in nato.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

name = input("Please insert name:\n").upper()

nato_name = [nato_dict[letters] for letters in name]

print(nato_name)


