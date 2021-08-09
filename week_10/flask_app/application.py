from flask import Flask
from MovieRecommender import movie_rec, movie_list
from flask import render_template
from flask import request
from omdbapi.movie_search import GetMovie

movie_db = GetMovie(api_key='c9287ac7')

app = Flask(__name__)

@app.route('/')
def index():
    names = movie_list
    return render_template('index.html', title='Awesome Movie Recommender', movienames = names)


@app.route('/recommender')
def recommender():
    html_form_data = dict(request.args)
    # a python dictionary consisting of
    # "name"-value pairs from the HTML form!

    recs = movie_rec.get_recommendations(html_form_data)
    # at this point, we would then pass this
    #information as an argument into our recommender function.

    user_recs = movie_rec.get_user_based_rec(html_form_data)

    hidden_gems = movie_rec.get_hidden_gems()

   # image = movie_db.get_movie(title= hidden_gems[0]) 

    print(html_form_data)

    return render_template('recommendations.html',
                            movies = recs, u_movies = user_recs, hid_movies = hidden_gems) #image_link = image

@app.route('/movielist')
def movielist():

    return render_template('movielist.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)

