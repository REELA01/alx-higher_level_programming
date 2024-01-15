#!/usr/bin/python3
"""defines the Base class"""
from json import dumps, loads
import csv


class Base:
    """the base class representation"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initlization"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON string representation of list_dictionaries"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save json represnation to a file"""
        if list_objs is not None:
            list_objs = [ob.to_dictionary() for ob in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """deserialaization"""
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new = Rectangle(1, 1)
        elif cls is Square:
            new = Square(1)
        else:
            new = None
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """load from the file that we have save to"""
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as f:
            return [cls.create(**dic) for dic in cls.from_json_string(f.read())]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save to csv"""
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[ob.id, ob.width, ob.height, ob.x, ob.y]
                             for ob in list_objs]
            else:
                list_objs = [[ob.id, ob.size, ob.x, ob.y]
                             for ob in list_objs]
        with open('{}.csv'.format(cls.__name__), 'w', newline='',
                  encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """load from csv"""
        from models.rectangle import Rectangle
        from models.square import Square
        ret = []
        with open('{}.csv'.format(cls.__name__), 'r', newline='',
                  encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                row = [int(r) for r in row]
                if cls is Rectangle:
                    dic = {"id": row[0], "width": row[1], "height": row[2],
                         "x": row[3], "y": row[4]}
                else:
                    dic = {"id": row[0], "size": row[1],
                         "x": row[2], "y": row[3]}
                ret.append(cls.create(**dic))
        return ret

    @staticmethod
    def draw(list_rectangles, list_squares):
        import turtle
        import time
        from random import randrange
        turtle.Screen().colormode(255)
        for i in list_rectangles + list_squares:
            tur = turtle.Turtle()
            tur.color((randrange(255), randrange(255), randrange(255)))
            tur.pensize(1)
            tur.penup()
            tur.pendown()
            tur.setpos((i.x + tur.pos()[0], i.y - tur.pos()[1]))
            tur.pensize(10)
            tur.forward(i.width)
            tur.left(90)
            tur.forward(i.height)
            tur.left(90)
            tur.forward(i.width)
            tur.left(90)
            tur.forward(i.height)
            tur.left(90)
            tur.end_fill()

        time.sleep(5)
