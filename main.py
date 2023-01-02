from data_handler import DataHandler as DH
from hangman import HangmanLogic as HL
from scenes import Scenes
import riddle as riddles


def main(): 
    scene = Scenes()
    hangLogic = HL()

    opening_choice = scene.display_opening()

    if opening_choice == '1':
        scene.display_instructions()
    
    choice_riddle = scene.display_available_riddles()
    choice_difficulty = scene.display_difficulty()

    riddle = riddles.Riddle(eval(choice_riddle), choice_difficulty)
    riddle.create_riddle_status()
    while riddle.life > 0:
        if "".join(riddle.riddle_status) == riddle.word:
            scene.victory_scene(riddle.word)
        
        scene.display_riddle_status(riddle.riddle_status, riddle.life, riddle.guessed_letters)
        guess_letter = input("Podaj literę: ")
        condition = hangLogic.condition_letter(guess_letter, riddle.guessed_letters)

        if not condition:
            riddle.guessed_letters.append(guess_letter)
            guessed = hangLogic.guessing(riddle.riddle, guess_letter)

            if guessed:
                riddle.change_guess_riddle(guessed)
            
            else:
                riddle.life -= 1
        
        else:
            print(f"\n{condition}")
    
    scene.defeat_scene(riddle.word)


if __name__ == '__main__':
    main()