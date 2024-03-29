import pygame
import camera_class

# this class is used to render the game
class Render_manager:

    def __init__(self, game):
        self.game = game

    # takes the active level and renders it TODO: add a ability to render multible levels at once
    def render(self):
        render_data = self.game.level_manager.active_levels
        if self.game.camera_manager.mode == camera_class.Camera_mode.dynamic or self.game.camera_manager.mode == camera_class.Camera_mode.level:
            self.game.__SURFACE__.fill((0, 0, 0))
        for i in render_data:
            if i.level_data["Data"]["BackgroundTransparent"] is True:
                i.screen.fill((0, 0, 0, 0))

        for i in render_data:
            sorted_layers = sorted(i.loaded_objects.keys())
            for j in sorted_layers:
                for k in i.loaded_objects[j]:
                    k.draw(self.game)
            self.game.__SURFACE__.blit(i.screen, (i._x, i._y))

        self.game.delta_time = self.game.__clock__.tick() / 1000
        pygame.display.update()
