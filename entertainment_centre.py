import fresh_tomatoes
import media

''' Script to produce movie website.  '''


American_Sniper = media.Movie("AMERICAN SNIPER",
                              " ",
                              "http://bit.ly/18LI1Gg",
                              "https://youtu.be/99k3u9ay1gs")

Fury = media.Movie("FURY",
                   " ",
                   "http://bit.ly/2uUJObE",
                   "https://youtu.be/09w9MTtZDEM")

Lone_Survivor = media.Movie("LONE SURVIVOR",
                            " ",
                            "http://bit.ly/2x3haCC",
                            "https://youtu.be/yoLFk4JK_RM")

Hacksaw_Ridge = media.Movie("HACKSAW RIDGE",
                            " ",
                            "http://bit.ly/2igIbPy",
                            "https://youtu.be/s2-1hz1juBI")

NYSM2 = media.Movie("NOW YOY SEE ME 2",
                    " ",
                    "http://bit.ly/2vZXBe8",
                    "https://youtu.be/InqU8CLwbPg")

Argo = media.Movie("ARGO",
                   " ",
                   "https://goo.gl/YzD4bs",
                   "https://youtu.be/T29kIOXpj6o")

movies = [American_Sniper, Fury, Lone_Survivor, Hacksaw_Ridge, NYSM2, Argo]
fresh_tomatoes.open_movies_page(movies)
