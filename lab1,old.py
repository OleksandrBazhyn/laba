import math

print("The author of this program is Kormanovska Anastasia")
print("This program calculates the value of the expression by given x.Variant 74.")


def f(x) -> float:
    return math.cos(27/64) + 2*math.pi - 70*math.e*13/((x-8)*(x+6)) + 14*math.sin(x-3) - math.log10(x+7)


def calculation():
    try:
        x = float(input("Enter x: "))
        print("\n****** do calculations ...", end="")
        if x > -7 and x != -6 and x != 8:
            result = f(x)
            print(" done")
            print(f'for x = {x: .8f}')
            print(f'result = {result: .8f}')
        else:
            print("done")
            print(f'for x = {x: .8f}')
            print("result = undefined")

    except ValueError:
        print("\nwrong input")
    except KeyboardInterrupt:
        print("\nprogram aborted")
    except ZeroDivisionError:
        print("\nwrong input")


calculation()