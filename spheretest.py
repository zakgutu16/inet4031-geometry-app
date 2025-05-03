import unittest
import sphere

class sphereTest(unittest.TestCase):

    #these need to be updated for a sphere
    def test_volume1(self):
        assert(round(sphere.volume(1), 5) == 4.18879)

    def test_volume2(self):
        assert(round(sphere.volume(3), 5) == 113.09734)

    def test_volume3(self):
        assert(round(sphere.volume(5), 5) == 523.59878)

    #failing test
    #def test_volume3(self):
        #assert(sphere.volume(10,1000) == ??)

if __name__ == '__main__':
    unittest.main()
