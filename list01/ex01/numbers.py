#!/usr/bin/env python3

def my_numbers():
    with open("numbers.txt") as my_file:
        print(my_file.read().replace(',', "\n"))


if __name__ == '__main__':
    my_numbers()
