from random import choice


class Riddle(object):

    def __init__(self, riddles, life):
        self.word = choice(riddles)
        self.life = life
        self.riddle_status = []
        self.guessed_letters = []
        self.riddle = self.word.replace("'", " ").lower()

    # some character names contain spaces or quotation marks    
    def create_riddle_status(self):
        for letter in self.word:
            if letter == ' ':
                self.riddle_status.append(' ')
            elif letter == "'":
                self.riddle_status.append("'")
            else:
                self.riddle_status.append('_')

    def change_guess_riddle(self, list):
        for index in list:
            self.riddle_status[index] = self.word[index]
            