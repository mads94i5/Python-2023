"""
Imagine this class as being something you 
as a programmer deals with, 
and the code in the notebook is what 
people who uses your code will see

So "library code" and "user code"

"""

class Number:
    def __init__(self, value):
        self.x = value

    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        if 0 <= value <= 100:
            self._x = value
        else:
            raise ValueError('Number should be between 0 and 100')