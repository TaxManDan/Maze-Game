import arcade
import arcade.gui


class HomeView(arcade.View):

    def __init__(self):
        super().__init__()

        # Create and enable the UIManager
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.difficulty = "Normal"

        arcade.set_background_color(arcade.color.LIGHT_CORNFLOWER_BLUE)

        help_button = arcade.gui.UIFlatButton(text="HELP", width=200)
        difficulty_button = arcade.gui.UIFlatButton(text="DIFFICULTY", width=200)
        play_button = arcade.gui.UIFlatButton(text="PLAY", width=200)

        button_box = arcade.gui.UIBoxLayout()  # Create a box group to align the 'open' button in the center
        button_box.add(help_button)  # Create a button. We'll click on this to open our window.
        button_box.add(difficulty_button)
        button_box.add(play_button)
        help_button.on_click = self.on_click_help  # Add a hook to run when we click on the button.
        difficulty_button.on_click = self.on_click_difficulty
        play_button.on_click = self.on_click_play

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                # Positioning for first option
                anchor_x="center",
                align_x=0,
                anchor_y="center",
                align_y=-150,


                child=help_button
            )
        )
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center",
                align_x=0,
                anchor_y="center",
                align_y=0,


                child=difficulty_button
            )
        )
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center",
                align_x=0,
                anchor_y="center",
                align_y=150,

                child=play_button
            )
        )

    def on_click_help(self, event):
        # The code in this function is run when we click the ok button.
        # The code below opens the message box and auto-dismisses it when done.
        message_box = arcade.gui.UIMessageBox(
            width=375,
            height=250,
            message_text=(
                "This is a Help Message box for giving users in game hints "
                "click ok to close."
            ),
            callback=self.on_message_box_close,
            buttons=["Ok", "Cancel"]
        )

        self.manager.add(message_box)

    def on_message_box_close(self, button_text):
        print(f"User pressed {button_text}.")

    def on_click_difficulty(self, event):
        # The code in this function is run when we click the ok button.
        # The code below opens the message box and auto-dismisses it when done.
        message_box = arcade.gui.UIMessageBox(
            width=350,
            height=125,
            message_text=(
                "Select the difficulty you want to play(Only Easy currently works)"

            ),
            callback=self.on_difficulty_box_close,
            buttons=["Easy", "Normal", "Hard"]
        )

        self.manager.add(message_box)

    def on_difficulty_box_close(self, button_text):
        self.difficulty = button_text
        print(self.difficulty)

    def on_click_play(self, event):
        difficulty = self.difficulty
        if difficulty == "Easy":
            game_view = EasyView()
        elif difficulty == "Normal":
            game_view = NormalView()
        elif difficulty == "Hard":
            game_view = HardView()
        self.window.show_view(game_view)

    def on_draw(self):
        self.clear()
        self.manager.draw()


class EasyView(arcade.View):
    def __init__(self):
        super().__init__()
        # set a background color
        arcade.set_background_color(arcade.color.BLACK)
        self.wall_list = None
        self.scene = None
        self.player_list = None
        self.player_sprite = None
        self.physics_engine = None
        # --- Required for all code that uses UI element,
        # a UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.setup()
        self.on_draw()


        arcade.finish_render()

    def setup(self):
        self.scene = arcade.Scene()

        # Create the Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)

        # Set up the player, specifically placing it at these coordinates.
        self.player_sprite = arcade.Sprite("images/circle.png", .0625)
        self.player_sprite.center_x = 125
        self.player_sprite.center_y = 125
        self.scene.add_sprite("Player", self.player_sprite)

        wall = arcade.Sprite("images/rectangle.png", 1)
        wall.center_x = 640
        wall.center_y = 50
        self.scene.add_sprite("Walls", wall)

        self.physics_engine = arcade.PhysicsEngineSimple(
            self.player_sprite, self.scene.get_sprite_list("Walls")
        )


    def draw_maze(self):
        walls = arcade.color.BABY_BLUE
        arcade.draw_rectangle_filled(50, 360, 100, 720, walls)
        arcade.draw_rectangle_filled(640, 50, 1280, 100, walls)
        arcade.draw_rectangle_filled(640, 670, 1280, 100, walls)
        arcade.draw_rectangle_filled(1230, 360, 100, 720, walls)
        arcade.draw_rectangle_filled(125, 125, 50, 50, arcade.color.RUBY_RED)
        arcade.draw_rectangle_filled(1155, 595, 50, 50, arcade.color.GO_GREEN)
        arcade.draw_rectangle_filled(175, 285, 50, 370, walls)
        arcade.draw_rectangle_filled(565, 395, 230, 50, walls)
        arcade.draw_rectangle_filled(875, 485, 50, 270, walls)
        arcade.draw_rectangle_filled(1105, 435, 50, 370, walls)
        arcade.draw_rectangle_filled(915, 175, 530, 50, walls)
        arcade.draw_rectangle_filled(415, 545, 530, 50, walls)
        arcade.draw_rectangle_filled(775, 325, 50, 270, walls)
        arcade.draw_rectangle_filled(1005, 325, 50, 270, walls)
        arcade.draw_rectangle_filled(675, 285, 50, 270, walls)
        arcade.draw_rectangle_filled(475, 385, 50, 270, walls)
        arcade.draw_rectangle_filled(375, 235, 50, 270, walls)
        arcade.draw_rectangle_filled(275, 385, 50, 270, walls)

    def on_draw(self):
        """Render the screen."""

        # Clear the screen to the background color
        self.clear()

        # Draw our sprites
        #self.draw_maze()
        self.scene.draw()
        self.wall_list.draw()
        self.player_list.draw()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = 5
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = -5
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -5
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 5

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""

        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """Movement and game logic"""

        # Move the player with the physics engine
        self.physics_engine.update()


class NormalView(arcade.View):
    def __init__(self):
        super().__init__()
        # set a background color
        arcade.set_background_color(arcade.color.CITRON)
        self.clear()
        # --- Required for all code that uses UI element,
        # a UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # set a random number between 1-20

        # --- Finish drawing ---
        arcade.finish_render()


class HardView(arcade.View):
    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.BLACK)
        self.clear()
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.draw_maze()

        arcade.finish_render()

    def draw_maze(self):
        arcade.draw_rectangle_filled(center_x=20, center_y=360, width=40, height=720, color=arcade.color.BABY_BLUE)
        arcade.draw_rectangle_filled(640, 20, 1280, 40, arcade.color.BABY_BLUE)
        arcade.draw_rectangle_filled(640, 700, 1280, 40, arcade.color.BABY_BLUE)
        arcade.draw_rectangle_filled(1260, 360, 40, 720, arcade.color.BABY_BLUE)
        arcade.draw_rectangle_filled(60, 60, 40, 40, arcade.color.RUBY_RED)


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Danny's Maze Game"


def main():
    """ Main function """

    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = EasyView()
    window.show_view(start_view)
    arcade.run()


main()