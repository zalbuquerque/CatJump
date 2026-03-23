import pygame


class AssetManager:
    @staticmethod
    def image(path, size=None):
        image = pygame.image.load(path).convert_alpha()
        if size is not None:
            image = pygame.transform.scale(image, size)
        return image

    @staticmethod
    def sound(path):
        return pygame.mixer.Sound(path)