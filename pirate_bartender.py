"""This code will ask a series of questions, 

Tip:
    random.choice(): --

"""

import random


# These are the type of drink and follow up question
# this is a constant
# questions (rename): QUESTIONS
QUESTIONS = {
        "strong": "Do ye like yer drinks strong?",
        "salty": "Do ye like it with a salty tang?",
        "bitter": "Are ye a lubber who likes it bitter?",
        "sweet": "Would ye like a bit of sweetness with yer poison?",
        "fruity": "Are ye one for a fruity finish?"
}

# These are the corresponding ingredients
INGREDIENTS = {
        "strong": ["glug of rum", "slug of whisky", "splash of gin"],
        "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
        "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
        "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
        "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

# Random drink names
DRINKNAME = ["Fuzzy Navel", "Bridge Troll", "Death Door", "Ring of fire"]


def ask_questions(answers):
    answers = {}
    print("Answer each question ('y' or 'n') to determine your drink.")

    for key, value in questions.items():
        reply = raw_input(value).lower()

        if reply == "y":
            answers[key] = True
        else:
            answers[key] = False

    return answers


def create_drink(answers, ingredients):
    """Create the drink based on the answers given by matching answers
    and selecting a random matching ingredient. Then choose a random
    name from the drinkname list.

    Args:
        answer (dict): --
        ingredients (dicts): --

    Returns:
        str: The name of the new drink.

    """
   
    print(a)
    print "\nHere's your drink! It is a {drinkname}.".format(drinkname=random.choice(drinkname))

    for key, value in answers.items():

        if value is True:
            # use random.choice instead
            new_drink ="{0}".format(random.choice(ingredients))

    return new_drink


# Runtime -- local scope, this doesn't execute if this module
# is imported, rather than ran through python directly.
if __name__ == "__main__":
    answers = ask_questions()
    create_drink(answers, ingredients)
