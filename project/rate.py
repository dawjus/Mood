import json


def rate(title, rate):
    jsonFile = open("moviesent.json", "r")  # Open the JSON file for reading
    data = json.load(jsonFile)  # Read the JSON into the buffer
    jsonFile.close()  # Close the JSON file
    for i in range(0, len(data)):
        if data[i]['title'] == title:
            data[i]["ratings"] = (data[i]["ratings"] + rate) / 2

    # Save our changes to JSON file
    jsonFile = open("moviesent.json", "w+")
    jsonFile.write(json.dumps(data, indent=2))
    jsonFile.close()


def main():
    title = 'Avatar'
    vote = 9
    rate(title, vote)


if __name__ == "__main__":
    main()
