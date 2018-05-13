

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
    groups = {
        'A': [3, 130],
        'B': [2, 45],
    }
    basket = {
        'A': 0,
        'B': 0,
        'C': 0,
        'D': 0,
    }
    cost = 0
    for product in skus:
        if product in price_catalogue.keys():
            basket[product] += 1
        else:
            return -1
    for product, quantity in basket.iteritems():
        if product in groups.keys():
            cost += price_catalogue[product] * quantity
        else:
            cost += price_catalogue[product] * quantity
    return cost
