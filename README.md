## udacity movie trailer project

Project that creates a movie trailer website. To run it:

1. install python 2.7
2. git clone https://github.com/gustavopaes/udacity_movie_trailer_project.git
3. run `python entertainment_center.py`

### How it works

After run `entertainment_center.py` file, `fresh_tomatoes.html` file will be created on
your current directory and it will be open on your default browser.

If you want to change the movies and series, edit the `entertainment_center.py` file adding
a new Movie or TvShow providing a IMDB Id and Youtube Trailer URL.

    toy_story = Movie("tt0114709", "https://www.youtube.com/watch?v=KYz2wyBy3kc")
    elit_squad = Movie("tt0861739", "https://www.youtube.com/watch?v=_gnJB10WTpE")

## What's included

```
udacity_movie_trailer_project/
    ├──entertainment_center.py
    ├──fresh_tomatoes.py
    ├──LICENSE
    ├──media.py
    ├──README.md
```

## third part

* bootstrap framework
* jquery javascript lib
* `fresh_tomatores.py` lib
* Thanks to the [http://www.omdbapi.com/](http://www.omdbapi.com/) that provide movie info API.
