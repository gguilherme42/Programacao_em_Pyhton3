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
    
    
    def __add__(self, other):
        """
        >>> p = Point(1, 1)
        >>> q = Point(2, 2)
        >>> r = Point(3,3)
        >>> p = q + r
        >>> p
        Point(5, 5)
        >>> p = r + 2
        Traceback (most recent call last):
        ...
        AssertionError: can't add non-Point object
        """
        assert isinstance(other, Point), "can't add non-Point object"
        return Point((self.x + other.x), (self.y + other.y))


    def __iadd__(self, other):
        """
        >>> p = Point(1, 1)
        >>> q = Point(2, 2)
        >>> p += q
        >>> p
        Point(3, 3)
        >>> p += 2
        Traceback (most recent call last):
        ...
        AssertionError: can't add non-Point object
        """
        assert isinstance(other, Point), "can't add non-Point object"
        return self + other
    

    def __sub__(self, other):
        """
        >>> p = Point(1, 1)
        >>> q = Point(2, 2)
        >>> r = Point(3,3)
        >>> p = q - r
        >>> p
        Point(-1, -1)
        >>> p = r - 2
        Traceback (most recent call last):
        ...
        AssertionError: can't sub non-Point object
        """
        assert isinstance(other, Point), "can't sub non-Point object"
        return Point((self.x - other.x), (self.y - other.y))
        
    def __isub__(self, other):
        """
        >>> p = Point(1, 1)
        >>> q = Point(2, 2)
        >>> p -= q
        >>> p
        Point(-1, -1)
        >>> p -= 2
        Traceback (most recent call last):
        ...
        AssertionError: can't sub non-Point object
        """
        assert isinstance(other, Point), "can't sub non-Point object"
        return self - other
    
    def __mul__(self, number):
        """
        >>> p = Point(1,1)
        >>> q = Point(2,2)
        >>> n = 5
        >>> p = q * n
        >>> p
        Point(10, 10)
        >>> p = p * q
        Traceback (most recent call last):
        ...
        AssertionError: can't multiply non-number object
        """
        assert isinstance(number, float) or isinstance(number, int), "can't multiply non-number object"
        return Point((self.x * number), (self.y * number))
    

    def __imul__(self, number):
        """
        >>> p = Point(2,2)
        >>> n = 5
        >>> p *= n
        >>> p
        Point(10, 10)
        >>> p *= p
        Traceback (most recent call last):
        ...
        AssertionError: can't multiply  by a non-number object
        """
        assert isinstance(number, float) or isinstance(number, int), "can't multiply  by a non-number object"
        return self * number
    
    def __truediv__(self, number):
        """
        >>> p = Point(1,1)
        >>> q = Point(2,2)
        >>> n = 2
        >>> p = q / n
        >>> p
        Point(1.0, 1.0)
        >>> p = p / q
        Traceback (most recent call last):
        ...
        AssertionError: can't divide by a non-number object
        """
        assert isinstance(number, float) or isinstance(number, int), "can't divide by a non-number object"
        return Point((self.x / number), (self.y / number))
    

    def __itruediv__(self, number):
        """
        >>> p = Point(2,2)
        >>> n = 2
        >>> p /= n
        >>> p
        Point(1.0, 1.0)
        >>> p /= p
        Traceback (most recent call last):
        ...
        AssertionError: can't divide by a non-number object
        """
        assert isinstance(number, float) or isinstance(number, int), "can't divide by a non-number object"
        return self / number
    

    def __floordiv__(self, number):
        """
        >>> p = Point(1,1)
        >>> q = Point(2,2)
        >>> n = 2
        >>> p = q // n
        >>> p
        Point(1, 1)
        >>> p = p // q
        Traceback (most recent call last):
        ...
        AssertionError: can't divide by a non-number object
        """
        assert isinstance(number, float) or isinstance(number, int), "can't divide by a non-number object"
        return Point((self.x // number), (self.y // number))

    def __ifloordiv__(self, number):
        """
        >>> p = Point(2,2)
        >>> n = 2
        >>> p //= n
        >>> p
        Point(1, 1)
        >>> p //= p
        Traceback (most recent call last):
        ...
        AssertionError: can't divide by a non-number object
        """
        
        assert isinstance(number, float) or isinstance(number, int), "can't divide by a non-number object"
        return self // number

    
    def __repr__(self):
        return f"Point({self.x!r}, {self.y!r})"
    
    def __str__(self):
        return f"({self.x!r}, {self.y!r})"


if __name__ == "__main__":
    import doctest
    doctest.testmod()