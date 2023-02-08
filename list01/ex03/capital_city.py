#!/usr/bin/env python3
import sys


def capital():
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }

    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    states_capital = {}

    for state_full_name in states:
        if capital_cities[states[state_full_name]]:
            states_capital[state_full_name] = capital_cities[states[state_full_name]]

    if len(sys.argv) != 2:
        return

    if sys.argv[1] in states_capital:
        return print(states_capital[sys.argv[1]])

    return print("Unknown state")


if __name__ == '__main__':
    capital()
