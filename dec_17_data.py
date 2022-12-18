import itertools
from typing import Sequence, Tuple, Iterator

JET_PATTERN_MINI = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

JET_PATTERN_FULL = "><<<>><<<>>><<<>>>><>>><>>>><<>><<>><>>>><<>>><<>><<>>>><<>>><<>><<<<><<<<><><<>><<<<>>>><<><<<>>><>>><<<>>><>><<<<><<<><<>><<<<>>><<<>>><<<>>><<<<><<<>>>><<<<>><<<<>>><<><><>>>><<<>>>><><<<<><<<><>>>><<<>><<>><<>><><<<<><<<<>>><>>>><<>>><><<>><<><<<<>><<>><<>>>><<<<>><<><<><<<<>><<>>><<<<>>><<>><<><<<>>>><<<>><<<>>><>><<><<<<>><<<<><><<<<>>><<<>>><<<>>>><<<<>>><<>>><<<<>>><<<><<><>><>><<<>>><<<<>>>><<>>>><<<<>>><<>>><>><<<>>><<<<>><<<<><>>>><>><>>><<<<>>>><<>>><<<<>><>>>><<<<>><><<<><>>><>>>><>><<<>><<><<<><<<<>>>><>><><<<<><<<>>>><<<<>>>><<<<>><<>><<>>><<<>>>><>>>><<<><<<>>><>><<<<>>><<<>><<<>>>><<>>>><<<>>><<><<><<<<>><<>>><>>>><<>>>><<><<<<>>><<<<><<<<>>><<>>><>>><<>>>><<<<>>>><<><>>><<<<>><<><<>><<<<>><<<<>>><<<>><><<<><<<<>>>><<>>><><<>><<<>><<>>><<<<>><>><<<>><<<>>><>>><>>>><<<><>><<>>>><<<<>><<><<<<>><<<>><<>><<<>>>><><<<>>><>><<<><<<>>><<<><<<<>>><<>>><<<>>>><<<>><<>>><<>><<>>>><<>>>><>>>><<<<>><>>><<<><<<><<><<<<>>>><<>>><<<<><<<<>><>><<>><<<><<>>><>>>><>>>><<<<>>>><>>>><<<>><<<<>>><<<>>><>>><<><<>>>><<<><>>><<>>>><<<<><>>>><><<<<>>><<<>><>>><><<>>>><<<<>>><<<<><<>>><<>>>><>><<<<><<<><<<>>>><<><<<<>>>><<<>>><<<>><<>>><>>>><<<<>>>><<<<>><>><><<<><>>><>><>>>><<<<>>><<<<>><<<>><<<<>>>><<<><>>><<><<<>><<<>>>><<<>><>>>><<<<>>>><>>><<>>><<<>>><<<><>>>><>><<<<>>><>><<<><<<<>>><><<<<>>><<<<><<>>>><<<<>>><<<>><<<><><<>>>><>><<>>><>><<>>><<<<>><<<<><>><<<<>><<<><<>><>>>><<<>>>><<<<>>><<<<>>><>>><>>><<>>><<<<><<<<>><><<<>>><<>><<>>><>>><<<<>>><<<<>>><<<>>><<<<>>><<<<>>>><<>>><<<>><<<<><<><<>><>>>><<<<>>><<>><<>>><<<>>>><<<<>>><<<<><>>>><<<<>>>><<<><>><<<<>>><><<<><>>><<<<><<<<><>>><<<<>>><>>>><>>>><<>>>><<<>>><<>><<<<><<<>>>><<<<>>><<<<><<<<>><<<>><<>>><<<<>><>>>><<<<>><<>>><<<><<>>><<>><<>>>><<<<>>><<<<>>><<<<>>><>>>><>>><<><>><<<<>>>><>>><<>>><<<>><<<><<><<<>><<<>>>><>>><<>><<>>><<<<><<<>>><<<<>>>><<<>>><>>><<>>><<<<>>>><<><<>><>>><<>>>><>>>><>><<<>>>><<>>>><<<<>>><>>><<>>>><<<<>>>><><<<<>>>><<><<<<>>><<<<>>>><<>><>><<<<>>><<><<<>>>><<<>>><<<>>><<<<>>><<>><>>><<<>>>><>>>><<><>>><<<>>><>>><<<><<<><<>>><>>><<>>>><<><<<<>>>><<>><<<<>><<<<>>>><<<><>>><<><<<<>>>><<<>><<<>><>><>>>><>><><<>><<>><<<<><<><<>>>><>>><<<<><<>>>><<><<>>><<<<>><<<<><<<><>>><<>>>><<<<><<<<>>><<<>><<<<><<<<>>>><<>>>><<<<>>><<<><<<><<><<<<>>>><<<>>>><<<>>><<<<>><<<>>>><>>><<<<>><<>>>><<<>>>><>><<<<>>><<<<>>><<><<>>>><<<><<<<>>>><<<>><<>>>><<<>>>><<<><<<<>>><<<>>>><>><<<<>>><<>>>><><<<<>>>><<>><<<>><<<>><<<<>>>><<<<>>>><<<>>><<>>>><<<<><<<<>>><<<>>>><<<<>>><<<<>>><>>><<<<>><<>><>>>><<<><<<>>>><<<>>>><>>><<><><<<>>>><>>>><<<>>>><<>>>><><<<<>><>>><>>>><><<>>>><>>><<>>>><<<>><<>>>><<><<><<>><<<<>>><<<>>>><<>>><<<>>>><>><<<<>>><<>>><<<>>><<<>>>><<><>>><>>>><>>>><<<<>><<>>><><<>>><<>>><<>>><<>><><<<><<<<>>><<<<><<<<><<<<>><<<<><<<><<<<>>><<<<>>>><><<<>><>>><>>><>><<<>>>><<<>>>><<>>><<><>><<<>>><<<><>>><<<>>><<>><<>><<>>>><<<<>>><<<>>>><>><<>>>><<<<><<<>>><<>><<<><<<>>><>>>><<<<><<<>><>><<<>><>>>><<<<><>><<<<>><<>><>>>><<>><<<<>>>><>><>>>><<><<>><>>>><<<>>>><<<<>><>>><<>><<<<>><<<<><<<<>>>><>><<>><<<<><<<>>>><<<>><<>>>><<<>>>><>>>><<<>><<<>><<<><<>>><<>>>><<>>><<<>><<<>><<<>>><<>>><>><<><<<>><<><>><>><<<>>><<<<><<<><>>>><<<><>>><<<>>><<<<>>><<>>><<<<>>>><<>><<<>>>><<><<<><>>><<<>>><<<>><<<<>>><<>>><>><<<>><<>>><>>><<<>>><<<>>>><<<>>>><>>><<<<><>>>><><>>>><>><>>><>><<>><<<<>>>><><<<<>>><>>>><<>>><<<><<<>><<>><<<>>>><<>>>><><<<>>><<<<>><<<<><<>><>>><>><<<>>>><<<<>><<<>>>><<<<><<<>>><<>>>><<>><<<<>>>><<<<>>><<<>>><<>><<<>><>>>><<<>>>><<<<><>>><<><<<>>>><>>>><<>>>><>><<<><<>>><<<>>><<<<>>>><<<<>>><>><<>>><<<<>>>><<<<><<>><<>>><<<<>><<<<>><<><>>>><>>>><<>>>><<>>>><>><<<>>><<<>><<<<>>><<<>>><>><<>><<>><<<>><<<<><<<<><>>><<>>>><>>>><<<>>>><<<>><<><<><<<<>>>><<<<><<<>><<<><>>><<<<>><>><<><<<>><>>><<>>>><<><<>><<>><<<<><<>>><<<<>>><<<><<<<>><<<>>>><><<>>>><<>>>><<<>><<<<>>><<<<><><><<<>><<<<>>><<<<>>>><>>><<<>>>><<<<>><>><<<<>><<>><<<>><<<><<<><<<<>>>><><<>>>><>>><<>>>><>>>><<<<>>><<<>>><<<<><>>><><<<<>><<<<>>><<<<>>>><>>>><<<>>><<<<>>>><<<<>>><>>><<>><<>>>><<<<><<<<>><<>>><<><><<><<<<><<><<<><>>>><<<<>><<>>><>>><<><<>><<>>>><<<<><<<>>>><<>>>><<<><<<><>>><<<>>>><><<<>>>><><>>><<>>>><<<<>>><<<>>>><<<<>><<<>><<<<><<<><<>>>><>>><<<>>>><>>>><<<><<>>>><<<<>>>><>>><<<>><<>><<<<>>><<<>><>>>><<<<>>>><<><<<>>><<<<>><<<>>><><<<<>><<<<>><<><<>><>><><<<<><<>>><<<<>>><<>>><<<<>><<<<>><<><<<<>>><<>><<>>><><<<>>>><>>><<>>>><<<<>><<<<><<>>>><>>>><>>><<<<>>><>><>><<<<>><>>><<<>>>><<<><<<>><<<>>>><<>>><<<>>>><><>>>><<>><<<<>><<<<>>><<>><<>>><>><<<>><<<>>><<<<>>>><<<<>>>><>><<<<>>>><<><<<<>>><>>>><>>><<>>>><<<>>>><>>>><><<<><<>>>><><><<<<>>><<<<>><<<<><<><<<<>>><<<<>><<>>><<<>>><<<<>>><<<<><<<<>>>><<<<>>>><<<>><<>>><<<<><>>>><<>>>><<<<><<<><>>><<<>>>><>>><<<>><<<>><<<>>>><<>>><<><>><>>>><<<>>><<><<<>><<<<><>>><><<<<>><<<>><<<>>>><<><<<<>>><<<<>><<<>><<<>>><<>>>><>>><<>>><<<<><><<<>><<<><>><<>><<<<>>><<<>>>><<<<>>><<><<<<>>><<<>><<<>>>><<<<><><<>>><<<><<<>>><<<<>>>><>>>><<><<<><<<<>>>><<<><>>><<<<><<<<>><<>>>><<>><>>><>>><<>>><><><<<>>>><><>>><>>>><<<><<<<>><<<>>><<<<>><>>>><<><<><<<<>><><><<<>><<<<>>><<<<>>>><>><<<<>><>>>><>>><<<<><<<>>><<<<>><<<<>>>><<>>><<>><<<<>>>><<>>>><<<<>><><<<>>>><><<<<>><>>><<<<>><<<><<<<>>><<>>><<>>><<<>>>><>>>><>>><<>>>><<<<><><>>>><<<><><>>><>>>><<<<><<<<>>><<>>><<<<>>><>>>><<<<>>><<<>><<><>><<<<>>><<>>><<<>><><<<<>>>><<>>>><<<>>>><<>><<<>>>><<<>><<<<>>><>>>><<>>><<<<>><<<>>>><<<<>>>><<>><<<>>><<>><<><><>><<<<><<>><<<<>><<><<<>>>><<>>>><<<><>>>><><<>><<<<>>><<<>>><<<<>>><>>><<<>>><><>>>><<>>>><<<<><<><<>>>><<<>>>><<><<<<>>><<<<>>><<>><<<<><<<>>>><<<>>>><<<<>>>><<<<>>><<>><><>>>><<>><<<>>>><<<<>><<<<>>><<<<>>><><<<>>>><<<<>>><<>><<<><<<<>>><>>>><>>><<>>><<>><<<<>>><<<<>>><<<>><>>><<<>>><<>>>><<>>><<<><<<>><<><<<<>>>><>>>><>>><<>>><<<>>>><<>>>><<><<<>>>><<><<<>><>><<>><<<<>><<>><<<<><<<<><<>>><<<>>>><><<>>>><<<><<>>>><<<<><>><<>><<<>>><<<<>><>><<<<>><<<<>><<>>><<<<><<>>>><>>>><<>>>><>>><>>><<<<>>><><><>>><<<>><<<>><>>><><>><<<<>>>><<>>>><<<>><>>><>><<>>>><<<<>>>><<<>><<<>>><>><<<>>><<<<>><<<<>><<>>>><>><><<<>>><<<>>><><><<<>>>><<<<>><<<><<<<>>>><<<<>>><>><>>>><<<>><<<<><<<<>>>><<>><<<<>>><<><<>>>><<>>><<<>>>><<>>>><<>><<>>>><<<<>>>><<<>>><<>><<<>>><<>>>><<<<>>>><>>><<<<>>><<>>>><<<<><<<>>>><<>><>><<<>>><<<<>><>>>><<<<>>>><>>><<<<>>><>>>><<><<>>><<>><<<<>>>><<<>><<<>>><<<<>><<<>>><<<>><<<><<>><<>>>><<<<>><<<>>><<>><<<>>>><<>>>><<<<>>>><<<>>><<<<>>><<>>><<>>>><<<<><<<<>>>><<<<>><>><<<<>><<><<<<>>>><<>><<<<>>><<<><<<><><<<>>><<<<><>><<<>><<>>>><<>><><<><<>>><<<>><>>><<<<>><>>><><<<>>>><<<<>>>><<>><<>><<<<>>>><<>>>><<<<>><>><<>>><<<>><>><<><<>>>><<<<>><>>>><<<<>>><><>>><>><<<<><<<><<<<>>><<<<>><<<<>>>><>><>>>><<<<>>><>>><<<<>>><<<<>>><<>><<><<<>>><><<<>><>>>><>><>>>><<<<>>><<<<>>><><<<<>>><<>>>><<<<>>>><<<>>><<<>><<<<>><<<>>><<<<><><<<<><><<<>><<>>>><<<<>>><<<<>>>><<<><<<>>>><<>>>><<<<>>>><<>>><<>><<>><<<>>><><<<><<<<><>>><<<<>>>><<<<>>>><<>>><<<<>><<<>>><<>>>><><>>>><<<<>><<<><><<<<><>>><<>>><>><>>><<<>>>><<<>>><>>>><<>>><><<<><<<<><<>>>><>>>><<<<>>>><<<<>>>><<>>><>>><>><<>>><><<><<><<<>><>><><<><<>><<>>><<<>>><<<<>>>><><<><<><<>>><<<>>>><<><<<<>>>><<<>>><<>><><>>>><<<>>>><<>>>><<<>><<<><<>><<<<>>>><<<<>>>><<>>>><<<<>>><<>>><<>>>><<>><>><<<<>><<<<>>><>>>><<>><<>><>><>>>><<<<>>>><<<<>>><>>>><<>><<<><><<<><<<<>>><<<<>>><<<<>>><>>><><><>>>><>>>><<<<>>>><<<<>>>><<>>>><<<<>>>><<>><<<>>><<>>>><<><><>>>><>><<>><<<>>><<<<>>>><>>>><<>>>><><><<<<>>><<<>>>><<>>>><<>>><<>><<><>><<<>>><<<<>>><<<<>>><<>>><<<<>><<<<>><<<<>>><<<>><<<>>>><<<><><<>><>><<>><<<<>>><<<<><><<<>>>><<<<><<>>><<<>>><<<><<<<>><<><<<<>>>><<<<>>><<<<>>><<<<>><<><<>><<<>>><<<<>>>><>><>>><<<><<<<>>>><<<>>><<>><<>><<<<>>><<<>><<>>>><<>><><>>><<>>><<>><<><<<<>>>><>>><<><<>>>><<<>>><<>>><<>>><<<>>><<>>><<><<>>>><<<<>>>><<<>><<<>>><<>><<<>>>><<<<>>>><<<<><>>>><<<<>><>><<>>><>>><>>><<<<>>><<>><>><<>>><>><<>><><<<>>><<<><<<<>>><<<<>>>><<<<>>><<><<>>><<<<>><<<>><<<<>>><<<>><>>><<>>>><<<>>><<><<>><<>><<<>>>><><<<<>><<<>><<<><<<>>>><>>><<<>>>><<<><<>>><<<>>>><>>>><<<<>><<>>>><>>><<<<>>>><<<<>>><>><<<>><<>><<<><<<<>>><>>><<<>>>><><>>><<<<>>><>>>><<<>><<<<>><>>>><><<<>>>><><<<<>>><<>>>><>>><<<>>><<<><<<<>>><<<<><<<<>>>><<<<>><<>>>><<<<>>><>>>><<<>><<<><<<<><<<<>>>><<<>>><<<><>>>><<<>><<<>>><<<<>>>><<<>>>><<<>><<<>>><<>>>><<<<>>><<<><>>><>>>><>><<<>><<>><><<<<><<<>>><<<>><<<<>>>><<<>>>><<>>><<<<>>>><<<>>>><<<>>><<<>>>><>><>>>><<<>>>><<<<>>><<<<>><<<>><<<>>>><<>>><><<>><<<<>><<>>><<<<>>>><<<<>><<<<>>><>><<<>>><<>><<<<>><<<>>><<<><<>>>><<>>><><<<<><>>><<>>><<<<><<<<><>>><<>>>><<<>>>><<>>><<<<><<>>><<>>>><<<<>><<<>>><<<>><<<<>>><<<>><<<<>>><<>>>><>><<<<>>><<<>>>><<<<>><<<>>><<<<>><<><<><>>>><<<><>>>><<<>>><>>><>>>><<<>><<<<>><>><<<>>><<<<><>>>><<<<><<<<>>><<><<<>>>><<<><<><<<<>>>><<><<><<>><<<<>>>><<>>><>>><<<<>>>><<<<><<>><<<>>><<<<>>>><<<>>><>>>><<<<>>><<<>><<<>><<<>>>><<<>><<<<>>><><><<>>>><>>><<>>><<<>><<>>>><>>>><<<><>>>><>>>><<<>>>><<<>><<<<>>>><<<<><<<<>>><<>><<<>>><<<<>>>><>>>><<><<<<><<><>><<<>>><<<><<<<><<<<>>><<<<>>>><<<<>><<<<>>>><<>>><<<>>><<<>>>><<<>><<<>>>><<<<>>>><>>>><<><<>><<<<>><<>><<<<>>><>>>><<<<>><<>>><<>>>><<<><>><><<<<>>><<<><<>>>><<>>><<<<>>><<<>>><>>>><<>>><<<>>><<>><>><>>>><<><<<><<<<>>>><<<<><>>><>><<>>><<<><>>><<<<><>><<<<><<<<><<<<><>>>><<<>>><<<<>><<<<>>><<>>>><<>>>><>>>><<<>><<<<>><>>><<<><<>><><<>>><<<<>>><><<<<>>><>>><<>>><<>>>><><<<>>>><<>>><>>>><>>>><<<<>>><<>>>><<>>>><>><><<<<>>><<><<>>><<<<>>><<<<><<<<><<>>>><>>>><<<<>>>><<<<><<<<>>><<>>><<<><>>><<><<<>>>><<><>>>><><<>><<>>>><<>><<<><<<>>>><>>>><<<><>>><<>>><<<>>><<<<>>>><<<>><<<<><<<>>><<<<>><>>><<>>><<<<>><>><<<>>><><>><<<>>>><<>>>><<<><<<<>><<<<>>>><>><<><<>>>><<<>><>><<<<><>>><><<<<>>><><<<>>><<><<<>>>><><<>>><<><<>>><<<><<<<><<>><<<>>>><<<<>>>><<>>><<<><<<>>><>><<<<>><<>>><<<>><>>><<<><>><<>><<<>><<>><<>>><<<<>>>><>><<><<<<><>>><<<>>><<<<>><>><<>>>><<><<>><<>>><>>><<<>>><<><<<<><><<>>><<>>><<<><><<>>>><<<>><<<<>><<<>>><<<><>>><<>>><<>>>><><<>>><<>><>>>><<>><<<><>><<<>>><<<<>>><<>><<<>>>><<<>>><<>>><<<<>>>><<<>>>><<<>>>><>>>><<>>>><<<>>><<>>>><<>><<>>>><<<><><><<>>><<<>><<<><>>>><>>><<>><<<<>>><<<<>><<<>><>><<<<>><<<<><<<><<<<>><<<>>>><>>>><<>><<><<<>>><<<><<<>>><<>>>><<<>>>><>>>><<<><>>><<>>><<<<>>><<<<>>>><>>"

