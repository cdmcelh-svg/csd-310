import mysql.connector

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

db = mysql.connector.connect(**config)

cursor = db.cursor()


def show_films(cursor, title):

    cursor.execute("""
        SELECT
            film_name AS Name,
            film_director AS Director,
            genre_name AS Genre,
            studio_name AS Studio
        FROM film
        INNER JOIN genre
            ON film.genre_id = genre.genre_id
        INNER JOIN studio
            ON film.studio_id = studio.studio_id
    """)

    films = cursor.fetchall()

    print("\n -- {} --".format(title))

    for film in films:
        print("Film Name: {}".format(film[0]))
        print("Director: {}".format(film[1]))
        print("Genre Name ID: {}".format(film[2]))
        print("Studio Name: {}\n".format(film[3]))


show_films(cursor, "DISPLAYING FILMS")


cursor.execute("""
INSERT INTO film
(film_name, film_releaseDate, film_runtime,
film_director, studio_id, genre_id)
VALUES
('The Matrix', '1999', 136,
'Lana and Lilly Wachowski', 1, 2)
""")

db.commit()

show_films(cursor, "DISPLAYING FILMS AFTER INSERT")


cursor.execute("""
UPDATE film
SET genre_id = 1
WHERE film_name = 'Alien'
""")

db.commit()

show_films(cursor, "DISPLAYING FILMS AFTER UPDATE")


cursor.execute("""
DELETE FROM film
WHERE film_name = 'Gladiator'
""")

db.commit()

show_films(cursor, "DISPLAYING FILMS AFTER DELETE")


cursor.close()
db.close()