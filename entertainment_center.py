from media import Movie, TvShow
import fresh_tomatoes

# Create movies and series to website
toy_story = Movie("tt0114709",
                  "https://www.youtube.com/watch?v=KYz2wyBy3kc")

elit_squad = Movie("tt0861739",
                   "https://www.youtube.com/watch?v=_gnJB10WTpE")

pulp_fiction = Movie("tt0110912",
                     "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

friends = TvShow("tt0108778",
                 "https://www.youtube.com/watch?v=hDNNmeeJs1Q")

sopranos = TvShow("tt0141842",
                  "https://www.youtube.com/watch?v=ch-X-9J73aQ")

movies = [toy_story, elit_squad, pulp_fiction]
series = [sopranos, friends]

# Concatenate movies and series into videos
# which will send to fresh_tomatoes api
videos = movies + series

# Open video trailers website
fresh_tomatoes.open_movies_page(videos)


