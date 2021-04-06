"""
python implement b tree
"""
import typing


class Entity(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value


class Node:
    """ single node """

    def __init__(self):
        self.data : typing.List[Entity] = []
        self.left_child :Node = None
        self.right_child :Node = None


class Tree:
    """ b tree """

    def __init__(self):
        self.size = 0
        self.root :Node = None

