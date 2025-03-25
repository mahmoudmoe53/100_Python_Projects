PLACEHOLDER = "[name]"
with open("Input/Names/invited_names.txt") as names:
    list_of_names = names.readlines()



with open("Input/Letters/starting_letter.txt") as letter:
    letter_contents = letter.read()
    for person in list_of_names:
        stripped_name = person.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"Output/ReadyToSend/{stripped_name}'s_letter.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)











