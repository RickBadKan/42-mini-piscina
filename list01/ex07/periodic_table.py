#!/usr/bin/env python3
import sys


def escreve_elemento(writer, nome_elemento, atributo):
    writer.write('''
        <tr>
            <td style="border: 1px solid black; padding:10px">
                <h4>{}</h4>
                <ul>
                    <li>{}</li>
                    <li>{}</li>
                    <li>{}</li>
                <ul>
            </td>
        </tr>'''.format(nome_elemento,
                        atributo["number"],
                        atributo["small"],
                        atributo["molar"]))


def ex07():
    with open('periodic_table.html', 'w+') as writer:
        with open('periodic_table.txt') as reader:
            writer.write('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My periodic table!</title>
</head>
<body>
    <h1>The Periodic Table of Elements!</h1>
    <table>''')

            linhas = reader.read().split("\n")

            # Remove o último elemento da lista, que é uma linha vazia.
            linhas.remove('')

            for linha in linhas:
                elemento_completo = linha.split(" = ")
                nome_elemento = elemento_completo[0].strip()

                atributo = {}

                for atributo_texto in elemento_completo[1].split(", "):
                    chave, valor = atributo_texto.split(":")
                    atributo[chave] = valor.strip()

                escreve_elemento(writer, nome_elemento, atributo)

            writer.write('''
    </table>
</body>
</html>''')


if __name__ == '__main__':
    ex07()
