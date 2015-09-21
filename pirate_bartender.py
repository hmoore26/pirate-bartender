def find_preferences():
    preferences = {}
    for type, question in questions.iteritems():
        print question
        preferences[type] = raw_input().lower() in ["y", "yes"]
        print ""
    return preferences
    
def make_drink(preferences):
    drink = []
    for ingredient_type, liked in preferences.iteritems():
        if not liked:
            continue

        drink.append(random.choice(ingredients[ingredient_type]))
    return drink


def main():
    preferences = find_preferences()
    drink = make_drink(preferences)
    print "One drink coming up."
    print "It's full of good stuff.  The recipe is:"
    for ingredient in drink:
        print "A {}".format(ingredient)

if __name__ == "__main__":
    main()
