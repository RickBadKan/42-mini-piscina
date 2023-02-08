#!/usr/bin/env python3
import sys
import os
import re


class WrongNumberOfArgs(Exception):
    "Raised when the number of arguments is different than 2"
    pass


class IncorrectSettingsFile(Exception):
    "Raised when the settings file is not correctly formated"
    pass


class WrongFileExtension(Exception):
    "Raised when the template file passed as argument is not a '.template' file"
    pass


def load_file(file_name):
    try:
        full_path = os.getcwd() + '/' + file_name

        with open(full_path) as file:
            return file.read()

    except Exception:
        raise FileNotFoundError


if __name__ == '__main__':
    # Your tests and your error handling

    # You will have to turn-in a myCV.template file which, once converted in HTML, will
    # have to include at least the complete structure of a (doctype, head and body page, the
    # page’s title, name and surname of the resume’s owner, their age and profession. Of course,
    # these informations will not directly appear in the .template file.
    try:
        if len(sys.argv) != 2:
            raise WrongNumberOfArgs

        if not re.search("[\w]+\.template", sys.argv[1]):
            raise WrongFileExtension

        template = load_file(sys.argv[1])

        settings_raw = [item for item in
                        load_file("settings.py").split("\n")
                        if item]

        settings = {}

        for config in settings_raw:
            if not re.search("^\s*[\w]+\s*=\s*.+$", config):
                raise IncorrectSettingsFile

            key_value = config.split("=")

            if not key_value:
                raise IncorrectSettingsFile

            settings[key_value[0].strip()] = \
                key_value[1].strip().strip('"').strip("'")

        formated_template = template.format(**settings)

        with open(sys.argv[1].split('.')[0] + ".html", 'w+') as web_page:
            web_page.write(formated_template)

    except FileNotFoundError:
        print("Incorrect file name!")
    except KeyError:
        print("There are more variables on the .template file than in the settings.py!")
    except IncorrectSettingsFile:
        print("Your settings.py file is not correcty formated!")
    except WrongNumberOfArgs:
        print("Wrong number of args!")
    except WrongFileExtension:
        print("The input file is not a '.template'!")
    except Exception as e:
        print('An exception has occurred: {}'.format(e))
