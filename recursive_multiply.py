
def multiply(int x, int y):

    #Check if either integer is 0
    if (x == 0 || y == 0):
        return 0
        
    #Break input down into pieces    
    int x_Rem = x % 10
    int y_Rem = y % 10

    int x10 = x / 10
    int y10 = y /10

    bool x_digit = (x_Rem == 0)
    bool y_digit = (y_Rem == 0)

    #Base case
    if (x_digit && y_digit):
        return (x * y)

    if (x_digit):
        return ((multiply(x, y10) * 10) + multiply(x, y % 10))

    if (y_digit):
        return ((multiply(x10, y) * 10) + multiply(x % 10, y))

    return ((multiply(x, y10) * 10) + multiply(x, y % 10)
