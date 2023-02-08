#!/usr/bin/env python3
from elem import Elem, Text


class Html(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='html', attr=attr, content=content)


class Head(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='head', attr=attr, content=content)


class Body(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='body', attr=attr, content=content)


class Title(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='title', attr=attr, content=content)


class Meta(Elem):
    def __init__(self, attr={}):
        super().__init__(tag='meta', attr=attr, tag_type='simple')


class Img(Elem):
    def __init__(self, attr={}):
        super().__init__(tag='img', attr=attr, tag_type='simple')


class Table(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='table', attr=attr, content=content)


class Th(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='th', attr=attr, content=content)


class Tr(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='tr', attr=attr, content=content)


class Td(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='td', attr=attr, content=content)


class Ul(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='ul', attr=attr, content=content)


class Ol(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='ol', attr=attr, content=content)


class Li(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='li', attr=attr, content=content)


class H1(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='h1', attr=attr, content=content)


class H2(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='h2', attr=attr, content=content)


class P(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='p', attr=attr, content=content)


class Div(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(attr=attr, content=content)


class Span(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='span', attr=attr, content=content)


class Hr(Elem):
    def __init__(self, attr={}):
        super().__init__(tag='hr', attr=attr, tag_type='simple')


class Br(Elem):
    def __init__(self, attr={}):
        super().__init__(tag='br', attr=attr, tag_type='simple')


# Classe adicional para estilo CSS
class Style(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='style', attr=attr, content=content)


if __name__ == '__main__':

    print(
        Html(attr={'lang': 'en'}, content=[
            Head([
                Meta(attr={'charset': 'UTF-8'}),
                Meta(attr={'http-equiv': 'X-UA-Compatible',
                     'content': 'IE=edge'}),
                Meta(attr={'name': 'viewport',
                     'content': 'width=device-width, initial-scale=1.0'}),
                Title(Text("Meu primeiro CV na 42 :)")),
                Style(
                    Text('table, th, td {border: 1px solid gold; border-collapse: collapse;}'))
            ]),
            Body([
                Div([
                    H1(Text("CV: Ricardo Baddini Kannebley")),
                    H2(Text("27 anos - São Paulo - SP")),
                    Img(attr={'src': 'http://i.imgur.com/pfp3T.jpg'}),
                    Table([
                        Tr([
                            Th(Text("Telefone")),
                            Th(Text("E-mail")),
                            Th(Text("Github"))
                        ]),
                        Tr([
                            Td(Text("(13) 99111-4201")),
                            Td(Text("ricardo.kannebley@gmail.com")),
                            Td(Text("https://github.com/RickBadKan"),
                               attr={'style': "border-color: #424242; border-width: 2px"})
                        ])
                    ]),
                ]),
                Hr(),
                Div([
                    P(Span(Text("Skills"))),
                    Ul([
                        Li(Text("Python")),
                        Li(Text("AWS")),
                        Li(Text("DevOps"))
                    ]),
                    Br()
                ]),
                Div([
                    P(Span(Text("Career Path"))),
                    Ol([
                        Li(Text("IMT: Communications Director")),
                        Li(Text("Logicalis: Pre sales Engineer")),
                        Li(Text("Itaú: DevOps Engineer"))
                    ])
                ])
            ])
        ])
    )

    print(Html([
        Head(
            Title(Text("'Hello ground!'"))
        ),
        Body([
            H1(
                Text("'Oh no, not again!'")
            ),
            Img(attr={'src': 'http://i.imgur.com/pfp3T.jpg'})
        ])
    ]))
