from abc import ABC, abstractmethod


class Entity(ABC):
    # entity should not control its position
    def get_type(self) -> str:
        return self.__class__.__name__


class Rock(Entity):
    pass


class Tree(Entity):
    pass


class Grass(Entity):
    pass


class Creature(Entity, ABC):
    @abstractmethod
    def make_move(self):
        pass


class Herbivore(Creature):
    def make_move(self):
        pass
