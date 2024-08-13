"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Tereza Růžičková
email: terkaruzicka@seznam.cz
discord: terka_99
"""
print("Enter username:",)
username = input()
print("username:", username)

print("Enter password:")
password = input()
print("password:", password)

print("-" * 40)

login_data = {"bob" : "123",
               "ann" : "pass123",
               "mike" : "password123",
               "liz" : "pass123"}

if login_data.get(username) == password:
    print("Welcome to the app,", username)
    print("We have 3 texts to be analyzed.")
    print("-" * 40)

    TEXTS = {
            1: '''Situated about 10 miles west of Kemmerer,
             Fossil Butte is a ruggedly impressive
             topographic feature that rises sharply
             some 1000 feet above Twin Creek Valley
             to an elevation of more than 7500 feet
             above sea level. The butte is located just
             north of US 30N and the Union Pacific Railroad,
             which traverse the valley. ''',
             2: '''At the base of Fossil Butte are the bright
             red, purple, yellow and gray beds of the Wasatch
             Formation. Eroded portions of these horizontal
             beds slope gradually upward from the valley floor
             and steepen abruptly. Overlying them and extending
             to the top of the butte are the much steeper
             buff-to-white beds of the Green River Formation,
             which are about 300 feet thick.''',
             3: '''The monument contains 8198 acres and protects
             a portion of the largest deposit of freshwater fish
             fossils in the world. The richest fossil fish deposits
             are found in multiple limestone layers, which lie some
             100 feet below the top of the butte. The fossils
             represent several varieties of perch, as well as
             other freshwater genera and herring similar to those
             in modern oceans. Other fish such as paddlefish,
             garpike and stingray are also present.'''
            }
    
    print("Enter a number btw. 1 and 3:")
    print("-" * 40)

    text_number_input = input()
    if text_number_input.isdigit() is True:
        if int(text_number_input) in TEXTS:
            text_number = int(text_number_input)
            chosen_text = TEXTS[text_number]
            word_list = chosen_text.split()
            word_count = len(word_list)
            print(f"There are {word_count} words in the selected text")
            titlecase_count = 0
            capitalized_count = 0
            lowercase_count = 0
            numbers_count = 0
            sum_of_numbers = 0
            word_length_freq = {}
            for word in word_list:
                if word.istitle() is True:
                    titlecase_count += 1
                if word.isupper() is True and word.isalpha() is True:
                    capitalized_count += 1
                if word.islower() is True:
                    lowercase_count += 1
                if word.isdigit() is True:
                    numbers_count += 1
                    number = int(word)
                    sum_of_numbers += number
                word_length = len(word.strip(",.?!"))
                if word_length in word_length_freq:
                        word_length_freq[word_length] +=1
                else:
                        word_length_freq[word_length] = 1
            print("There are", titlecase_count, "titlecase words.")
            print("There are", capitalized_count, "uppercase words.")
            print("There are", lowercase_count,"lowercase words.")
            print("There are", numbers_count, "numeric strings")
            print("The sum of all the numbers is", sum_of_numbers)
            print("-" * 40)
            print(f"{'Length':<6} | {'Occurences':<20} | {'Number':<3}")
            print("-" * 40)
            for length in sorted(word_length_freq):
                print(f"{length:<6} | {'*' * word_length_freq[length]:<20} | {word_length_freq[length]:<3}")
        else:
            print("No text was found for the given number, terminating the program...")
    else:
        print("Input is not a number, terminating the program..")
else:
    print("Unregistered user, terminating the program...")
