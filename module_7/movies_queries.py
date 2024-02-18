import mysql.connector
from mysql.connector import errorcode

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
    print(
        "\n\n Database user {} connected to MySQL on host {} with database {}".format(
            config["user"], config["host"], config["database"]
        )
    )

    print("-- DISPLAYING Studio RECORDS --")

    cursor.execute("SELECT studio_id, studio_name FROM studio")
    studios = cursor.fetchall()
    for studio in studios:
        print("Studio ID: {}\nStudio Name: {}\n".format(studio[0], studio[1]))

    print("-- DISPLAYING Genre RECORDS --")

    cursor.execute("SELECT genre_id, genre_name FROM genre")
    genres = cursor.fetchall()
    for genre in genres:
        print("Genre ID: {}\nGenre Name: {}\n".format(genre[0], genre[1]))

    print("-- DISPLAYING Short Film RECORDS --")

    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
    short_films = cursor.fetchall()
    for short_film in short_films:
        print("Film Name: {}\nRuntime: {}\n".format(short_film[0], short_film[1]))

    print("-- DISPLAYING Director RECORDS in Order --")

    cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")
    films_and_directors = cursor.fetchall()
    for film_and_director in films_and_directors:
        print(
            "Film Name: {}\nfilm_director {}\n".format(
                film_and_director[0], film_and_director[1]
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
