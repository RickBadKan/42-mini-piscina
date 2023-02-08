#!/usr/bin/env python3
import requests
import sys
from bs4 import BeautifulSoup


class WrongNumberOfArgsError(Exception):
    pass


class InfiniteLoopError(Exception):
    pass


def to_snake_case(string):
    return string \
            .replace(',', '_') \
            .replace('.', '_') \
            .replace(' ', '_') \
            .replace('-', '_') \


def roads_to_philosophy(url, previous):
    try:
        data = requests.get(url)

        data.raise_for_status()

        road = BeautifulSoup(data.text, 'html.parser')

        title = road.find(id='firstHeading').text

        if title in previous:
            raise InfiniteLoopError
        
        previous.append(title)

        print(title)

        if title == 'Philosophy':
            return print(f"{len(previous)} roads from {previous[0]} to Philosophy")

        content = road.find(id='mw-content-text')

        allLinks = content.select('p > a')

        for link in allLinks:
            if (link.get('href') is not None) \
                    and \
                (link['href'].startswith('/wiki/')) \
                    and \
                (not link['href'].startswith('/wiki/Wikipedia:')) \
                    and \
                (not link['href'].startswith('/wiki/Help:')):
                
                return roads_to_philosophy('https://en.wikipedia.org' + link['href'], previous)

        return print("It leads to a dead end !")

    except requests.HTTPError as e:
        if (data.status_code == 404):
            return print("It leads to a dead end !")

    except InfiniteLoopError:
        return print("It leads to an infinite loop !")

    except Exception as e:
        return print(f'An exception occurred: {e}')


def orquestrator():
    try:
        if len(sys.argv) != 2:
            raise WrongNumberOfArgsError

        previous = []

        query = to_snake_case(sys.argv[1].strip())
        
        url = f'https://en.wikipedia.org/wiki/{query}'

        roads_to_philosophy(url, previous)


    except WrongNumberOfArgsError:
        return print('Wrong number of args!')


if __name__ == '__main__':
    orquestrator()