from __future__ import annotations

from pathlib import Path
import pygame


def load_image(path: str | Path, size: tuple[int, int] | None = None, alpha: bool = True) -> pygame.Surface:
    file_path = Path(path)
    surface = pygame.image.load(str(file_path))
    surface = surface.convert_alpha() if alpha else surface.convert()
    if size is not None:
        surface = pygame.transform.smoothscale(surface, size)
    return surface
