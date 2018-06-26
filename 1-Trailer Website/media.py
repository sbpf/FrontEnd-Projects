import webbrowser
class Movie():
    def __init__(self,movie_title,movie_storyline,poster_image_url,trailer_video_url):
        self.title = movie_title
        storyline = movie_storyline
        self.poster_image = poster_image_url
        self.trailer_url = trailer_video_url

    def show_trailer(self):
        webbrowser.open(self.trailer_url)
      
        
        
        
