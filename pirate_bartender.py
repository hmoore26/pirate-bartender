import random

answers = {}

# These are the type of drink and follow up question

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

# These are the corresponding ingredients

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

# Random drink names

drinkname = ["Fuzzy Navel", "Bridge Troll", "Death Door", "Ring of fire"]

def ask_questions():
    print "Answer each question ('y' or 'n') to determine your drink."
    for key, value in questions.items():
        reply = raw_input(value).lower()
        if reply == "y":
            answers[key] = True
        else:
            answers[key] = False
    return answers

#Create the drink based on the answers given by matching answers and selecting a random matching ingredient.Then choose a random name from drinkname list
   
def create_drink(answers, ingredients):
   
    print "\nHere's your drink! It is a {drinkname}.".format(drinkname=random.choice(drinkname))
    for key, value in answers.items():
        if value is True:
            print "{0}".format(ingredients[key][random.randint(0, 2)])
    return


if __name__ == "__main__":
    ask_questions()
    create_drink(answers,ingredients)
