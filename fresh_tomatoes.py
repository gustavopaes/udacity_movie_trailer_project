import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        .navbar-filter-label {
            color: #fff;
            font-weight: bold;
        }
        .navbar-filter {
            line-height: 50px;
            padding-right: 10px;
            color: #fff;
        }
        .navbar-filter:hover,
        .navbar-filter:active,
        .navbar-filter:visited {
            color: #fff;
            cursor: pointer;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .movie-tile small {
            font-size: 16px;
            line-height: 15px;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // filter videos
        $(document).on('click', '.navbar-filter', function (event) {
            var $body = $('body')
            $('.movie-tile').show('fast');

            switch(this.hash) {
                case '#movies':
                    $('.movie-tile').filter('.video-tvshow').hide('fast');
                    break;

                case '#tvshows':
                    $('.movie-tile').filter('.video-movie').hide('fast');
                    break;
            }
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Drama Video Trailers</a>
          </div>

          <div class="text-right">
            <span class="navbar-filter-label">Show:</span>
            <a class="navbar-filter" href="#all">All</a>
            <a class="navbar-filter" href="#tvshows">TV Shows</a>
            <a class="navbar-filter" href="#movies">Movies</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-lg-12 video-{video_type} movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <div class="col-lg-3">
        <img src="{poster_image_url}" width="220" height="342">
    </div>
    <div class="col-lg-4 text-left">
        <h2>
            <small class="video-type">{video_type}</small>
            {video_title}
        </h2>
        <p>{video_plot}</p>
        <dl>
            <dt>Year</dt>
            <dd>{video_year}</dd>

            <dt>Director</dt>
            <dd>{video_director}</dd>
        </dl>
    </div>
</div>
'''


def create_movie_tiles_content(videos):
    # The HTML content for this section of the page
    content = ''
    for video in videos:
        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            video_title=video.title,
            video_type=video.content_type,
            poster_image_url=video.poster_image_url,
            trailer_youtube_id=video.get_youtube_id(),
            video_plot=video.storyline,
            video_year=str(video.year),
            video_director=str(video.director)
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
