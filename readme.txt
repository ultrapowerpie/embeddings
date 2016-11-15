################################################################################

Name: Jackey Liu
Netid: guanghao

################################################################################

Running the code:

$ python MovieEmbeddings.py

Running the MovieEmbeddings.py module will create an output.txt file that lists
the 20 most similar movies to "The Lion King", and the 20 most similar movies to
the movies "Sleepless in Seattle", "Philadelphia Story", and
"Sex, Lies, and Videotape"

################################################################################

About:

The MovieEmbeddings class has 4 objects:

# The movies dictionary maps movie ids to their titles.

movies := a dictionary of { movie id: movie title }

# The movie_ratings dictionary maps user ids to movies they liked
# (since dislikes are not used by the coocurrence matrix, they are discarded)

movie_ratings := a dictionary of { user id: set([movie ids]) }

# The coocurrence matrix is an n x n array of all 1682 movies with entry [i, j]
# being the number of people who liked both movie i and movie j.

coocurrences := an n x n numpy array

# The movie embeddings vector is an n x 300 array of 300 features of all 1682
# movies

embeddings := an n x 300 numpy array

################################################################################

Output:

Recommender 1 (Movies most similar to "The Lion King"):

('Lion King, The (1994)\r\n', 1.0000000000000002)
('Aladdin (1992)\r\n', 0.80068618196028629)
('Beauty and the Beast (1991)\r\n', 0.79965703312657743)
('Forrest Gump (1994)\r\n', 0.79409792874493668)
('Apollo 13 (1995)\r\n', 0.77874665197263659)
('E.T. the Extra-Terrestrial (1982)\r\n', 0.77181028931140239)
('Jurassic Park (1993)\r\n', 0.75954209331863376)
('Back to the Future (1985)\r\n', 0.75362098434730862)
('Dances with Wolves (1990)\r\n', 0.72246923517934125)
("It's a Wonderful Life (1946)\r\n", 0.71616664251252249)
('Toy Story (1995)\r\n', 0.71505483593507047)
('Field of Dreams (1989)\r\n', 0.71485304669976935)
('Cinderella (1950)\r\n', 0.71125402627140299)
('Top Gun (1986)\r\n', 0.70799686278560348)
('Sound of Music, The (1965)\r\n', 0.70632279326152358)
('Mrs. Doubtfire (1993)\r\n', 0.70550324214714988)
('Braveheart (1995)\r\n', 0.7027105841492276)
('Speed (1994)\r\n', 0.69735685110958745)
('Ghost (1990)\r\n', 0.69628418638461087)
('Snow White and the Seven Dwarfs (1937)\r\n', 0.69614274139315313)

Recommender 2 (Movies most similar to "Sleepless in Seattle",
"Philadelphia Story", and "Sex, Lies, and Videotape"):

('Sleepless in Seattle (1993)\r\n', 0.81452909366803417)
('When Harry Met Sally... (1989)\r\n', 0.79687083137550785)
('Philadelphia Story, The (1940)\r\n', 0.77045044624846326)
('Amadeus (1984)\r\n', 0.74318409322640311)
('Four Weddings and a Funeral (1994)\r\n', 0.74263678478897333)
('Dead Poets Society (1989)\r\n', 0.74140168459209177)
('Back to the Future (1985)\r\n', 0.74058180847806754)
('Sex, Lies, and Videotape (1989)\r\n', 0.73971774298511495)
('Dances with Wolves (1990)\r\n', 0.73262005696426424)
('E.T. the Extra-Terrestrial (1982)\r\n', 0.72914825279662565)
("It's a Wonderful Life (1946)\r\n", 0.72861020347739591)
('Wizard of Oz, The (1939)\r\n', 0.72751243995429804)
('Sting, The (1973)\r\n', 0.72691649270205472)
('Butch Cassidy and the Sundance Kid (1969)\r\n', 0.71065729291311819)
('Graduate, The (1967)\r\n', 0.71030629047505889)
('M*A*S*H (1970)\r\n', 0.70785598450139475)
('Casablanca (1942)\r\n', 0.70477399400216401)
('Fish Called Wanda, A (1988)\r\n', 0.69298102881730028)
('To Kill a Mockingbird (1962)\r\n', 0.691520714987515)
('Gandhi (1982)\r\n', 0.68823872633899774)
