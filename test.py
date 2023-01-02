import unittest
import riddle
import hangman


class TestRiddle(unittest.TestCase):

    def setUp(self):
        self.lol_obj = riddle.Riddle(["Test' s"], 10)
        self.lol_obj.create_riddle_status()

    def test_init(self):
        self.assertEqual(self.lol_obj.word, "Test' s")
        self.assertEqual(self.lol_obj.riddle, "test  s")
    
    def test_create_riddle_status(self):
        self.assertEqual(self.lol_obj.riddle_status, ["_", "_", "_", "_", "'", " ", "_"])

    def test_change_guess_riddle(self):
        self.lol_obj.change_guess_riddle([2, 6])
        self.assertEqual(self.lol_obj.riddle_status, ["_", "_", "s", "_", "'", " ", "s"])

        self.lol_obj.change_guess_riddle([0, 3])
        self.assertEqual(self.lol_obj.riddle_status, ["T", "_", "s", "t", "'", " ", "s"])


class TestHangmanLogic(unittest.TestCase):

    def setUp(self):
        self.hangLogic = hangman.HangmanLogic()
        self.condition = self.hangLogic.condition_letter 

    def test_guessing(self):
        guessed_1 = self.hangLogic.guessing("test  s", "s")
        self.assertEqual(guessed_1, [2, 6])

    def test_conditions(self):
        guessed_letters = ['a', 'b']

        self.assertEqual(self.condition("B", guessed_letters), 
                                        "Nie używaj dużych liter!")
        
        self.assertEqual(self.condition("b", guessed_letters), 
                                        "Nie używaj tych samych liter!")
        
        self.assertEqual(self.condition("0", guessed_letters), 
                                        "Nie używaj specjalnych znaków oraz cyfr!")
        
        self.assertEqual(self.condition("", guessed_letters), 
                                        "Musisz podać tylko 1 małą literę!")
        
        self.assertEqual(self.condition("asd", guessed_letters), 
                                        "Musisz podać tylko 1 małą literę!")
        
        self.assertEqual(self.condition("ę", guessed_letters), 
                                        "Musisz podać jakąś małą literę z angielskiego alfabetu!")


if __name__ == "__main__":
    unittest.main()