import pygame
import sys

# Initialisierung von Pygame
pygame.init()

# Fenstergröße und -titel
width, height = 850, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Stack Visualization")

# Farben
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_GRAY = (211, 211, 211)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Schriftart und -größe
font = pygame.font.SysFont(None, 24)
limit = 6

# Klasse für den Stack
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        if len(self.stack) < limit:
            self.stack.append(value)  # Am Ende der Liste einfügen
        else:
            print("Limit erreicht!")

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()  # Vom Ende der Liste entfernen
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def get_stack(self):
        return self.stack

# Funktion zum Zeichnen des Stacks
def draw_stack(stack):
    screen.fill(WHITE)
    rect_width = 110
    rect_height = 50
    padding = 20

    for i, value in enumerate(stack):
        x = width // 2 - rect_width // 2
        y = height - (i + 1) * (rect_height + padding)

        # Zeichnen des Rechtecks
        pygame.draw.rect(screen, GRAY, (x, y, rect_width, rect_height))
        
        # Zeichnen des Trennstrichs (senkrecht)
        pygame.draw.line(screen, BLACK, (x + rect_width // 2, y), (x + rect_width // 2, y + rect_height), 2)
        
        # Zeichnen des Indexes und Wertes
        index_text = font.render(str(i), True, BLACK)
        value_text = font.render(str(value), True, BLACK)
        screen.blit(index_text, (x + 10, y + rect_height // 2 - index_text.get_height() // 2))
        screen.blit(value_text, (x + rect_width - value_text.get_width() - 10, y + rect_height // 2 - value_text.get_height() // 2))

    if stack:  # Zeiger für den obersten Wert hinzufügen
        top_x = width // 2 + rect_width // 2 + 10
        top_y = height - (len(stack)) * (rect_height + padding) + rect_height // 2
        arrow_offset = 10

        # Zeichnen des Zeigers für den obersten Wert
        pygame.draw.polygon(screen, GREEN, [(top_x + arrow_offset, top_y + 10),
                                          (top_x, top_y),
                                          (top_x + arrow_offset, top_y - 10)])
        top_text = font.render("Top", True, GREEN)
        screen.blit(top_text, (top_x + 15, top_y - arrow_offset - 10))

# Funktion zum Zeichnen des Eingabefeldes und der Buttons
def draw_ui(input_text):
    # Eingabefeld
    input_rect = pygame.Rect(150, 50, 140, 32)
    pygame.draw.rect(screen, LIGHT_GRAY, input_rect)
    text_surface = font.render(input_text, True, BLACK)
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
    input_rect.w = max(100, text_surface.get_width() + 10)

    # Push Button
    push_button = pygame.Rect(300, 50, 100, 32)
    pygame.draw.rect(screen, BLUE, push_button)
    push_text = font.render("Push", True, WHITE)
    screen.blit(push_text, (push_button.x + 5, push_button.y + 5))

    # Pop Button
    pop_button = pygame.Rect(450, 50, 100, 32)
    pygame.draw.rect(screen, BLUE, pop_button)
    pop_text = font.render("Pop", True, WHITE)
    screen.blit(pop_text, (pop_button.x + 5, pop_button.y + 5))

    # Hinweis Feld
    hinweis_feld = pygame.Rect(650, 50, 100, 32)
    pygame.draw.rect(screen, BLACK, hinweis_feld)
    hinweis_text = font.render("Limit: " + str(limit), True, WHITE)
    screen.blit(hinweis_text, (hinweis_feld.x + 5, hinweis_feld.y + 5))

    return input_rect, push_button, pop_button

# Hauptprogramm
def main():
    stack = Stack()
    running = True
    input_active = False
    input_text = ''

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    input_active = True
                else:
                    input_active = False
                if push_button.collidepoint(event.pos):
                    if input_text.isdigit():
                        stack.push(int(input_text))
                        input_text = ''
                if pop_button.collidepoint(event.pos):
                    stack.pop()
            if event.type == pygame.KEYDOWN:
                if input_active:
                    if event.key == pygame.K_RETURN:
                        if input_text.isdigit():
                            stack.push(int(input_text))
                            input_text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode

        draw_stack(stack.get_stack())
        input_rect, push_button, pop_button = draw_ui(input_text)
        pygame.display.flip()

if __name__ == "__main__":
    main()
