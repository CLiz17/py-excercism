def triangle(sides):
    """
    To check if the given sides can form a triangle.
    
    :param sides: list or tuple of three positive numbers.
    :return: bool - True if the sides can form a triangle, False otherwise.
    """
    a, b, c = sides
    return a > 0 and b > 0 and c > 0 and a + b >= c and b + c >= a and a + c >= b

def equilateral(sides):
    if triangle(sides):
        return sides[0] == sides[1] == sides[2]
    return False

def isosceles(sides):
    if triangle(sides):
        return sides[0] == sides[1] or sides[1] == sides[2] or sides[2] == sides[0]
    return False

def scalene(sides):
    if triangle(sides):
        return sides[0] != sides[1] and sides[1] != sides[2] and sides[2] != sides[0]
    return False