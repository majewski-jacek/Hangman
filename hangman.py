import string


class HangmanLogic(object):
    
    # returns a list with the indices of the guessed characters
    @staticmethod
    def guessing(riddle, guessing_letter):
        return [num for num, letter in list(enumerate(riddle)) if guessing_letter == letter]

    @staticmethod
    def condition_letter(letter, guessed_letters):

        conditions = {
                    letter in guessed_letters: "Nie używaj tych samych liter!",
                    not letter in string.ascii_letters: "Musisz podać jakąś małą literę z angielskiego alfabetu!",
                    letter == letter.upper(): "Nie używaj dużych liter!",                                   
                    not letter.isalpha(): "Nie używaj specjalnych znaków oraz cyfr!",
                    len(letter) != 1: "Musisz podać tylko 1 małą literę!"
                    }

        for cond, msg in conditions.items():
            if cond:
                return msg
       
        return False