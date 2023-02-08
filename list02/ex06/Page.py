#!/usr/bin/env python3
from elem import *
from elements import *


class Page():
    def __init__(self, html_element: Elem()):
        if not isinstance(html_element, Elem):
            raise Elem.ValidationError()

        self.html_element = html_element

    def __str__(self):
    # Display its HTML code when we print an instance. Beware: the HTML code displays
    # must be preceded by a doctype if and if only the root element type is Html
        if isinstance(self.html_element, Html):
            return f"<!DOCTYPE html>\n{str(self.html_element)}"
        
        return str(self.html_element)


    def write_to_file(self, file_name):
    # Write your HTML code in a file thanks to a write_to_file method that takes the
    # file's name as a parameter. Beware: HTML code written in the file must be preceded
    # by a doctype if and if only the root element's type is Html.
        if not file_name or file_name == '.':
            file_name = "index.html"
        
        if len(file_name.split('.')) < 2:
            file_name += ".html"
        try:
            with open(file_name, 'w+') as file:
                file.write(str(self))

        except Exception as e:
            print(f'File error: {e}')
        

    def is_valid(self):
    # If, on the tree path, a node has not one of the following types:
    # html, head, body, title, meta, img, table, th, tr, td, ul, ol, li, h1, h2, p, div, span, hr, br, Text
        valid_types = (Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li, H1, H2, Div, Span, Hr, Br, Text)

        # def flatten(S):
        #     if S == []:
        #         return S
        #     if isinstance(S[0], list):
        #         return flatten(S[0]) + flatten(S[1:])
        #     return S[:1] + flatten(S[1:])

        # list = flatten(self.html_element.content)
        
        # print(self.html_element.content)
        # print("------------------------------------")
        # print(list)


        # for element in self.html_element.content:
        #     if not isinstance(element, valid_types) or not isinstance(self.html_element, valid_types):
        #         return False
        
        # return True

        

if __name__ == '__main__':
    def flatten(S):
        if S == []:
            return S
        if isinstance(S[0], Elem):
            if isinstance(S[0].content, list):
                return flatten(S[0].content) + flatten(S[1:])
        if isinstance(S[0], list):
            return flatten(S[0]) + flatten(S[1:])
        return S[:1] + flatten(S[1:])

    # def flatten(S):
    #     if S == []:
    #         return S
    #     if isinstance(S[0], list):
    #         return flatten(S[0]) + flatten(S[1:])
    #     return S[:1] + flatten(S[1:])

    teste = Page(Html([Head(),Body(P())]))
    

    list = flatten(teste.html_element.content)
    
    print(teste.html_element.content)
    print("------------------------------------")
    print(list)
