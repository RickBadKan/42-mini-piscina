#!/usr/bin/env python3
import sys


def ex05():
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

    capital_states = {v: k for k, v in states_capital.items()}

    if len(sys.argv) != 2:
        return

    entrada = sys.argv[1].split(',')

    saida = ""

    for registro in entrada:
        registro_alterado = registro.strip().title()
        if registro_alterado == "":
            continue

        if registro_alterado in states_capital:
            saida = saida + states_capital[registro_alterado] + \
                " is the capital of " + registro_alterado + "\n"

        elif registro_alterado in capital_states:
            saida = saida + registro_alterado + " is the capital of " + \
                capital_states[registro_alterado] + "\n"

        else:
            saida = saida + registro.strip() + " is neither a capital city nor a state\n"

    if not saida:
        return

    print(saida.strip())


if __name__ == '__main__':
    ex05()
