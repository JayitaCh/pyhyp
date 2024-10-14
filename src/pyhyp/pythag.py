import numpy as np

# Module to calculate the longest side of a right-angled 
# triangle using Pythogora's theorem.

#Function to check input is float/int
#throw error if not

# Function to add two numbers together
# inputs: float or int or list/ array of float or int

# Generate Docstring added in devcontainer.json to automatically get func description
def add_nums(a,b):
    """Adds two different numbers

    Args:
        a (float, int, array): a number/list of numbers
        b (float, int, array): a number/list of numbers

    Returns:
        float/int/array: Addition of a and b
    """
    sum = a+b
    return sum

# Function to calculate the square of the number
# inputs: float or int or list/ array of float or int
def square_num(a):
    """Returns the square of a number

    Args:
        a (float,int,array): A number/ list of numbers

    Returns:
        float, int, array: squared
    """
    sq_num = a**2
    return sq_num

# Function to calculate the square root of the number
def square_root(a):
    sq_rt = np.sqrt(a)
    return sq_rt

# Function to calculate the hypotenuse using the following equation
# a^2 + b^2= c^2
# c = sqrt(a^2 + b^2)
# inputs: float or int or list/ array of float or int
def calc_hyp(opposite,adjacent):
    """Calculates the hypotenuse for a rt-angled triangle

    Args:
        opposite (float, int, array): A number /list of numbers
        adjacent (float, int, array): A number /list of numbers

    Returns:
        hypotenuse (float, int, array): A number /list of numbers
    """
    sq_opp = square_num(opposite)
    sq_adj = square_num(adjacent)
    
    sum = add_nums(sq_opp,sq_adj)
    
    hypotenuse = square_root(sum)
    
    return hypotenuse
    