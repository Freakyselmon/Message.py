from colorama import Fore, Style
import random


def print_colorful_birthday_with_hearts(message, font_size=100, colors=[Fore.RED, Fore.GREEN, Fore.BLUE]):
    message = message.upper()

    heart_symbols = ['❤️', '💙', '💚', '💛', '💜', '🧡']

    for i in range(font_size):
        line = ""
        for char in message:
            if char.isalpha():
                color = random.choice(colors)
                line += f"{color}{char} "
            elif char.isspace():
                line += "  "
            else:
                heart = random.choice(heart_symbols)
                line += f"{Fore.RESET}{heart} "
        print(line.center(len(message) * 4))


# Example usage:
print_colorful_birthday_with_hearts("I LOVE YOU 🧡 ", font_size=100, colors=[Fore.RED, Fore.GREEN, Fore.BLUE])
