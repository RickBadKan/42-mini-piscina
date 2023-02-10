from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import psycopg2

# Create your views here.
def init(request):
    try:
        conn = psycopg2.connect(
        database = 'djangotraining',
        host = 'localhost',
        user = 'djangouser',
        password = 'secret'
        )

        curr = conn.cursor()

        curr.execute(''' CREATE TABLE IF NOT EXISTS ex02_movies (
            title varchar(64) UNIQUE NOT NULL,
            episode_nb int PRIMARY KEY,
            opening_crawl text,
            director varchar(32) NOT NULL,
            producer varchar(128) NOT NULL,
            release_date date NOT NULL
            )
            ''')

        conn.commit()
        conn.close()
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(e)

def _make_insert(movie):
    return f'''INSERT INTO ex02_movies (episode_nb, title, director, producer, release_date)
        VALUES
        ({movie[0]}, '{movie[1]}', '{movie[2]}', '{movie[3]}', '{movie[4]}')
    '''

def populate(request):
    try:
        conn = psycopg2.connect(
        database = 'djangotraining',
        host = 'localhost',
        user = 'djangouser',
        password = 'secret'
        )

        curr = conn.cursor()

        inserts = {}
        inserts['OK'] = []
        inserts['NOK'] = []
        movies = [
            (1, 'The Phantom Menace', 'George Lucas', 'Rick McCallum', '1999-05-19'),
            (2, 'Attack of the Clones', 'George Lucas', 'Rick McCallum', '2002-05-16'),
            (3, 'Revenge of the Sith', 'George Lucas', 'Rick McCallum', '2005-05-19'),
            (4, 'A New Hope', 'George Lucas', 'Gary Kurtz, Rick McCallum', '1977-05-25'),
            (5, 'The Empire Strikes Back', 'Irvin Kershner', 'Gary Kurtz, Rick McCallum', '1980-05-17'),
            (6, 'Return of the Jedi', 'Richard Marquand', 'Howard G. Kazanjian, George Lucas, Rick McCallum', '1983-05-25'),
            (7, 'The Force Awakens', 'J. J. Abrams', 'Kathleen Kennedy, J. J. Abrams, Bryan Burk', '2015-12-11')
        ]

        for movie in movies:
            try:
                curr.execute(_make_insert(movie))
                conn.commit()
                inserts['OK'].append(movie[1])
            except Exception as e:
                inserts['NOK'].append(f"{movie[1]}: error {e}")

        conn.close()

        return render(request, 'ex02/index.html', {'inserts_ok': inserts['OK'], 'inserts_nok': inserts['NOK']})

    except Exception as e:
        return HttpResponse(e)

def display(request):
    pass