import media
import fresh_tomatoes

# This line creates the instance "Toy_story" of the Movie class
toy_story = media.Movie("TOY STORY","STORY OF TOYS","https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0,0,300,450","https://www.youtube.com/watch?v=KYz2wyBy3kc")
# This line creates the instance "harold_kumar" of the Movie class
harold_kumar = media.Movie("HAROLD AND KUMAR","Two boys going to white castle with lots of huddles","https://upload.wikimedia.org/wikipedia/en/7/72/Harold_%26_Kumar_Go_to_White_Castle.JPG","https://www.youtube.com/watch?v=cwP5E15VzRM")
# This line creates the instance "prestige" of the Movie class
prestige = media.Movie("THE PRESTIGE","Story of two Bold magicians","https://i.jeded.com/i/the-prestige.14577.jpg","https://www.youtube.com/watch?v=o4gHCmTQDVI")
# This line creates the instance "shawshank" of the Movie class
shawshank = media.Movie("THE SHAWSHANK REDEMPTIOM","Old century movie about ANDY and his life in prison","https://images-na.ssl-images-amazon.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_UY1200_CR88,0,630,1200_AL_.jpg","https://www.youtube.com/watch?v=NmzuHjWmXOc")
# This line creates the instance "inter" of the Movie class
inter=media.Movie("THE INTERSTELLAR","About the long journey in space","https://images-na.ssl-images-amazon.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_UY1200_CR69,0,630,1200_AL_.jpg","https://www.youtube.com/watch?v=zSWdZVtXT7E")
# This line creates the instance "shutter" of the Movie class
shutter=media.Movie("SHUTTER ISLAND","A deep mystery about rachel salando missing case","https://s3-ap-southeast-2.amazonaws.com/fna-wordpress-website06/wp-content/uploads/2016/11/26021839/Shutter-Island-1440x960.jpg","https://www.youtube.com/watch?v=5iaYLCiq5RM")

# This creates an array of movies containing all the instances of the class.
Films=[toy_story,harold_kumar,prestige,shawshank,inter,shutter]
# The array of movies is passed as an argument
fresh_tomatoes.open_movies_page(Films)


