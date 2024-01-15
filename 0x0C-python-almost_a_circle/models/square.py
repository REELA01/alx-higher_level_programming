#!/usr/bin/python3
"""defines sqyuare class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square class represntation"""

    def __init__(self, size, x=0, y=0, id=None):
        """intilization"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return string info of square"""
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """square size gitter and sitter"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update of square"""
        if args is not None and len(args) is not 0:
            lst = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if lst[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, lst[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns the dict of square"""
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
