import pyglet

# Initialize game window
game_window = pyglet.window.Window()

# Resources
pyglet.resource.path = ['../resources']
pyglet.resource.reindex()

# Load images
player_image = pyglet.resource.image('player.png')
bullet_image = pyglet.resource.image('bullet.png')
asteroid_image = pyglet.resource.image('asteroid.png')

# Center images
def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2

center_image(player_image)
center_image(bullet_image)
center_image(asteroid_image)

# Labels
score_label = pyglet.text.Label(text = "Score: 0", x = 10, y = 460)
level_label = pyglet.text.Label(text = "My Amazing Game",
                            x = game_window.width // 2, y = game_window.height // 2, anchor_x = 'center')

##################################################
# EVENTS
@game_window.event
def on_draw():
	game_window.clear()
	
	level_label.draw()
	score_label.draw()

##################################################

if __name__ == '__main__':
	pyglet.app.run()
