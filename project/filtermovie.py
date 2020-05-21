import json
from .analyzer import analyzer


def filtermovie(genre, answer1, answer2, answer3, answer4):
    sentanswer1 = analyzer(answer1)
    sentanswer2 = analyzer(answer2)
    sentanswer3 = analyzer(answer3)
    sentanswer4 = analyzer(answer4)
    sentgenre = analyzer(genre)
    sentuser = (sentanswer1 + sentanswer2 +
                sentanswer3 + sentanswer4 + sentgenre) / 5
    movie2 = []

    with open("project/moviesent.json", "r") as infile:
        movie = json.load(infile)

    for i in range(0, len(movie)):
        txt = movie[i]['genres']
        x = txt.split("|")
        for y in range(0, len(x)):
            if genre.lower() in x[y].lower():
                if movie[i]['sentiment'] > sentuser:
                    movie2.append(
                        {"title": movie[i]['title'], "ratings": movie[i]['ratings'], "genres": movie[i]['genres']})

    # Open the JSON file for reading
    jsonFile = open("project/filterhistory.json", "r")
    data = json.load(jsonFile)  # Read the JSON into the buffer
    jsonFile.close()  # Close the JSON file
    data.append((genre, answer1, answer2, answer3, answer4))
    # Save our changes to JSON file
    jsonFile = open("project/filterhistory.json", "w+")
    jsonFile.write(json.dumps(data, indent=2))
    jsonFile.close()

    return (movie2)
