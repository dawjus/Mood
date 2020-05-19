import json
from analyzer import analyzer


def main():
    movie2 = []
    genres = []
    with open('movie.json') as infile:
        movie = json.load(infile)

    with open('moviesent.json', 'w') as f:
        for i in range(0, 1000):
            movie2.append({"title": movie[i]['title'], "ratings": movie[i]['vote_average'],"genres":movie[i]['genres'],"sentiment": analyzer(movie[i]['overview'])})
        json.dump(movie2, f, indent=2)

    with open('genres.json', 'w') as f1:
        for i in range(0, len(movie)):
            txt = movie[i]['genres']
            x = txt.split("|")
            for y in range(0, len(x)):
                if x[y] not in genres:
                    genres.append(x[y])
        json.dump(genres, f1, indent=2)


if __name__ == "__main__":
    main()
