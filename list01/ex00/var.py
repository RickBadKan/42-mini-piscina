#!/usr/bin/env python3

def my_var():
    inteiro = int(42)
    texto = str("42")
    frances = str("quarante-deux")
    flutuante = float(42.0)
    booleano = True
    lista = [42]
    dicionario = {42: 42}
    tupla = (42,)
    conjunto = set()

    print(str(inteiro) + " has a type " + str(type(inteiro)))
    print(str(texto) + " has a type " + str(type(texto)))
    print(str(frances) + " has a type " + str(type(frances)))
    print(str(flutuante) + " has a type " + str(type(flutuante)))
    print(str(booleano) + " has a type " + str(type(booleano)))
    print(str(lista) + " has a type " + str(type(lista)))
    print(str(dicionario) + " has a type " + str(type(dicionario)))
    print(str(tupla) + " has a type " + str(type(tupla)))
    print(str(conjunto) + " has a type " + str(type(conjunto)))


if __name__ == '__main__':
    my_var()
