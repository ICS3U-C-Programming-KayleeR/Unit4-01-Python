#!/usr/bin/env python3
# Created By: Kaylee R
# Date: 05, 11, 2026
# This program


def main():
    # set a sum variable that hold the sum of all the numbers
    total = 0

    # set a counter
    counter = 0

    # get user's int input
    user_num = input("Enter a positive integer: ")

    # try to cast the input to an int
    try:
        user_int = int(user_num)

        if user_int < 0:
            print("Integer can not be a negative")

        else:
            while user_int >= counter:
                print("Tracking {} times through the loop".format(counter))
                total = total + counter
                counter = counter + 1

            print("The sum of the numbers from 0-{} is {}".format(user_int, total))

    except ValueError:
        print("{} is not a valid integer".format(user_num))


if __name__ == "__main__":
    main()
