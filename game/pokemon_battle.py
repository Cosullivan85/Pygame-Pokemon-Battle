import pygame
import csv


class Game:
    def __init__(self, width, height):
        pygame.init()
        pygame.font.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Pokemon Battle")
        self.large_font = pygame.font.SysFont("cascadia", 48)
        self.medium_font = pygame.font.SysFont("cascadia", 32)
        self.small_font = pygame.font.SysFont("cascadia", 24)
        self.DEFAULT_IMAGE_SIZE = (150, 150)

        # define colors
        self.black = (0, 0, 0)
        self.gold = (218, 165, 32)
        self.grey = (200, 200, 200)
        self.green = (0, 200, 0)
        self.red = (200, 0, 0)
        self.white = (255, 255, 255)

        # starter Pokemon list for selection screen:
        self.starter_pokemon_list = [1, 4, 7, 10, 16, 21, 25, 37, 41, 54]
        self.starter_pokemon = []

        # initial Game status
        self.game_status = "intro"

        while self.game_status != "quit":
            # 1 Process input/events

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_status = "quit"

                # detect keypress
                if event.type == pygame.KEYDOWN:
                    if self.game_status == "intro":
                        self.game_status = "select_pokemon"

            # 2 Draw/render
            if self.game_status == "intro":
                self.screen.fill(self.white)
                self.displayTitleImage()

            if self.game_status == "select_pokemon":
                self.screen.fill(self.white)
                # next select your 3 starter Pokemon, then select first opponent trainer
                self.starterPokemonSelectionScreen()

            pygame.display.flip()
            self.clock.tick(60)

    def starterPokemonSelectionScreen(self):
        self.x = 0
        self.y = 0

        self.pokemon_selection_text = self.large_font.render(
            "Select Three Starter Pokemon", True, self.red
        )
        self.screen.blit(
            self.pokemon_selection_text,
            (
                (self.width / 2) - (self.pokemon_selection_text.get_width() / 2),
                (self.height / 2) - (self.pokemon_selection_text.get_height() / 2) - 25,
            ),
        )

        self.starter_name_positions = [
            (125, 250),
            (300, 250),
            (475, 250),
            (625, 250),
            (775, 250),
            (125, 550),
            (300, 550),
            (475, 550),
            (625, 550),
            (775, 550),
        ]
        self.starter_sprite_positions = [
            (100, 75),
            (275, 75),
            (450, 75),
            (600, 75),
            (750, 75),
            (100, 375),
            (275, 375),
            (450, 375),
            (600, 375),
            (750, 375),
        ]
        for i in range(0, 10):
            self.starter_pokemon.append(Pokemon(int(self.starter_pokemon_list[i])))

            self.starter_pokemon_name = self.starter_pokemon[i].name
            self.pokeText1 = self.small_font.render(
                self.starter_pokemon_name, True, self.black
            )
            self.sprite_image = pygame.image.load(
                self.starter_pokemon[i].official_artwork_front_default_sprite_file_name
            )
            self.sprite_image = pygame.transform.scale(
                self.sprite_image, self.DEFAULT_IMAGE_SIZE
            )
            self.screen.blit(
                self.sprite_image,
                (
                    self.starter_sprite_positions[i][0],
                    self.starter_sprite_positions[i][1],
                ),
            )
            self.screen.blit(
                self.pokeText1,
                (
                    self.starter_name_positions[i][0],
                    self.starter_name_positions[i][1],
                ),
            )

    def displayTitleImage(self):
        # Images
        self.titleImg = pygame.image.load("data/img/Pokémon_logo.svg")
        self.teamTitleImg = pygame.image.load(
            "data/img/PMD_Exploration_Team_artwork.png"
        )

        self.screen.blit(
            self.titleImg,
            (
                (self.width / 2) - (self.titleImg.get_width() / 2),
                (self.height / 2) - (self.titleImg.get_height() / 2) - 200,
            ),
        )

        # Centre the Team tile image on the screen
        self.screen.blit(
            self.teamTitleImg,
            (
                (self.width / 2) - (self.teamTitleImg.get_width() / 2),
                (self.height / 2) - (self.teamTitleImg.get_height() / 2),
            ),
        )

        self.introText1 = self.large_font.render(
            "Let the Battle Begin!", True, self.black
        )
        self.screen.blit(
            self.introText1,
            (
                (self.width / 2) - (self.introText1.get_width() / 2),
                (self.height / 2) - (self.introText1.get_height() / 2) + 225,
            ),
        )
        self.introText2 = self.large_font.render("Press any Key", True, self.black)
        self.screen.blit(
            self.introText2,
            (
                (self.width / 2) - (self.introText2.get_width() / 2),
                (self.height / 2) - (self.introText2.get_height() / 2) + 275,
            ),
        )


class Pokemon:
    """
    Basic class to define a Pokemon. Stats are imported from data csv file.
    """

    def __init__(self, index):
        with open("data/lists/pokemon_stats.csv", newline="") as self.csvfile:
            self.reader = csv.reader(self.csvfile)
            self.data = list(self.reader)
            self.header = self.data.pop(0)

        # headers: index,name,type 1,type 2,hp,attack,defense,sp. atk,sp. def,speed,height,weight,base exp.,gen
        self.index = index
        self.name = self.data[self.index - 1][1]
        self.type_1 = self.data[self.index - 1][2]
        self.type_2 = self.data[self.index - 1][3]
        self.hp = self.data[self.index - 1][4]
        self.attack = self.data[self.index - 1][5]
        self.defense = self.data[self.index - 1][6]
        self.special_attack = self.data[self.index - 1][7]
        self.special_defense = self.data[self.index - 1][8]
        self.speed = self.data[self.index - 1][9]
        self.height = self.data[self.index - 1][10]
        self.weight = self.data[self.index - 1][11]
        self.base_exp = self.data[self.index - 1][12]
        self.gen = self.data[self.index - 1][13]
        self.back_default_sprite_file_name = (
            "data/img/back_default_sprite_" + str(self.index) + ".png"
        )
        self.front_default_sprite_file_name = (
            "data/img/front_default_sprite_" + str(self.index) + ".png"
        )
        self.official_artwork_front_default_sprite_file_name = (
            "data/img/official_artwork_front_default_sprite_" + str(self.index) + ".png"
        )


# create the game window
# width = 960
# height = 720

game = Game(960, 720)
