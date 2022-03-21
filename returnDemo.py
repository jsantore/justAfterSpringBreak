import math

def square(x):
    return x*x

def distance2(p1, p2):
    x_val = square(p2.getX() - p1.getX())
    y_val = square(p2.getY() - p1.getY())
    dist = math.sqrt(x_val+ y_val)
    return dist
    print("We will never get here")
    
def main():
    my_dist = distance2((0,3), (3,4))