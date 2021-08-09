import numpy as np
from sklearn.decomposition import NMF
import pandas as pd
import pickle
from json import dumps

from sklearn.impute import KNNImputer
from sklearn.metrics.pairwise import cosine_similarity

small = 'data/ml-latest-small/ratings.csv'

class MovieRecommender():
    ''' Class for getting movie recommendations.

    Attributes
    ==========
    
    data_set

    user_movies

    user_ratings

    recommender_choice


    Methods
    =======
    get_data(path)

    prepare_model(n_c)
    
    make_movie_idx

    make_movie_idx_rev
    
    get_input(movie_name, u_rating)

    make_prediction(model, Q)

    find_movie(movie_rec)

    get_negative()

    get_user_based_rec()

    '''

    def __init__(self):
        self.load_data()
        self.make_movie_idx()
        self.make_movie_idx_rev()

        #get_reco
        #self.get_input()
        #self.make_prediction()
        #self.more_recommendations()
    

    def __repr__(self): 
        return f"MovieRecommender(based on: {self.user_movie}, {self.user_rating})"

    def load_data(self):
        self.u_m_matrix = pd.read_csv('u_m_matrix.csv', index_col= 0)
        self.u_m_matrix_n = pd.read_csv('u_m_matrix_n.csv', index_col= 0)
        filename = 'model_small.sav'
        self.model, self.Q, self.R = pickle.load(open(filename, 'rb'))
         
    
    def make_movie_idx(self):
        self.movies = pd.read_csv('data/ml-latest-small/movies.csv',index_col=0)
        ids = self.movies.index
        names = self.movies.title
        zip_iterator = zip(ids, names)
        self.movie_index = dict(zip_iterator)
   

    def make_movie_idx_rev(self):
        movies = pd.read_csv('data/ml-latest-small/movies.csv',index_col=0)
        ids = movies.index
        names = movies.title
        zip_iterator = zip(names, ids)
        self.movie_idx_rev = dict(zip_iterator)

    def get_input(self, html_dict):
        new_user = np.full(shape=(1,self.R.shape[1]), fill_value=2.5)
        self.new_user = pd.DataFrame(new_user,
                    index= [self.R.shape[0]+1],
                    columns= self.u_m_matrix.columns)
        for i in range(1,5):
            movie_name = html_dict[f'name{i}']
            rating = float(html_dict[f'rating{i}'])
            user_pref = self.movie_idx_rev[movie_name]
            self.new_user.loc[self.R.shape[0]+1][str(user_pref)] = rating
       

    def make_prediction(self):
        user_P = self.model.transform(self.new_user)
        self.actual_recommendations = np.dot(user_P, self.Q)
        #np.argsort(actual_recommendations) #index of a sorted array
        #self.movie_rec = np.argmax(actual_recommendations)
        self.movie_rec_10 = np.argsort(self.actual_recommendations[0])[-10:][::-1]
        self.hidden_gems = np.argsort(self.actual_recommendations[0])[-30:-27][::-1]
    

    def find_movie(self, movie_rec):
        loca = self.u_m_matrix.columns[movie_rec]
        return self.movie_index[int(loca)]
        

    def more_recommendations(self):
        self.recommendations = []
        for i in self.movie_rec_10:
            self.recommendations.append(self.find_movie(i))
        return self.recommendations

    def get_hidden_gems(self):
        self.hidden_rec = []
        for i in self.hidden_gems:
            self.hidden_rec.append(self.find_movie(i))
        return self.hidden_rec
        
    
    def get_recommendations(self, rating_dict):
        self.get_input(rating_dict)
        self.make_prediction()
        return self.more_recommendations()

    
    def get_input_negative(self, html_dict):
        self.new_user_n = np.full(shape=(1,self.R.shape[1]), fill_value=0)
        self.new_user_n = pd.DataFrame(self.new_user_n,
                    index= [self.R.shape[0]+1],
                    columns= self.u_m_matrix.columns)
        for i in range(1,5):
            movie_name = html_dict[f'name{i}']
            rating = float(html_dict[f'rating{i}'])
            user_pref = self.movie_idx_rev[movie_name]
            if rating <= 2.5:
                rating = -2.5 + rating
            elif rating > 2.5:
                rating = rating -2.5
            self.new_user_n.loc[self.R.shape[0]+1][str(user_pref)] = rating
    
    def get_user_based_rec(self, html_dict):
        self.get_input_negative(html_dict)
        added_user = self.u_m_matrix_n.append(self.new_user_n)
        cs = cosine_similarity(added_user)
        cs = pd.DataFrame(cs, index = np.arange(1,cs.shape[1]+1))
        cs.columns = np.arange(1,len(cs.columns)+1)
        self.related_users = cs.loc[added_user.shape[0]]
        self.related_users.pop(added_user.shape[0])
        best_recommendations = cs.iloc[self.related_users.index[np.argmax(self.related_users)]]
        mov_id = cs.columns[(np.argmax(best_recommendations))]
        return self.movie_index[mov_id]

        

movie_rec = MovieRecommender()
movie_list = list(movie_rec.movies.title)
movie_list = str(dumps(movie_list))


if __name__ == "__main__":
    html_dict = {'name1':'Pretty Woman (1990)', 'rating1': '5', 'name2': 'Romeo and Juliet (1968)', 'rating2': '5'}
    u = MovieRecommender()
    print(u.get_recommendations(html_dict))
    print(u.movie_rec_10)
    print(u.new_user)
    html_dict = {'name1':'Clueless (1995)', 'rating1': '5', 'name2': 'Scream (1996)', 'rating2': '5'}
    u = MovieRecommender()
    print(u.get_recommendations(html_dict))
    print(u.movie_rec_10)
    print(np.argsort(u.actual_recommendations))
    print(u.get_user_based_rec(html_dict))
    print(np.sort(u.related_users))
