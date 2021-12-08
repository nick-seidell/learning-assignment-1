# Method for multiplying large numbers recursively
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

    # Base case, if both x and y are single digit numbers, return the product
    if (x_digit && y_digit):
        return (x * y)

    # If x is a single digit, recursive call to multiply x and components of y
    if (x_digit):
        return ((multiply(x, y10) * 10) + multiply(x, y % 10))

    # If y is a single digit, recursive call to multiply y and components of x
    if (y_digit):
        return ((multiply(x10, y) * 10) + multiply(x % 10, y))

    return ((multiply(x, y10) * 10) + multiply(x, y % 10)
