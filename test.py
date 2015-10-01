"""This code will ask a series of questions, and
provide the user with a drink.

Constants:
    QUESTIONS (dict): Contains the types of drink, as well as the
        respective follow-up question. This is in the form of
	{adjective (str): question (str)}.
    INGREDIENTS (dict): Contains the types of ingredients, as well 
        as a description of those ingredients. This is in the form
        of {adjective (str): list of ingredients (list[str])}.
    DRINKNAME (list[str]): Contains a list of "random" (manually
        specified/non-dynamic [not generated]) drink names.

Note:
    If you look at the bottom of this file, there is a runtime.

See Also:
    * Bulit-in random module

"""

import random


# These are the type of drink and follow up question
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


def ask_questions():
    """ask_questions will ask user a series of questions and record
    responses as a boolean 
  
    Example:
        >>> answers = ask_questions()
        "Do you like your drink strong?" : y
        "Do you like drink sweet?" : n
        >>> answers
        {'strong': True, 'sweet': False}

    Returns:
        dict: Returns a dictionary of True or False questions whether
            a user likes an ingredient or not. Example:

            >>> {'strong': True, 'sweet': False}

    Raises:
        exception: If the user answers 'n' to all the questions,
            it will be impossible to make a new drink. Thus, this
            error is raised.

    """

    answers = {}
    print("Answer each question ('y' or 'n') to determine your drink.")

    for key, value in QUESTIONS.items():
        reply = raw_input(value).lower()

        if reply == "y":
            answers[key] = True
        else:
            answers[key] = False

    if not any(answers.values()):

        raise Exception("You need to like SOMETHING to make a drink!")

    return answers


def create_drink(answers):
    """Create a drink using user supplied responses to QUESTIONS
    out of INGREDIENTS chosen by those questions.

    Based on responses to QUESTIONS a random INGREDIENT will be chosen.

    Args:
        answers (dict): Answers will be a dictionary of adjectives
            describing ingredients, with a boolean representing
            a yes or no answer (if the user likes that kind
            of ingredient or not). Example:
	
            >>> answers = {'bitter': False, 'strong': True}

    Return:
        tuple(str): Generated drink name, along with randomly
            chosen ingredients. Each of the two elements are
            strings.

            >>> ('Deaths Door', 'glug of rum') 

    Notes:
        prints the drink name, returns the ingredients.

    See Also:
      * QUESTIONS
      * INGREDIENTS
      * random.choice
      * ask_questions()

    """

    print(answers)
    generated_drink_name = random.choice(DRINKNAME)
    print(("\nHere's your drink! It is a {drinkname}.".
           format(drinkname=generated_drink_name)))

    # ingredient adjective, bool representing if user likes it
    for ingredient_adjective, yes_or_no in answers.items():

        if yes_or_no:
            new_drink ="{0}".format(random.choice(INGREDIENTS[key]))

    return generated_drink_name, new_drink


# Runtime -- local scope, this doesn't execute if this module
# is imported, rather than ran through python directly.
if __name__ == "__main__":
    answers = ask_questions()
    drink_name, ingredients = create_drink(answers)
    print(drink_name + ingredients)
