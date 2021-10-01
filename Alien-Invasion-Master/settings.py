class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5
#for bullets
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
# Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
# Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

# fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1