"""
This program calculates the value of the series by given x and eps
"""
A = -1
B = 1


def s(x: float, eps: float) -> float:
    """
    Calculate the value of the series by given x and eps
    """
    n = 2
    d = (x * x * x)/6
    result = d
    while d >= eps or d <= -eps:
        d *= x * (n/((n + 2)*(n - 1)))
        result += d
        n += 1
    else:
        return result


def _print_function(x, eps):
    """
    Print "done", print x and eps, 5 and 4 characters after the period accordingly
    """
    print(" done")
    print(f"for x ={x: .5f}")
    print(f"for eps ={eps: .4E}")


def _print_error():
    """
    Print from a new line "***** error"
    """
    print("\n***** error")


def _main_function(x):
    """
    Receive eps and check eps in domain, calculate s and print result
    """
    eps = float(input("Enter positive eps > 0: "))
    if eps > 0:
        print("\n***** do calculations ...", end="")
        result = s(x, eps)
        _print_function(x, eps)
        print(f"result ={result: .9f}")
    else:
        print("\n***** error")
        print("(Incorrect value of eps)")


def _input_function():
    """
    Check x in domain
    """
    x = float(input(f"Enter a real from [{A}, {B}]: "))
    if A <= x <= B:
        _main_function(x)
    else:
        _print_error()
        print("(Incorrect entered value of x, it is not in domain)")


def _check_exception():
    """
    if something is wrong with value of given x or eps print exception
    """
    try:
        _input_function()
    except ValueError:
        _print_error()
        print("ValueError(There are no input or it could not be converted to float)")
    except KeyboardInterrupt:
        print("\nprogram aborted")
    except EOFError:
        _print_error()
        print("EOFError(There are no input or it could not be converted to float)")
    except IOError:
        _print_error()


print("The author of this program is Kormanovska Anastasia")
print("This program calculates the value of the series ....... Variant 74.")

_check_exception()
