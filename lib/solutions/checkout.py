

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
        'E': 40
    }
    basket = {
        'A': 0,
        'B': 0,
        'C': 0,
        'D': 0,
        'E': 0,
    }
    cost = 0

    for product in skus:
        if product in price_catalogue.keys():
            basket[product] += 1
        else:
            return -1

    offered = basket['E'] / 2 # python 2 integer division
    if basket['B'] >= offered:
        basket['B'] -= offered
    else:
        basket['B'] = 0

    for product, quantity in basket.iteritems():
        if product == 'A':
            if quantity >= 5:
                remainder = quantity % 5
                discounted = quantity / 5
                cost += discounted * 200
            remainder = quantity % 3
            discounted = quantity / 3
            cost += discounted * 130 + remainder * 50
        elif product == 'B':
            remainder = quantity % 2
            discounted = quantity / 2
            cost += discounted * 45 + remainder * 30
        else:
            cost += basket[product] * price_catalogue[product]

    return cost
