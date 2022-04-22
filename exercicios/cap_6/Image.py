import os
import pickle



class ImageError(Exception): pass
class CoordinateError(ImageError): pass
class LoadError(ImageError): pass
class SaveError(ImageError): pass
class ExportError(ImageError): pass
class NoFileNameError(ImageError): pass

class Image:
    """
>>> import os
>>> import tempfile
>>> red = "#FF0000"
>>> blue = "#0000FF"
>>> img = os.path.join(tempfile.gettempdir(), "test.img")
>>> xpm = os.path.join(tempfile.gettempdir(), "test.xpm")
>>> image = Image(10, 8, img)
>>> for x, y in ((0, 0), (0, 7), (1, 0), (1, 1), (1, 6), (1, 7), (2, 1),
...             (2, 2), (2, 5), (2, 6), (2, 7), (3, 2), (3, 3), (3, 4),
...             (3, 5), (3, 6), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4),
...             (5, 5), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (7, 1),
...             (7, 2), (7, 5), (7, 6), (7, 7), (8, 0), (8, 1), (8, 6),
...             (8, 7), (9, 0), (9, 7)):
...    image[(x, y)] = blue
>>> for x, y in ((3, 1), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2),
...             (6, 1)):
...    image[x, y] = red
>>> print(image.width, image.height, len(image.colors), image.background)
10 8 3 #FFFFFF
>>> border_color = "#FF0000" # red
>>> square_color = "#0000FF" # blue
>>> width, height = 240, 60
>>> midx, midy = width // 2, height // 2
>>> image = Image(width, height, img, "#F0F0F0")
>>> for x in range(width):
...     for y in range(height):
...         if x < 5 or x >= width - 5 or y < 5 or y >= height -5:
...             image[x, y] = border_color
...         elif midx - 20 < x < midx + 20 and midy - 20 < y < midy + 20:
...             image[x, y] = square_color
>>> print(image.width, image.height, len(image.colors), image.background)
240 60 3 #F0F0F0
>>> image.save()
>>> newimage = Image(1, 1, img)
>>> newimage.load()
>>> print(newimage.width, newimage.height, len(newimage.colors), newimage.background)
240 60 3 #F0F0F0
>>> image.export(xpm)
>>> image.thing
Traceback (most recent call last):
...
AttributeError: 'Image' object has no attribute 'thing'
>>> for name in (img, xpm):
...     try:
...         os.remove(name)
...     except EnvironmentError:
...         pass
"""
    def __init__(self, width: int, height: int, filename: str="", background: str="#FFFFFF"):
        self.filename = filename
        self.__background = background
        self.__data = {}
        self.__width = width
        self.__height = height
        self.__colors = {self.__background}


    @property
    def background(self):
        return self.__background
    
    @property
    def width(self):
        return self.__width
    
    @property
    def height(self):
        return self.__height
    
    @property
    def colors(self):
        return self.__colors
    
    
    def __getitem__(self, coordinate: tuple):
        assert len(coordinate) == 2, "coordinate should be a 2-tuple"

        if not(0 <= coordinate[0] < self.width) or \
        not(0 <= coordinate[1] < self.height):
            raise CoordinateError(str(coordinate))

        return self.__data.get(tuple(coordinate), self.__background)


    def __setitem__(self, coordinate: tuple, color: str):
        assert len(coordinate) == 2, "coordinate should be a 2-tuple"

        if not(0 <= coordinate[0] < self.width) or \
        not(0 <= coordinate[1] < self.height):
            raise CoordinateError(str(coordinate))

        if color == self.__background:
            self.__data.pop(tuple(coordinate), None)
        else:
            self.__data[tuple(coordinate)] = color
            self.__colors.add(color)
    
    def __delitem__(self, coordinate: tuple):
        assert len(coordinate) == 2, "coordinate should be a 2-tuple"

        if not(0 <= coordinate[0] < self.width) or \
        not(0 <= coordinate[1] < self.height):
            raise CoordinateError(str(coordinate))
        self.__data.pop(tuple(coordinate), None)

    
    def save(self, filename=None):
        if filename is not None:
            self.filename = filename
        
        if not self.filename:
            raise NoFileNameError()
        
        fh = None
        try:
            data = [self.__width, self.__height, self.__background, self.__data]
            fh = open(self.filename, 'wb')
            pickle.dump(data, fh, pickle.HIGHEST_PROTOCOL)

        except (EnvironmentError, pickle.pickle.PicklingError) as err:
            raise SaveError(str(err))
        finally:
            if fh is not None:
                fh.close()
    

    def load(self, filename=None):
        if filename is not None:
            self.filename = filename
        
        if not self.filename:
            raise NoFileNameError()
        
        fh = None
        try:
            fh = open(self.filename, 'rb')
            data = pickle.load(fh)
            (self.__width, self.__height, self.__background, self.__data) = data
            self.__colors = (set(self.__data.values()) | {self.__background})
        except (EnvironmentError, pickle.UnpicklingError) as err:
            raise LoadError(str(err))
        finally:
            if fh is not None:
                fh.close()


    def __export_xpm(self, filename: str): pass
    
    
    def export(self, filename: str):
        if filename.lower().endswith('.xpm'):
            self.__export_xpm(filename)
        else:
            raise ExportError(f'unsupported export format: {os.path.splittext(filename)[1]}')


    def resize(self, width=None, height=None):
        """Resizes to the given dimensions; returns True if changes made

        If a dimension is None; keeps the original. Deletes all out of
        range points.

        >>> image = Image(10, 10)
        >>> for x, y in zip(range(10), range(10)):
        ...     image[x, y] = "#00FF00" if x < 5 else "#0000FF"
        >>> image.width, image.height, len(image.colors)
        (10, 10, 3)
        >>> image.resize(5, 5)
        True
        >>> image.width, image.height, len(image.colors)
        (5, 5, 2)
        """
        if (width is None) and (height is None):
            return False
        if width is None:
            width = self.__width
        if height is None:
            height = self.__height
        if width >= self.width and height >= self.height:
            self.__width = width
            self.__height = height
            return True
        
        self.__width = width
        self.__height = height
        for x, y in list(self.__data.keys()):
            if x >= self.__width or y >= self.__height:
                del self.__data[(x,y)]
        self.__colors = set(self.__data.values()) | {self.__background}
        return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()