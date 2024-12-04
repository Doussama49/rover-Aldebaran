import unittest
from rover import Rover

class TestRover(unittest.TestCase):

    def setUp(self):
        self.rover = Rover()

    def assertPosition(self, x, y, direction):
        self.assertEqual(self.rover.get_position(), (x, y, direction))

    def test_initial_calibration(self):
        self.rover.calibrate(5, 5)
        self.assertPosition(5, 5, 'North')

    def test_going_north(self):
        self.rover.x, self.rover.y, self.rover.direction = 0, 0, 'North'
        self.rover.move_forward()
        self.assertPosition(0, 1, 'North')

    def test_going_south(self):
        self.rover.x, self.rover.y, self.rover.direction = 0, 0, 'North'
        self.rover.move_backward()
        self.assertPosition(0, -1, 'North')

    def test_turning_left(self):
        self.rover.x, self.rover.y, self.rover.direction = 9, 9, 'East'
        self.rover.turn_left()
        self.assertPosition(9, 9, 'North')

    def test_turning_right(self):
        self.rover.x, self.rover.y, self.rover.direction = 5, 5, 'South'
        self.rover.turn_right()
        self.assertPosition(5, 5, 'West')

    def test_turning_right_and_going_forward(self):
        self.rover.x, self.rover.y, self.rover.direction = 3, 3, 'North'
        self.rover.turn_right()
        self.rover.move_forward()
        self.assertPosition(4, 3, 'East')
    

    def test_commands_recieved(self):
        self.rover.x, self.rover.y, self.rover.direction = 0, 0,  'North'
        self.rover.set_orders(['f', 'f', 'l'])
        self.rover.apply_order()
        self.assertPosition(0,2, 'West')

if __name__ == '__main__':
    unittest.main()
