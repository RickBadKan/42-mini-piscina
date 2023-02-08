#!/usr/bin/env python3

from antigravity import geohash
import sys

class WrongNumberOfArgs(Exception):
    "Raised when the number of arguments is different than 3"
    pass

def main():
    try:
        if len(sys.argv) != 4:
            raise WrongNumberOfArgs
        
        lat = float(sys.argv[1])
        long = float(sys.argv[2])
        datedow = bytes(sys.argv[3], encoding='utf-8')

        geohash(lat, long, datedow)

    except ValueError:
        print("Some arguments are not well formatted!")
    except WrongNumberOfArgs:
        print("Wrong number of args! Expected Latitude, Longitude and Date-Dow")
    except Exception as e:
        print(f"An exception occurred: {e}")



if __name__ == '__main__':
    '''Compute geohash() using the Munroe algorithm.
        >>> geohash(37.421542, -122.085589, b'2005-05-26-10458.68')
        37.857713 -122.544543
    '''
    main()