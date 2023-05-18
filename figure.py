import math

class line:
    _length = 0
    def init_(self,length):
        self._length = length
    
    def set_length(self,length):
        self._length = length
    
    def get_length(self):
        return self._length
    
    def area_square(length):
        
        return length*length
    
    def area_circle(length):
        return length*length*math.pi
    
    def area_regular_triangle(length):

        return length*length*math.sqrt(3) / 4

 
    
