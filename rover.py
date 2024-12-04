class Rover:
    def __init__(self, x=0, y=0, direction='North'):
        self.x = x
        self.y = y
        self.direction = direction
        self.order_list = []

    def calibrate(self, x, y):
        self.x = x
        self.y = y
        self.direction = 'North'
    
    def set_orders(self, order_list):
        self.order_list = order_list

    def apply_order(self):
        for order in self.order_list:
            match order:
                case 'f':
                    self.move_forward()
                case 'b':
                    self.move_backward()
                case 'l': 
                    self.turn_left()
                case 'r':
                    self.turn_right()

        self.set_orders([])

    def move_forward(self):
        if self.direction == 'North':
            self.y += 1
        elif self.direction == 'South':
            self.y -= 1
        elif self.direction == 'East':
            self.x += 1
        elif self.direction == 'West':
            self.x -= 1

    def move_backward(self):
        if self.direction == 'North':
            self.y -= 1
        elif self.direction == 'South':
            self.y += 1
        elif self.direction == 'East':
            self.x -= 1
        elif self.direction == 'West':
            self.x += 1

    def turn_left(self):
        directions = ['North', 'West', 'South', 'East']
        self.direction = directions[(directions.index(self.direction) + 1) % 4]

    def turn_right(self):
        directions = ['North', 'East', 'South', 'West']
        self.direction = directions[(directions.index(self.direction) + 1) % 4]

    def get_position(self):
        return self.x, self.y, self.direction