ROCK_SHAPES = """
####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##
"""


def get_rock_shapes_xy() -> Sequence[Sequence[Tuple[int, int]]]:
    shape_strings = [s.strip('\n').split('\n') for s in ROCK_SHAPES.strip('\n').split('\n\n')]
    shape_strings_xy = [[(x, len(s)-y-1) for y, line in enumerate(s) for x, c in enumerate(line) if c == "#"] for s in shape_strings]
    return shape_strings_xy


def iter_is_jet_rightward(jet: str) -> Iterator[bool]:
    characters_in_jet = set(jet)
    assert characters_in_jet == set("<>"), f"Jet had invalid characters: {characters_in_jet.difference(set('<>'))}"
    for c in itertools.cycle(jet):
        yield c == ">"


def iter_rocks(n: int) -> Iterator[Sequence[Tuple[int, int]]]:
    """ Get rock shapes as a list of (x, y) points, with x starting from left and y starting from bottom """
    for rock, _ in zip(itertools.cycle(get_rock_shapes_xy()), range(n)):
        yield rock


def iter_index_and_rocks(n: int) -> Iterator[Sequence[Tuple[int, Tuple[int, int]]]]:
    """ Get rock shapes as a list of (x, y) points, with x starting from left and y starting from bottom """
    for (ix, rock), _ in zip(itertools.cycle(enumerate(get_rock_shapes_xy())), range(n)):
        yield ix, rock


if __name__ == '__main__':
    print(f"Rock Shapes: \n{get_rock_shapes_xy()}")

    print(list(iter_rocks(3)))