import numpy as np

class MovieEmbeddings:

    def __init__(self, movies_file, ratings_file):
        self.movies = self.load_movies(movies_file)
        self.movie_ratings = self.load_ratings(ratings_file)
        self.cooccurences = self.make_cooccurence()
        self.save_cooccurences("cooccurrence.csv.gz")
        self.embeddings = self.train()

    def load_movies(self, movies_file, delimiter="|"):
        '''
        Returns the dcitionary of movie ids to movie titles
        '''
        movies = {}
        movie_dict = {}
        with open(movies_file) as f:
            for line in f:
                t = line.split(delimiter)
                movies[int(t[0])] = t[1]
        return movies

    def load_ratings(self, ratings_file, delimiter=","):
        '''
        Returns the dictionary of users to the set of movies they liked
        '''
        users_dict = {}
        with open(ratings_file) as f:
            for line in f:
                t = line.split(delimiter)
                movie_id, user_id, rating = (int(t[0]), int(t[1]), int(t[2]))
                if not rating:
                    continue
                if user_id in users_dict:
                    users_dict[user_id].add(movie_id)
                else:
                    users_dict[user_id] = set([movie_id])
        return users_dict

    def make_cooccurence(self):
        '''
        Returns a cooccurence matrix from self.movie_ratings
        '''
        movies = len(self.movies.keys())
        cooccurences = np.zeros((movies, movies))
        # the u's are dictionaries every user's movie ratings
        for u in self.movie_ratings.values():
            for i in u:
                for j in u:
                    cooccurences[i-1,j-1] += 1
        return cooccurences

    def save_cooccurences(self, file):
        '''
        Saves the cooccurence matrix to a file
        '''
        np.savetxt(file, self.cooccurences)
        return

    def train(self):
        '''
        Trains the embedded movie vector
        '''
        n = self.cooccurences.shape[0]
        k = 300
        eta = 0.00001
        iterations = 200
        v = np.random.randn(n, k)
        for i in range(iterations):
            if i < 11 or i == iterations-1:
                print "Iter: %d, cost: %.2f" % (i, self.cost(v))
            v = self.gradient(v, eta)
        return v

    def gradient(self, v, eta):
        '''
        one step of the gradient descent algorithm on the movie vector
        '''
        grad = np.dot(v, v.T) - self.cooccurences
        np.fill_diagonal(grad, 0)
        return v-4*eta*np.dot(grad, v)

    def cost(self, v):
        '''
        Calculates the cost function of the gradient descent on the movie vector
        '''
        c = np.square(self.cooccurences - np.dot(v,v.T))
        np.fill_diagonal(c, 0)
        return np.sum(c)

    def cosine_similarity(self, v1, v2):
        '''
        Returns the cosine similarity of two vectors
        '''
        a = np.linalg.norm(v1)
        b = np.linalg.norm(v2)
        return np.divide(np.dot(v1,v2), a*b)

    def recommend1(self, movie, r):
        '''
        Given a movie id, return the r most similar movies
        '''
        if movie not in self.movies:
            return []

        scores = []
        v = self.embeddings[movie-1,:]

        for i, name in self.movies.items():
            s = self.cosine_similarity(v, self.embeddings[i-1,:])
            scores.append((name, s))

        return sorted(scores, key=lambda x: x[1], reverse=True)[:r]

    def recommend2(self, movies, r):
        '''
        Given a list of movie ids, return the r most similar movies
        '''
        n = 0
        v = np.zeros(self.embeddings.shape[1])
        for m in movies:
            if m not in self.movies:
                continue

            v += self.embeddings[m-1,:]
            n += 1

        v = np.divide(v, n)
        scores = []

        for i, name in self.movies.items():
            s = self.cosine_similarity(v, self.embeddings[i-1,:])
            scores.append((name, s))

        return sorted(scores, key=lambda x: x[1], reverse=True)[:r]

if __name__ == "__main__":
    me = MovieEmbeddings("movies.csv", "movieratings.csv")

    recommend1 = me.recommend1(71, 20)
    recommend2 = me.recommend2([88, 478, 708], 20)

    with open("output.txt", "w") as f:
        f.write("Recommender 1: \n\n")
        for r in recommend1:
            f.write(str(r)+"\n")
        f.write("\nRecommender 2: \n\n")
        for r in recommend2:
            f.write(str(r)+"\n")
