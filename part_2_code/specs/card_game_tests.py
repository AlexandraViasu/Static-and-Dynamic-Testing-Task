import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.cardgame = CardGame()
        self.card1 = Card("spades", 1)
        self.card2 = Card("hearts", 3)


    def test_check_for_ace(self):
        self.assertEqual(True, self.cardgame.check_for_ace(self.card1))

    def test_check_for_ace_false(self):
        self.assertEqual(False, self.cardgame.check_for_ace(self.card2))

    def test_highest_card_first_card_higher(self):
        self.assertEqual(self.card2, self.cardgame.highest_card(self.card1, self.card2))

    def test_highest_card_second_card_higher(self):
        self.assertEqual(self.card2, self.cardgame.highest_card(self.card2, self.card1))
    
    def test_cards_total(self):
        cards = [self.card1, self.card2]
        self.assertEqual("You have a total of 4", self.cardgame.cards_total(cards))
    
    def test_cards_total_no_cards(self):
        cards = []
        self.assertEqual("You have a total of 0", self.cardgame.cards_total(cards))
    

                         

    