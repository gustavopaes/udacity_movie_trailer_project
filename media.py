import re
import urllib
import json

class Video():
    """This class provides a way to store video related information

    Attributes:
        title (str): video title
        storyline (str): short text about the movie
        poster (str): url to movie poster
        trailer_url (str): youtube url to movie trailer

    Methods:
        get_youtube_id: return youtube id from trailer_url attribute
        get_video_data: fetch video data on amdbapi
    """
    def __init__(self, omdbid, trailer_url):
        self.omdbid = omdbid
        self.trailer_youtube_url = trailer_url
        self.get_video_data()

    def get_youtube_id(self):
        # Extract the youtube ID from the url
        # Source: original fresh_tomatoes.py (udacity)
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', self.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', self.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        return trailer_youtube_id

    def get_video_data(self):
        # Fetch video data on omdbapi and update self data
        connection = urllib.urlopen("http://www.omdbapi.com/?i="+self.omdbid)
        content = connection.read()
        connection.close()
        jsoncontent = json.loads(content)

        self.title = jsoncontent["Title"]
        self.storyline = jsoncontent["Plot"]
        self.poster_image_url = jsoncontent["Poster"]

        if(self.content_type == "movie"):
            self.director = jsoncontent["Director"].encode('utf-8')
        else:
            self.director = "N/A"

        self.year = jsoncontent["Year"].encode('utf-8')
        
class Movie(Video):
    """This class provides a way to store movie related information

    Attributes:
        omdbid (str): movie id on omdb site
        triler_url (str): youtube url to movie trailer
    """
    def __init__(self, omdbid, trailer_url):
        self.content_type = "movie"
        Video.__init__(self, omdbid, trailer_url)

class TvShow(Video):
    """This class provides a way to store movie related information

    Attributes:
        omdbid (str): movie id on omdb site
        triler_url (str): youtube url to movie trailer
    """
    def __init__(self, omdbid, trailer_url):
        self.content_type = "tvshow"
        Video.__init__(self, omdbid, trailer_url)


