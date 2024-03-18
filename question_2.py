# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8 
# Then, the output should be: 40320

# n! = n * (n-1) * (n-2) * (n-3) * ... * 4 * 3 * 2 * 1

# def n_factorial(n):
#     if n != 1:
#         n_fac = n * (n-1)
#         n = n-1
#     else:
#         pass

# print(n_factorial(8))

# i didn't handle the base case (when n = 1 or n = 0)

def n_factorial(n):
    if n == 1 or n == 0:
        return 1
    else: 
        # calling the function for n-1 will loop n-1 through the if/else statment until n = 1
        return n * n_factorial(n-1)
        

print(n_factorial(8))