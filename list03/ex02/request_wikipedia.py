import requests
import sys
from dewiki.parser import Parser

class InformationNotFoundError(Exception):
    pass

class WrongNumberOfArgsError(Exception):
    pass

def to_snake_case(string):
    return string \
            .replace(',', '_') \
            .replace('.', '_') \
            .replace(' ', '_') \
            .replace('(', '_') \
            .replace(')', '_') \
            .replace('{', '_') \
            .replace('}', '_') \
            .replace('-', '_') \
            + ".wiki"

def ex02():
    try:
        if len(sys.argv) != 2:
            raise WrongNumberOfArgsError

        query = sys.argv[1].strip()
    
        url = 'https://en.wikipedia.org/w/api.php'
        params = {
                    'action':'query',
                    'format':'json',
                    'list':'search',
                    'utf8':1,
                    'srsearch':query
                }
        
        data = requests.get(url, params=params).json()

        if data['query']['searchinfo']['totalhits'] == 0 and 'suggestion' not in data['query']['searchinfo']:
            raise InformationNotFoundError

        if data['query']['searchinfo']['totalhits'] == 0 and 'suggestion' in data['query']['searchinfo']:
            params['srsearch'] = data['query']['searchinfo']['suggestion']
            data = requests.get(url, params=params).json()


        params = {
                    'action': 'parse',
                    'pageid': data['query']['search'][0]['pageid'],
                    'format': 'json',
                    'prop':'wikitext',
                    'redirects':'true',
                }
        
        data = requests.get(url, params=params).json()

        text_to_write = str(Parser().parse_string(string=data['parse']['wikitext']['*']))

        with open(to_snake_case(query), 'w') as wiki:
            wiki.write(text_to_write)

    except InformationNotFoundError:
        print('No results or suggestions for your search.')

    except WrongNumberOfArgsError:
        print('Wrong number of args!')

    except Exception as e:
        print(f'An exception occurred: {e}')

if __name__ == '__main__':
    ex02()