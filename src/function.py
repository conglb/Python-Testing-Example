
def gcd(x, y):
    """
    Greatest common division
    :param x: first number
    :param y: second number
    :return: gcd of two integer x and y
    """
    if type(x) != int or type(y) != int: raise TypeError("Parameters is not int type")
    if x < 0 or y < 0: return gcd(abs(x) , abs(y))
    if x > y: return gcd(y, x)
    if x == 0: return y
    return gcd(y % x, x)