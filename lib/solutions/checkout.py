

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    """
    I am assuming products are sepereted by commas
    and their quantity follows as an int sperated with an asterisk
    e.g. skus="A*3,B*1"
    the server tests will reveal the input string's format after the penalty
    I also have no information on the offers for multiple items
    """
    price_catalogue = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
    }
    cost = 0
    if type(skus) != type([]):
        return -1
    try: # let's see if the string format guess was correct
        for product in skus:
            if product in price_catalogue.keys():
                cost += price_catalogue[product]
        return cost
    except:
        return -1
