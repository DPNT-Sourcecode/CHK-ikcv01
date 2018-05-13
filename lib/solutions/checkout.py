

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
    try: # let's see if the string format guess was correct
        products = skus.split(',') # split products
        for p in products: # split the quantities
            name, quantity = p.split('*')
            basket.append([name, int(quantity)])
        return basket
    except:
        return -1
