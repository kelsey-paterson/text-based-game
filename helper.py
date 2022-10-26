def render_text(text, x, y) {
  text_surface = my_font.render(text, True, (0, 128, 0))
  rect = text_surface.get_rect()
  rect.centery = y
  rect.left = x
  window.blit(text_surface, rect)
}