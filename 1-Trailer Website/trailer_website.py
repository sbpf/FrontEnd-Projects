import fresh_tomatoes
import media

# creating the first instance of the class "Movie"
harry_potter = media.Movie("Harry Potter",
                           "Story of an adventurous teenage wizard who gets into a School of Witchcraft and Wizardry",
                           "https://upload.wikimedia.org/wikipedia/en/c/c0/Harry_Potter_and_the_Philosopher%27s_Stone_posters.JPG",
                           "https://www.youtube.com/watch?v=kTzuxWN94PA")

# creating the second instance of the class "Movie"
pursuit_of_happyness = media.Movie("Pursuit Of Happyness",
                                   "A Biographical drama film based on entreprenewur Chis Gardner's nearly one year struggle being homeless.",
                                   "http://daxushequ.com/data/out/98/img60107496.png",
                                   "https://www.youtube.com/watch?v=89Kq8SDyvfg")

# creating the third instance of the class "Movie"
beautiful_mind = media.Movie("A Beautiful Mind",
                             "American biographical drama film based on the life of John Nash, a Nobel Laureate in Economics.",
                             "https://upload.wikimedia.org/wikipedia/sh/9/98/Abeautifulmindposter.jpg",
                             "https://www.youtube.com/watch?v=YWwAOutgWBQ")

# Adding all the instances created to a list called "movies"
movies = [harry_potter, pursuit_of_happyness, beautiful_mind]

# Invoking a function open_movies_page defined in fresh_tomatoes and passing the list of movies as an argument
fresh_tomatoes.open_movies_page(movies)
