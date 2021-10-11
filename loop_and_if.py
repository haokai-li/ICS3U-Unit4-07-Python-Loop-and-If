#!/usr/bin/env python3

# Created by: Haokai Li
# Created on: Oct 2021
# This Program is about loop and if


def main():
    # This function is about loop and if
    loop_number = 0

    # process
    for loop_number in range(1000, 2001):
        if (loop_number + 1) % 5 == 0:
            # output
            print("{} ".format(loop_number))
        else:
            # output
            print("{} ".format(loop_number), end="")


if __name__ == "__main__":
    main()
