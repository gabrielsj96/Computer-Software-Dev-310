import mysql.connector
from mysql.connector import errorcode


def show_films(cursor, title):
    # method to execute an inner join on all tables,
    # iterate over the dataset and output the results to the terminal window.

    # inner join query
    cursor.execute(
        "select film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' from film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id"
    )

    # get the results from the cursor object
    films = cursor.fetchall()

    print("\n -- {} --".format(title))

    # iterate over the film data set and display the results
    for film in films:
        print(
            "Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(
                film[0], film[1], film[2], film[3]
            )
        )


config = {
    "user": "root",
    "password": "Karamazov@1618",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True,
}

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    show_films(cursor, "DISPLAYING FILMS")

    cursor.execute(
        "INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) VALUES ('The Lorax', '2012', 95, 'Chris Renaud', 3, 3)"
    )

    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

    cursor.execute("UPDATE film SET genre_id = 1 WHERE film_id = 2")

    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE")

    cursor.execute("DELETE FROM film WHERE film_name = 'Gladiator'")

    show_films(cursor, "DISPLAYING FILMS AFTER DELETION")

    print(
        "\n\n Database user {} connected to MySQL on host {} with database {}".format(
            config["user"], config["host"], config["database"]
        )
    )
    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)

finally:
    db.close()
