# toolbox.py

def double(number):
    """Returns double the given number."""
    return number * 2


def is_pass(score):
    """Returns True if the score is 50 or higher, otherwise False."""
    return score >= 50


def greet(name, greeting="Hello"):
    """Returns a greeting string formatted as 'Greeting, Name!'."""
    return f"{greeting}, {name}!"


# Testing the functions
if __name__ == "__main__":
    print(double(7))
    print(double(10))
    print(is_pass(80))
    print(is_pass(20))
    print(greet("Amina"))
    print(greet("Brian", "Habari"))