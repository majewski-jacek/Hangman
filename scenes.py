from textwrap import dedent
from sys import exit
from data_handler import DataHandler as DH


class Scenes(object):

    @staticmethod    
    def display_opening():
        print(dedent("""
                    Witaj w grze pt. "Hangman"!
                    Jeśli chcesz zagrać wpisz cokolwiek, a jeśli chcesz zobaczyć zasady wpisz 1.
                    """))
        
        choice = input("> ")
        return choice

    @staticmethod
    def display_instructions():
        print(dedent("""
                    Zasady:
                    1. Musisz odgadnąć zaszyfrowane hasło
                    2. Jeśli odgadniesz literę to '_' zamieni się w daną literę.
                    3. Podawaj tylko 1 małą literę!
                    """))

        input("Aby zacząć grę naciśnij cokolwiek ")

    @staticmethod
    def display_available_riddles():
        print("\nDostępne zagadki:")
        riddles = [riddle for riddle in DH.__dict__ if not riddle.startswith("__")]
        i = 1
        for riddle in riddles:
            print(f"{i}. {riddle}")
            i += 1

        while True:
            try:
                choice = input("\nWybierz numer zagadki jaki chcesz zagrać.\n> ")
                return "DH()." + riddles[int(choice) - 1]
            
            except:
                print("Podaj poprawną liczbę")

    @staticmethod
    def display_difficulty():
        print(dedent("""
                    Wybierz numer poziomu trudności:
                    1. Łatwy
                    2. Normalny
                    3. Trudny
                    4. Ekstremalny
                    """))    
        
        difficulty = {"1": 15, "2": 10, "3": 7, "4": 3}

        while True:
            choice = input("> ")
            if difficulty.get(choice, False):
                return difficulty.get(choice) 

            print("Podaj poprawną liczbę")

    @staticmethod
    def display_riddle_status(riddle, live, letters):
        print(dedent(f"""
                    {''.join(riddle)}
                    Pozostałe życia: {live}
                    Użyte litery: {', '.join(letters)} 
                    """))
    
    @staticmethod
    def victory_scene(word):
        print(dedent(f"""
                    Gratulacje, udało Ci się odgadnąć hasło !!!
                    Poprawne hasło -> {word}
                    """))
        exit(0)

    @staticmethod
    def defeat_scene(word):
        print(dedent(f"""
                    Niestety, nie udało Ci się odgadnąć hasła.
                    Poprawne hasło -> {word}
                    """))
        exit(0)
