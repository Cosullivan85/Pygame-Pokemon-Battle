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
        for i in range(0, 9):
            self.starter_pokemon.append(Pokemon(int(self.starter_pokemon_list[i])))

        for poke in self.starter_pokemon:
            self.starter_pokemon_name = poke.name
            self.pokeText1 = self.large_font.render(
                self.starter_pokemon_name, True, self.black
            )

            # Need to space out the names properly & change font
            self.screen.blit(
                self.pokeText1,
                (
                    (self.width / 2) - (self.pokeText1.get_width() / 2),
                    (self.height / 2) - (self.pokeText1.get_height() / 2) + 225,
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
