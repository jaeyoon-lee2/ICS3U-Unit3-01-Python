#!/user/bin/env python3

# Created by: Jaeyoon
# Created on: Sept 2019
# This program calculates the sum of 2 integers
#     with user input

def main():
    # This function calculates the sum of 2 integers

    # input
    int1 = int(input("Enter the first number: "))
    int2 = int(input("Enter the second number: "))

    # process
    sum_number = int1 + int2
    
    # output
    print("")
    print("{0} + {1} = {2}"
          .format(int1, int2, sum_number))


if __name__ == "__main__":
    main()
