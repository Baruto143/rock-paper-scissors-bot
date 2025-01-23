import unittest
from RPS import player

class TestPlayerFunction(unittest.TestCase):

    def test_first_move(self):
        # Test the first move (should be random)
        first_move = player("", [])
        self.assertIn(first_move, ["R", "P", "S"])

    def test_counter_rock(self):
        # Test the case where opponent played "R", so our bot should play "P"
        move = player("R", [])
        self.assertEqual(move, "P")

    def test_counter_paper(self):
        # Test the case where opponent played "P", so our bot should play "S"
        move = player("P", [])
        self.assertEqual(move, "S")

    def test_counter_scissors(self):
        # Test the case where opponent played "S", so our bot should play "R"
        move = player("S", [])
        self.assertEqual(move, "R")

if __name__ == "__main__":
    unittest.main()

