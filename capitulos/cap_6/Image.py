import os
import pickle

class ImageError(Exception): pass
class CoordinateError(ImageError): pass
class LoadError(ImageError): pass
class SaveError(ImageError): pass
class ExportError(ImageError): pass
class NoFileNameError(ImageError): pass

class Image:
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
