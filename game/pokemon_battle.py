import pygame


class Game:
    def __init__(self, width, height):
        pygame.init()
        pygame.font.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Pokemon Battle")
        self.font = pygame.font.SysFont("cascadia", 48)

        # define colors
        self.black = (0, 0, 0)
        self.gold = (218, 165, 32)
        self.grey = (200, 200, 200)
        self.green = (0, 200, 0)
        self.red = (200, 0, 0)
        self.white = (255, 255, 255)

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
                # next select your starter Pokemon, then select first opponent

            pygame.display.flip()
            self.clock.tick(60)

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

        self.introText1 = self.font.render("Let the Battle Begin!", True, self.black)
        self.screen.blit(
            self.introText1,
            (
                (self.width / 2) - (self.introText1.get_width() / 2),
                (self.height / 2) - (self.introText1.get_height() / 2) + 225,
            ),
        )
        self.introText2 = self.font.render("Press any Key", True, self.black)
        self.screen.blit(
            self.introText2,
            (
                (self.width / 2) - (self.introText2.get_width() / 2),
                (self.height / 2) - (self.introText2.get_height() / 2) + 275,
            ),
        )


# create the game window
# width = 960
# height = 720

game = Game(960, 720)
