import math


def f(x) -> float:
    """
    Calculates the value of function at given x
    """
    return math.cos(27/64) + 2*math.pi - 70*math.e*13/((x-8)*(x+6)) + 14*math.sin(x-3) - math.log10(x+7)


def _print_function(x):
    """
    Print "done" and print x in a fixed point format,
8 characters after the period
    """
    print(" done")
    print(f'for x = {x: .8f}')


def _print_wrong_input():
    """
    Print from a new line "wrong input"
    """
    print("\nwrong input")


def _calculate_and_check_x(x):
    """
    Check x in domain, calculate it and print result
    """
    if x > -7 and x != -6 and x != 8:
        result = f(x)
        _print_function(x)
        print(f'result = {result: .8f}')
    else:
        _print_function(x)
        print("result = undefined")


def main():
    """
    Calculates entered float x and print result
    """
    try:
        x = float(input("Enter x: "))
        print("\n****** do calculations ...", end="")
        _calculate_and_check_x(x)

    except ValueError:
        _print_wrong_input()
    except KeyboardInterrupt:
        print("\nprogram aborted")
    except EOFError:
        _print_wrong_input()
    except IOError:
        _print_wrong_input()


print("The author of this program is Kormanovska Anastasia")
print("This program calculates the value of the expression by given x.Variant 74.")


main()
