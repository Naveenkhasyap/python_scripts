import media
import fresh_tomatoes
toy_story = media.Movie("Toy Story","A Story of toys and his friends which comes to life"
                        ,"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://youtu.be/Bj4gS1JQzjk")

avatar =  media.Movie("Avatar","A marine on alien planet"
                        ,"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY")

hebbuli = media.Movie("Hebbuli","A Story of a soldier who return home and fights corruption"
                        ,"https://upload.wikimedia.org/wikipedia/en/f/fc/Hebbuli_poster.jpg",
                        "https://www.youtube.com/watch?v=6vmB0j_zyNk")

kirik_party =  media.Movie("kirik party","A marine on alien planet"
                        ,"https://upload.wikimedia.org/wikipedia/en/thumb/1/1f/Kirik_Part_Poster.jpg/330px-Kirik_Part_Poster.jpg",
                        "https://www.youtube.com/watch?v=IfvnbER_6sQ")

lala_land = media.Movie("La La Land","A Story of toys and his friends which comes to life"
                        ,"https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png",
                        "https://www.youtube.com/watch?v=0pdqf4P9MB8")

logan =  media.Movie("Logan","A marine on alien planet"
                        ,"https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg",
                        "https://www.youtube.com/watch?v=DekuSxJgpbY")

#print(avatar.storyline)
#avatar.show_trailer()

movies = [toy_story,avatar,hebbuli,kirik_party,lala_land,logan]

fresh_tomatoes.open_movies_page(movies)
