# Globals for the bearings
# Change the values as you see fit
EAST = 2
NORTH = 1
WEST = 4
SOUTH = 3


class Robot(object):

    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.x = x
        self.y = y

    @property
    def coordinates(self):
        return (self.x, self.y)

    def turn_right(self):
        if self.bearing == 4:
            self.bearing = 1
        else:
            self.bearing = self.bearing + 1

    def turn_left(self):
        if self.bearing == 1:
            self.bearing = 4
        else:
            self.bearing = self.bearing - 1

    def advance(self):
        if self.bearing == 1:
            self.y +=1
        elif self.bearing == 2:
            self.x +=1
        elif self.bearing == 3:
            self.y -= 1
        elif self.bearing == 4:
            self.x -= 1

    def simulate(self, string):

        for char in string:
            if char == 'L':
                self.turn_left()
            elif char == 'R':
                self.turn_right()
            elif char == 'A':
                self.advance()






