"""This module defines the Movie and TV show objects to be used in entertainment_center.py"""

class Movie(object):

	"""This class provides a way to construct a movie object with movie details"""
	def __init__(self, title, poster_image_url, trailer_youtube_url, plot, cast):
		self.title = title
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url
		self.plot = plot
		self.cast = cast
