import sys

filename = sys.argv[1]


def print_ratings(filename):
    """Processes a file of restaurants and their ratings.

    Takes a filename argument on the command line and iterates over it to read
    restaurant scores. Returns output in full sentence form. Text file with
    scores must be called on the command line in argv[1] position.

    >>> print_ratings("scores.txt")
    Andalu is rated at 3.
    Arinell's is rated at 4.
    Bay Blend Coffee and Tea is rated at 3.
    Casa Thai is rated at 2.
    Charanga is rated at 3.
    El Toro is rated at 5.
    Giordano Bros is rated at 2.
    Irma's Pampanga is rated at 5.
    Little Baobab is rated at 1.
    Pancho Villa is rated at 3.
    Taqueria Cancun is rated at 2.
    Urbun Burger is rated at 1.
    """
    restaurant_ratings = {}
    with open(filename) as rest_scores:
        for line in rest_scores:
            name, rating = line.strip().split(":")
            restaurant_ratings[name] = rating

    for name, rating in sorted(restaurant_ratings.items()):
        print "%s is rated at %s." % (name, rating)

print_ratings(filename)

###

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
