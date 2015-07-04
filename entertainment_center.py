"""This module creates a list of favourite movies and TV shows to be displayed by fresh_tomatoes.py"""

import fresh_tomatoes
import media

shawshank = media.Movie("The Shawshank Redemption",
                        "http://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                        "https://www.youtube.com/watch?v=6hB3S9bIaco",
                        "Two imprisoned men bond over a number of years, finding solace & eventual redemption through acts of common decency.",
                        "Tim Robbins, Morgan Freeman")

matrix = media.Movie("The Matrix",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/c/c1/The_Matrix_Poster.jpg/220px-The_Matrix_Poster.jpg",
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU",
                     "A computer hacker learns from mysterious rebels about the true nature of his reality & his role in the war against its controllers.",
                     "Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss")

blood = media.Movie("There Will Be Blood",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/d/da/There_Will_Be_Blood_Poster.jpg/220px-There_Will_Be_Blood_Poster.jpg",
                     "https://www.youtube.com/watch?v=FeSLPELpMeM",
                     "A story of family, religion, hatred, oil and madness, focusing on a turn-of-the-century prospector in the early days of the business",
                     "Daniel Day-Lewis, Paul Dano, Ciaran Hinds")

walle = media.Movie("WALL-E",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/c/c2/WALL-Eposter.jpg/220px-WALL-Eposter.jpg",
                    "https://www.youtube.com/watch?v=alIq_wG9FNk",
                    "In the distant future, a small waste collecting robot inadvertently embarks on a space journey that will ultimately decide the fate of mankind.",
                    "Ben Burtt, Elissa Knight, Jeff Garlin")

old_men = media.Movie("No Country for Old Men",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/8/8b/No_Country_for_Old_Men_poster.jpg/220px-No_Country_for_Old_Men_poster.jpg",
                     "https://www.youtube.com/watch?v=xRA_0GIDAIo",
                     "Violence and mayhem ensue after a hunter stumbles upon a drug deal gone wrong and more than two million dollars in cash near the Rio Grande.",
                     " Tommy Lee Jones, Javier Bardem, Josh Brolin")

orange = media.Movie("A Clockwork Orange",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/4/48/Clockwork_orangeA.jpg/220px-Clockwork_orangeA.jpg",
                     "https://www.youtube.com/watch?v=G7fO3bzPeBQ",
                     "In future Britain, charismatic delinquent Alex DeLarge is jailed and volunteers for an experimental aversion therapy developed by the government in an effort to solve society's crime problem - but not all goes according to plan.",
                     "Malcolm McDowell, Patrick Magee, Michael Bates")

crazy = media.Movie("The Gods Must Be Crazy",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/5/59/Gods_must_be_crazyposter.jpg/220px-Gods_must_be_crazyposter.jpg",
                    "https://www.youtube.com/watch?v=GorHLQ-jLRQ",
                    "A comic allegory about a traveling Bushman who encounters modern civilization and its stranger aspects, including a clumsy scientist and a band of revolutionaries.",
                    "N!xau, Marius Weyers, Sandra Prinsloo")

juno = media.Movie("Juno",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/e/ec/Junoposter2007.jpg/215px-Junoposter2007.jpg",
                     "https://www.youtube.com/watch?v=K0SKf0K3bxg",
                     "Faced with an unplanned pregnancy, an offbeat young woman makes an unusual decision regarding her unborn child.",
                     "Ellen Page, Michael Cera, Jennifer Garner")

district = media.Movie("District 9",
                       "https://upload.wikimedia.org/wikipedia/en/thumb/d/d7/District_nine_ver2.jpg/220px-District_nine_ver2.jpg",
                       "https://www.youtube.com/watch?v=DyLUwOcR5pk",
                       "An extraterrestrial race forced to live in slum-like conditions on Earth suddenly finds a kindred spirit in a government agent who is exposed to their biotechnology.",
                       "Sharlto Copley, David James, Jason Cope")

my_fav_movies= [shawshank, matrix, old_men, blood, walle, orange, crazy, juno, district]
fresh_tomatoes.open_movies_page(my_fav_movies)
