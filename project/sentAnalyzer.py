
import json
from analyzer import analyzer
def main():
    movie2 = []
    with open('movie.json') as infile:
        movie = json.load(infile)
    # print(movie[0]['overview'])
    with open('moviesent2.json', 'w') as f:
        for i in range(0, 1000):
            movie2.append({"title": movie[i]['title'], "ratings": movie[i]['vote_average'], "sentiment": analyzer(movie[i]['overview'])})
        json.dump(movie2, f, indent=2)



if __name__ == "__main__":
    main()
