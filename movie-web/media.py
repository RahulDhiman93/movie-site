import webbrowser
#class movie
class Movie():
	def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
		"""
    	This function contains the details of the movie.
    	Args:
    	self:It points on a particluar movie.
    	movie_title:represents movie title.
    	movie_storyline:represents the movie story line.
    	poster_image:represents the poster image.
    	trailer_youtube:represents the youtube trailer of the particluar movie.
 		"""
		self.title=movie_title
		self.storyline=movie_storyline
		self.poster_image_url=poster_image
		self.trailer_youtube_url=trailer_youtube

	def show_trailer(self):
		"""
    	This function is used to play the trailer of the movie.
 	 	Args:
    	self:It points on the particluar trailer which is to be played.
    	"""
		webbrowser.open(self.trailer_youtube_url)
