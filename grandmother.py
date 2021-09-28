#!/usr/bin/env python3

# Created by: Mikayla Barthelette
# Created on: Sept 2021
# This program will tell you if you can date grandma's grandchild


def main():
    # this function determines if you can date her grandchild

    # input
    user_input = input("Please enter your age: ")

    # process & output
    try:
        user_age = int(user_input)
        if user_age >= 25 and user_age <= 40:
            print("You are accepted to date my grandchild.")
        else:
            print("You are not the right age.")
    except Exception:
        print("{0} is not valid input.".format(user_input))
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
