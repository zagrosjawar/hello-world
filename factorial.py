def factorial(n):
    """
    Calculate the factorial of a number using recursion.
    
    Args:
        n (int): The number to calculate the factorial of.
        
    Returns:
        int: The factorial of the given number.
    """
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    
    # Recursive case: factorial of n is n multiplied by factorial of (n-1)
    return n * factorial(n - 1)


result = factorial(5)
print(result)  # Output: 120



def double(n):
    return n*n



def git():
    print("git init, git clone, git add, git commit, git status, git branch, git merge, git pull, git push")


