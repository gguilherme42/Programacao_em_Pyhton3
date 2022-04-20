import sys
import subprocess


class RangeError(Exception): pass
class RowRangeError(RangeError): pass
class ColumnRangeError(RangeError): pass

_char_ASSERT_TEMPLATE = lambda c: f"char must be a single character: '{c}' is too long"
_max_rows = 25
_max_columns = 80
_grid = []
_background_char = " "

if sys.platform.startswith("win"):
    def clear_screen():
        subprocess.call(["cmd.exe", "/C", "cls"])
else:
    def clear_screen():
        subprocess.call(["clear"])

clear_screen.__doc__ = """Clears the screen using the underlying \ windows system's clear screen command"""


def resize(max_rows: int, max_columns: int, char=None):
    """Changes the size of the grid, wiping out the contents and changing the background if the background char is not None
    """

    assert max_rows > 0 and max_columns > 0, "too small"
    global _max_rows, _max_columns, _grid, _background_char

    if char is not None:
        assert len(char) == 1, _char_ASSERT_TEMPLATE(char)
        _background_char = char
    
    _max_rows = max_rows
    _max_columns = max_columns
    _grid = [[_background_char for column in range(_max_columns)] 
            for row in range(_max_rows)]

def char_at(row: int, column: int) -> str:
    try:
        return _grid[row][column]
    except IndexError:
        raise RangeError()


def add_horizontal_line(row: int, column0: int, column1: int, char: str="-"):
    """Adds a horizontal line to the grid using the given char

    >>> add_horizontal_line(8, 20, 25, "=")
    >>> char_at(8, 20) == char_at(8, 24) == "="
    True
    >>> add_horizontal_line(31, 11, 12)
    Traceback (most recent call last):
    ...
    RowRangeError
    """
    assert len(char) == 1, _char_ASSERT_TEMPLATE(char)
    try:
        for column in range(column0, column1):
            _grid[row][column] = char
    except IndexError:
        if not (0 <= row <= _max_rows):
            raise RowRangeError()
        raise ColumnRangeError()


resize(_max_rows, _max_columns)

if __name__ == "__main__":
    import doctest
    doctest.testmod()



