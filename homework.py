from pymongo import MongoClient

client = MongoClient()
db = client.test


def createMovie():
    title = str(input("Enter movie title"))
    genre = str(input("Enter movie genre"))
    year = int(str(input("Enter movie year")))
    movie = {
        "title" : title,
        "genre" : genre, 
        "year" : int(year)
    }
    return movie


def retrieveMovies():
    movies = db.movies
    movies.insert_one(movie)
    allMovies = movies.find()
    for m in allMovies:
        print(str(m))
        
createMovie()
retrieveMovies()
