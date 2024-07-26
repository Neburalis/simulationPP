from abc import ABC, abstractmethod
from graph_search import bfs_path

N, M = 5, 5


class Entity(ABC):
    # entity should not control its position
    def get_type(self) -> str:
        return self.__class__.__name__


class Map:
    def __init__(self, max_x, max_y):
        self.board = {}
        self.max_x, self.max_y = max_x, max_y

    def __getitem__(self, key: tuple[int, int]) -> Entity | None:
        if isinstance(key, tuple) and len(key) == 2:
            x, y = key
            if (x, y) in self.board.keys():
                return self.board[(x, y)]
            else:
                return None
        else:
            raise TypeError(f'Argument {key} must be {tuple} with coords')

    def __setitem__(self, key: tuple[int, int], value):
        if isinstance(key, tuple) and len(key) == 2:  # Получили координаты?
            x, y = key
            if 0 <= x < self.max_x and 0 <= y < self.max_y:  # Они внутри границ?
                if (x, y) in self.board.keys():  # Туда можно переместится?
                    if isinstance(value, Entity):  # Получили сущность?
                        # Тогда перемещаем
                        entity = value
                        self.board.pop(entity.get_position())  # Удаляем ссылку на сущность со старой позиции
                        self.board[(x, y)] = entity  # Добавляем ссылку на сущность на новую позицию

                        entity.set_position(x, y)  # Устанавливаем сущности новое положение
                    else:
                        raise ValueError(f'Argument value {value} must be an instance of {Entity}')
                else:
                    raise IndexError(f'Entity on {(x, y)} already exists')
            else:
                raise IndexError(f'Coords {(x, y)} is out of bounds. Bounds is {0, 0} and {self.max_x, self.max_y}')
        else:
            raise TypeError(f'Argument key {key} must be {tuple} with coords')

    def __iadd__(self, arg):
        if isinstance(arg, Entity):
            entity = arg
            x, y = entity.get_position()
            if 0 <= x < self.max_x and 0 <= y < self.max_y:
                if (x, y) not in self.board.keys():
                    self.board[(x, y)] = entity
                    entity.set_map(self)
                else:
                    raise IndexError(f'Entity on {(x, y)} already exists')
            else:
                raise IndexError(f'Coords {(x, y)} is out of bounds. Bounds is {0, 0} and {self.max_x, self.max_y}')
        else:
            raise TypeError(f'Argument value {arg[0]} must be an instance of {Entity}')
        return self

    def __isub__(self, arg):
        if isinstance(arg, tuple) and len(arg) == 2:
            x, y = arg
            if (x, y) in self.board.keys():
                del self.board[(x, y)]
        else:
            raise TypeError(f'Argument {arg} must be {tuple} with coords')
        return self

    def generate_graph(self):
        graph = [[0 for x in range(M)] for y in range(N)]
        for cords in self.board:
            graph[cords[0]][cords[1]] = self.board[cords].get_type()
        return graph


