import pygame
import sys

# Initialisierung von Pygame
pygame.init()

# Fenstergröße und -titel
width, height = 850, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Queue Visualization")

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
limit = 10

# Klasse für die Queue
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        if len(self.queue) < limit:
            self.queue.append(value)  # Am Ende der Liste einfügen
        else:
            print("Limit erreicht !")

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)  # Vom Anfang der Liste entfernen
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def get_queue(self):
        return self.queue

# Funktion zum Zeichnen der Queue
def draw_queue(queue):
    screen.fill(WHITE)
    rect_width = 60
    rect_height = 100
    padding = 20

    for i, value in enumerate(queue):
        x = i * (rect_width + padding) + padding
        y = height // 2 - rect_height // 2

        # Zeichnen des Rechtecks
        pygame.draw.rect(screen, GRAY, (x, y, rect_width, rect_height))
        pygame.draw.line(screen, BLACK, (x, y + rect_height // 2), (x + rect_width, y + rect_height // 2), 2)

        # Zeichnen des Indexes und Wertes
        index_text = font.render(str(i), True, BLACK)
        value_text = font.render(str(value), True, BLACK)
        screen.blit(index_text, (x + rect_width // 2 - index_text.get_width() // 2, y + rect_height // 4 - index_text.get_height() // 2))
        screen.blit(value_text, (x + rect_width // 2 - value_text.get_width() // 2, y + 3 * rect_height // 4 - value_text.get_height() // 2))

    if queue:  # Zeiger für "Kopf" und "Ende" hinzufügen
        head_x = padding
        end_x = (len(queue) - 1) * (rect_width + padding) + padding
        arrow_offset = 10

        # Zeichnen des Kopfzeigers
        pygame.draw.polygon(screen, GREEN, [(head_x + rect_width // 2, y - arrow_offset),
                                            (head_x + rect_width // 2 - arrow_offset, y - arrow_offset - 10),
                                            (head_x + rect_width // 2 + arrow_offset, y - arrow_offset - 10)])
        head_text = font.render("Kopf", True, GREEN)
        screen.blit(head_text, (head_x + rect_width // 2 - head_text.get_width() // 2, y - arrow_offset - 30))

        # Zeichnen des Endzeigers
        pygame.draw.polygon(screen, RED, [(end_x + rect_width // 2, y + rect_height + arrow_offset),
                                          (end_x + rect_width // 2 - arrow_offset, y + rect_height + arrow_offset + 10),
                                          (end_x + rect_width // 2 + arrow_offset, y + rect_height + arrow_offset + 10)])
        end_text = font.render("Ende", True, RED)
        screen.blit(end_text, (end_x + rect_width // 2 - end_text.get_width() // 2, y + rect_height + arrow_offset + 15))

# Funktion zum Zeichnen des Eingabefeldes und der Buttons
def draw_ui(input_text):
    # Eingabefeld
    input_rect = pygame.Rect(150, 50, 140, 32)
    pygame.draw.rect(screen, LIGHT_GRAY, input_rect)
    text_surface = font.render(input_text, True, BLACK)
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
    input_rect.w = max(100, text_surface.get_width() + 10)

    # Enqueue Button
    enqueue_button = pygame.Rect(300, 50, 100, 32)
    pygame.draw.rect(screen, BLUE, enqueue_button)
    enqueue_text = font.render("Enqueue", True, WHITE)
    screen.blit(enqueue_text, (enqueue_button.x + 5, enqueue_button.y + 5))

    # Dequeue Button
    dequeue_button = pygame.Rect(450, 50, 100, 32)
    pygame.draw.rect(screen, BLUE, dequeue_button)
    dequeue_text = font.render("Dequeue", True, WHITE)
    screen.blit(dequeue_text, (dequeue_button.x + 5, dequeue_button.y + 5))

    # Hinweis Feld
    hinweis_feld = pygame.Rect(650, 50, 100, 32)
    pygame.draw.rect(screen, BLACK, hinweis_feld)
    hinweis_text = font.render("Limit: " + str(limit), True, WHITE)
    screen.blit(hinweis_text, (hinweis_feld.x + 5, hinweis_feld.y + 5))

    return input_rect, enqueue_button, dequeue_button

# Hauptprogramm
def main():
    queue = Queue()
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
                if enqueue_button.collidepoint(event.pos):
                    if input_text.isdigit():
                        queue.enqueue(int(input_text))
                        input_text = ''
                if dequeue_button.collidepoint(event.pos):
                    queue.dequeue()
            if event.type == pygame.KEYDOWN:
                if input_active:
                    if event.key == pygame.K_RETURN:
                        if input_text.isdigit():
                            queue.enqueue(int(input_text))
                            input_text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode

        draw_queue(queue.get_queue())
        input_rect, enqueue_button, dequeue_button = draw_ui(input_text)
        pygame.display.flip()

if __name__ == "__main__":
    main()
