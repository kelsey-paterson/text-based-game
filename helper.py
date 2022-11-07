import game_display as gdi
import pygame as pg
pg.init()


def render_text(text, x, y, fontObj):
  text_surface = fontObj.render(text, True, (0, 128, 0))
  rect = text_surface.get_rect()
  rect.centery = y
  rect.left = x
  gdi.window.blit(text_surface, rect)


def draw_box(x, y, size_x, size_y, colour, line_thickness):
  box = pg.Rect(x, y, size_x, size_y)
  pg.draw.rect(gdi.window, colour, box, line_thickness)
