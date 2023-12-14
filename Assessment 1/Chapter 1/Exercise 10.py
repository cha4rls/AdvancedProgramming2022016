#Dictionary for the details of the movie
movie = {
    "Title": "2 Fast 2 Furious",
    "Year": 1994,
    "Director": "John Singleton",
    "Genre": "Action/Crime",
    "Rating": 5.9
}

#Displays the information using for loop
print("-----Movie Details-----")
for key, value in movie.items():
    print(f"{key}: {value}")