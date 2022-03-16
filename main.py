# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def get_password_strenth():
    chars = input("How many characters does your password have?")
    # eg 0-9 is 10 values; a-z is 26 more etc
    possible_values = input("how many different values can each character have ")
    strength = pow(int(chars), int(possible_values))
    print(f"it will take at most {strength} guesses for a computer to break your password")
    # Use a breakpoint in the code line below to debug your script.


get_password_strenth()