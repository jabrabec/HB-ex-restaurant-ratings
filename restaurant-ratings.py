import sys

filename = sys.argv[1]


def print_ratings(filename):
    """Processes a file of restaurants and their ratings.

    Takes a filename argument on the command line and iterates over it to read
    restaurant scores. Returns output in full sentence form. Text file with
    scores must be called on the command line in argv[1] position.
    """
    restaurant_ratings = {}

    with open(filename) as rest_scores:
        for line in rest_scores:
            name, rating = line.strip().split(":")
            restaurant_ratings[name] = rating

    while True:
        print "\nDo you want to:"
        print "1: See all current ratings?"
        print "2: Add a new restaurant and rate it?"
        print "Or 3: Quit?"
        user_choice = raw_input("Choose one: ")

        if user_choice == '1':
            for name, rating in sorted(restaurant_ratings.items()):
                print "%s is rated at %s." % (name, rating)        

        elif user_choice == '2':
            user_add_name = raw_input("Please enter a restaurant name: ").title()
            user_add_rating = raw_input("Please enter a restaurant rating: ")

            restaurant_ratings[user_add_name] = user_add_rating

            for name, rating in sorted(restaurant_ratings.items()):
                print "%s is rated at %s." % (name, rating)

        elif user_choice == '3':
            print "Thanks!"
            return

        else:
            print "Please enter 1, 2, or 3."

print_ratings(filename)
