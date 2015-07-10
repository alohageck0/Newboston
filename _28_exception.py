__author__ = 'royalfiish'

while True:
    try:
        number = int(input("Enter a number "))
        print(20 / number)
        break
    except ValueError:
        print("Not a number!")
    except ZeroDivisionError:
        print("Can not be a zero")
    finally:
        print("Done!")
