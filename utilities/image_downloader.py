# Script to download Pokemon Sprites and save to folder

import csv
import requests
import json
import shutil


# for each Pokemon in the file, get the relevant sprite urls from Pokeapi


class Pokemon_API_Call:
    _url = "https://pokeapi.co/api/v2/pokemon/"

    def __init__(self, id):
        self.api_call = requests.get(self._url + str(id))
        self.json_api_call = self.api_call.json()

    def return_back_default_sprite_url(self):
        return self.json_api_call["sprites"]["back_default"]

    def return_front_default_sprite_url(self):
        return self.json_api_call["sprites"]["front_default"]

    def return_official_artwork_front_default_sprite_url(self):
        return self.json_api_call["sprites"]["other"]["home"]["front_default"]


def downloadSpriteImageURLs():
    # open the pokemon sprite csv file
    # first row is read as the header

    with open("data/lists/pokemon_sprite_files.csv", newline="") as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
        header = data.pop(0)

    # Data header format is as follows:
    # index,name,back_default_sprite_url,front_default_sprite_url,official_artwork_front_default

    for x in range(1, 494):
        poke_call = Pokemon_API_Call(x)
        data[x - 1][2] = poke_call.return_back_default_sprite_url()
        data[x - 1][3] = poke_call.return_front_default_sprite_url()
        data[x - 1][4] = poke_call.return_official_artwork_front_default_sprite_url()

    with open("data/lists/pokemon_sprite_files.csv", "w", newline="") as csvfile:
        w = csv.writer(csvfile)
        w.writerow(header)
        for row in data:
            w.writerow(row)


def downloadSpriteImageFiles():
    with open("data/lists/pokemon_sprite_files.csv", newline="") as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
        header = data.pop(0)

    # Data header format is as follows:
    # index,name,back_default_sprite_url,front_default_sprite_url,official_artwork_front_default
    for x in range(0, 493):
        back_default_sprite_url = data[x][2]
        back_default_sprite_file_name = (
            "data/img/back_default_sprite_" + str(x + 1) + ".png"
        )
        front_default_sprite_url = data[x][3]
        front_default_sprite_file_name = (
            "data/img/front_default_sprite_" + str(x + 1) + ".png"
        )
        official_artwork_front_default_sprite_url = data[x][4]
        official_artwork_front_default_sprite_file_name = (
            "data/img/official_artwork_front_default_sprite_" + str(x + 1) + ".png"
        )

        res = requests.get(back_default_sprite_url, stream=True)
        if res.status_code == 200:
            with open(back_default_sprite_file_name, "wb") as f:
                shutil.copyfileobj(res.raw, f)
            print("Image sucessfully Downloaded: ", back_default_sprite_file_name)
        else:
            print("Image Couldn't be retrieved")

        res = requests.get(front_default_sprite_url, stream=True)
        if res.status_code == 200:
            with open(front_default_sprite_file_name, "wb") as f:
                shutil.copyfileobj(res.raw, f)
            print("Image sucessfully Downloaded: ", front_default_sprite_file_name)
        else:
            print("Image Couldn't be retrieved")

        res = requests.get(official_artwork_front_default_sprite_url, stream=True)
        if res.status_code == 200:
            with open(official_artwork_front_default_sprite_file_name, "wb") as f:
                shutil.copyfileobj(res.raw, f)
            print(
                "Image sucessfully Downloaded: ",
                official_artwork_front_default_sprite_file_name,
            )
        else:
            print("Image Couldn't be retrieved")


downloadSpriteImageFiles()
