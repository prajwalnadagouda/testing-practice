import unittest

from taste import Taste
from taste import Status

class TestLikeFunction(unittest.TestCase):
    def test_like1(self):
        self.assertIs(Taste.sequence("l"),Status.LIKE)

    def test_like2(self):
        self.assertIs(Taste.sequence("ll"),Status.NEUTRAL)
    
    def test_like3(self):
        self.assertIs(Taste.sequence("ld"),Status.DISLIKE)
    
    def test_like4(self):
        self.assertIs(Taste.sequence("lll"),Status.LIKE)
    
    def test_like5(self):
        self.assertIs(Taste.sequence("ldl"),Status.LIKE)
    
    def test_like6(self):
        self.assertIs(Taste.sequence("ldd"),Status.NEUTRAL)


class TestDislikeFunction(unittest.TestCase):
    def test_dislike1(self):
        self.assertIs(Taste.sequence("d"),Status.DISLIKE)
    
    def test_dislike2(self):
        self.assertIs(Taste.sequence("dl"),Status.LIKE)
    
    def test_dislike3(self):
        self.assertIs(Taste.sequence("dd"),Status.NEUTRAL)
    
    def test_dislike4(self):
        self.assertIs(Taste.sequence("ddd"),Status.DISLIKE)

    def test_dislike5(self):
        self.assertIs(Taste.sequence("dld"),Status.DISLIKE)

    def test_dislike6(self):
        self.assertIs(Taste.sequence("dll"),Status.NEUTRAL)
    
    

if __name__ == "__main__":
    unittest.main()