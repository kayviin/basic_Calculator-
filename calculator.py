import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the display
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Calculator')

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
LIGHT_GRAY = (200, 200, 200)

# Create button class
class Button:
    def __init__(self, text, pos, size, bg=LIGHT_GRAY, feedback=""):
        self.rect = pygame.Rect(pos, size)
        self.bg = bg
        self.feedback = feedback
        self.text = text
        self.text_color = BLACK
        self.font = pygame.font.SysFont(None, 36)  # Adjust the font size as needed

    def draw(self):
        pygame.draw.rect(screen, self.bg, self.rect)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            return self.feedback
        return ""

# Create buttons
buttons = [
    Button("7", (10, 100), (80, 60), feedback="7"),
    Button("8", (100, 100), (80, 60), feedback="8"),
    Button("9", (190, 100), (80, 60), feedback="9"),
    Button("/", (280, 100), (80, 60), feedback="/"),

    Button("4", (10, 170), (80, 60), feedback="4"),
    Button("5", (100, 170), (80, 60), feedback="5"),
    Button("6", (190, 170), (80, 60), feedback="6"),
    Button("*", (280, 170), (80, 60), feedback="*"),

    Button("1", (10, 240), (80, 60), feedback="1"),
    Button("2", (100, 240), (80, 60), feedback="2"),
    Button("3", (190, 240), (80, 60), feedback="3"),
    Button("-", (280, 240), (80, 60), feedback="-"),

    Button("0", (10, 310), (80, 60), feedback="0"),
    Button(".", (100, 310), (80, 60), feedback="."),
    Button("=", (190, 310), (80, 60), bg=GRAY, feedback="="),
    Button("+", (280, 310), (80, 60), feedback="+"),

    Button("sqrt", (10, 380), (120, 60), feedback="sqrt"),
    Button("x^2", (160, 380), (120, 60), feedback="^2"),

    Button("Clear", (10, 450), (120, 40), bg=GRAY, feedback="clear"),
    Button("Delete", (160, 450), (120, 40), bg=GRAY, feedback="delete"),
]

# Clear display
display = ""
operator = ""
first_num = ""

# Main loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        for button in buttons:
            feedback = button.click(event)
            if feedback:
                if feedback == "=":
                    if operator == "+":
                        display = str(float(first_num) + float(display))
                    elif operator == "-":
                        display = str(float(first_num) - float(display))
                    elif operator == "*":
                        display = str(float(first_num) * float(display))
                    elif operator == "/":
                        if float(display) != 0:
                            display = str(float(first_num) / float(display))
                        else:
                            display = "Error"
                    operator = ""
                    first_num = ""
                elif feedback in ["+", "-", "*", "/"]:
                    operator = feedback
                    first_num = display
                    display = ""
                elif feedback == "sqrt":
                    if display:
                        display = str(math.sqrt(float(display)))
                elif feedback == "^2":
                    if display:
                        display = str(float(display) ** 2)
                elif feedback == "clear":
                    display = ""
                    operator = ""
                    first_num = ""
                elif feedback == "delete":
                    display = display[:-1]
                else:
                    display += feedback

    # Update display
    screen.fill(WHITE)

    text_surface = pygame.font.SysFont(None, 48).render(display, True, BLACK)
    screen.blit(text_surface, (20, 20))

    for button in buttons:
        button.draw()

    pygame.display.flip()

pygame.quit()