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

    for name, rating in sorted(restaurant_ratings.items()):
        print "%s is rated at %s." % (name, rating)

print_ratings(filename)
