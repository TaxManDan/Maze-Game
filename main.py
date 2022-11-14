import arcade
import arcade.gui

# Set player movement speed
PLAYER_MOVEMENT_SPEED = 5

# Create the home view for the game
class HomeView(arcade.View):

    def __init__(self):
        super().__init__()

        # Create and enable the UIManager
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.difficulty = "Easy"

        arcade.set_background_color(arcade.color.LIGHT_CORNFLOWER_BLUE)

        # Create all the buttons for the Game
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
                "This is a simple maze game where you play as the orange circle"
                "and you have to get from the red square to the green square to win."
                "If you want to go back and change your difficulty just press 'B' at anytime"
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
        else:
            game_view = HomeView()
        self.window.show_view(game_view)

    def on_draw(self):
        self.clear()
        self.manager.draw()


class EasyView(arcade.View):
    def __init__(self):
        super().__init__()
        # set a background color
        arcade.set_background_color(arcade.color.BLACK)
        # self.wall_list = None
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.scene = None
        self.player_sprite = None
        self.finish_sprite = None
        self.physics_engine = None
        # --- Required for all code that uses UI element,
        # a UIManager to handle the UI.
        self.setup()
        self.on_draw()

    def setup(self):
        """Set up the game here. Call this function to restart the game."""

        # Initialize Scene
        self.scene = arcade.Scene()

        # Set up the player, specifically placing it at these coordinates.
        image_source = "images/circle.png"
        self.player_sprite = arcade.Sprite(image_source, 0.06, hit_box_algorithm="Simple")
        self.player_sprite.center_x = 125
        self.player_sprite.center_y = 125
        # Set up the finish at the end.
        self.finish_sprite = arcade.Sprite("images/finish.png",1, center_x=1155, center_y=595)
        self.scene.add_sprite("Player", self.finish_sprite)
        self.scene.add_sprite("Player", self.player_sprite)

        # Create the Walls of the maze
        wall = arcade.Sprite("images/rectangle.png", 1, center_x=640, center_y=50)
        self.scene.add_sprite("Walls", wall)
        wall = arcade.Sprite("images/rectangle.png", 1, center_x=640, center_y=670)
        self.scene.add_sprite("Walls", wall)
        wall = arcade.Sprite("images/wall1.png", 1, center_x=50, center_y=360)
        self.scene.add_sprite("Walls", wall)
        wall = arcade.Sprite("images/wall1.png", 1, center_x=1230, center_y=360)
        self.scene.add_sprite("Walls", wall)
        wall = arcade.Sprite("images/wall1.png", 1, image_width=50, image_height=370, center_x=175, center_y=285)
        self.scene.add_sprite("Walls", wall)
        wall = arcade.Sprite("images/wall1.png", 1, image_width=50, image_height=270, center_x=565, center_y=395)
        self.scene.add_sprite("Walls", wall)
        wall = arcade.Sprite("images/wall1.png", 1, image_width=50, image_height=270, center_x=875, center_y=485)
        self.scene.add_sprite("Walls", wall)
        wall = arcade.Sprite("images/wall1.png", 1, image_width=50, image_height=370, center_x=1105, center_y=435)
        self.scene.add_sprite("Walls", wall)
        wall = arcade.Sprite("images/wall1.png", 1, image_width=50, image_height=270, center_x=775, center_y=325)
        self.scene.add_sprite("Walls", wall)
        wall = arcade.Sprite("images/wall1.png", 1, image_width=50, image_height=270, center_x=1005, center_y=325)
        self.scene.add_sprite("Walls", wall)
        wall = arcade.Sprite("images/wall1.png", 1, image_width=50, image_height=270, center_x=675, center_y=285)
        self.scene.add_sprite("Walls", wall)
        wall = arcade.Sprite("images/wall1.png", 1, image_width=50, image_height=270, center_x=475, center_y=385)
        self.scene.add_sprite("Walls", wall)
        wall = arcade.Sprite("images/wall1.png", 1, image_width=50, image_height=270, center_x=375, center_y=235)
        self.scene.add_sprite("Walls", wall)
        wall = arcade.Sprite("images/wall1.png", 1, image_width=50, image_height=270, center_x=275, center_y=385)
        self.scene.add_sprite("Walls", wall)
        wall = arcade.Sprite("images/rectangle.png", 1, image_width=230, image_height=50, center_x=565, center_y=395)
        self.scene.add_sprite("Walls", wall)
        wall = arcade.Sprite("images/rectangle.png", 1, image_width=530, image_height=50, center_x=915, center_y=175)
        self.scene.add_sprite("Walls", wall)
        wall = arcade.Sprite("images/rectangle.png", 1, image_width=530, image_height=50, center_x=415, center_y=545)
        self.scene.add_sprite("Walls", wall)

        # Create the physics engine and add the walls as barriers
        self.physics_engine = arcade.PhysicsEngineSimple(
            self.player_sprite, self.scene.get_sprite_list("Walls")
        )

    def on_draw(self):
        """Render the screen."""

        # Clear the screen to the background color
        self.clear()

        # Draw the start square and the full scene.
        arcade.draw_rectangle_filled(125, 125, 50, 50, arcade.color.RUBY_RED)
        self.scene.draw()


    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
        # Added a keybind to the B button to go back to home
        elif key == arcade.key.B:
            game_view = HomeView()
            self.window.show_view(game_view)

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
        # Check if the user made it to the finish
        colliding = arcade.check_for_collision(self.player_sprite, self.finish_sprite)
        if colliding:
            game_view = EndView()
            self.window.show_view(game_view)


# View for when the user wins
class EndView(arcade.View):
    def __init__(self):
        super().__init__()

        # Create and enable the UIManager
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        arcade.set_background_color(arcade.color.LIGHT_CORNFLOWER_BLUE)

        # Create button to go back to the Home screen
        play_button = arcade.gui.UIFlatButton(text="MAIN MENU", width=200)

        button_box = arcade.gui.UIBoxLayout()  # Create a box group to align the 'open' button in the center
        button_box.add(play_button)
        play_button.on_click = self.on_click_play
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center",
                align_x=0,
                anchor_y="center",
                align_y=0,

                child=play_button
            )
        )

    def on_click_play(self, event):
        game_view = HomeView()
        self.window.show_view(game_view)

    def on_draw(self):
        self.clear()
        self.manager.draw()


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Danny's Maze Game"


# Bring all the views together in the game.
def main():
    """ Main function """

    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = HomeView()
    window.show_view(start_view)
    arcade.run()


main()