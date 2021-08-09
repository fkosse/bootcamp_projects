from MovieRecommender import MovieRecommender


def get_recommendations(base_dict):
    movie_name = base_dict['name1']
    u_rating = base_dict['rating1']
    u = MovieRecommender(movie_name, u_rating)
    return u.recommendations