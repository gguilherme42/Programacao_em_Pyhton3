import math

class Point:
    def __init__(self, x: float=0, y: float=0):
        self.x = x
        self.y = y
    
    @property
    def distance_from_origin(self) -> float:
        return math.hypot(self.x, self.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __repr__(self):
        return f"Point({self.x!r}, {self.y!r})"
    
    def __str__(self):
        return f"({self.x!r}, {self.y!r})"
     

class Circle(Point):
    def __init__(self, radius: float, x: float=0, y: float=0):
        super().__init__(x, y)
        self.radius = radius
    
    @property
    def radius(self):
        """The circle's radius

        >>> circle = Circle(-2)
        Traceback (most recent call last):
        ...
        AssertionError: radius must be nonzero and non-negative
        >>> circle = Circle(4)
        >>> circle.radius = -1
        Traceback (most recent call last):
        ...
        AssertionError: radius must be nonzero and non-negative
        >>> circle.radius = 6
        """
        return self.__radius
    
    @radius.setter
    def radius(self, radius):
        assert radius > 0, "radius must be nonzero and non-negative"
        self.__radius = radius
    

    @property
    def edge_distance_from_origin(self):
        return abs(self.distance_from_origin - self.radius)
    
    @property
    def area(self):
        return math.pi * (self.radius ** 2)
    
    @property
    def circumference(self):
        return 2 * math.pi * self.radius
    
    def __eq__(self, other):
        return self.radius == other.radius and super().__eq__(other)
    
    
    def __repr__(self):
        return f"Circle({self.radius!r}, {self.x!r}, {self.y!r})"
    

    def __str__(self):
        return repr(self)
    