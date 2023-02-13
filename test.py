import json

if __name__ == "__main__":
    with open(f'./standard_data/google_career_1.json', 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)
    dic = dict(json_object)
    print(len(dic))