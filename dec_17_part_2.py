import itertools
from typing import Iterator, Tuple, Dict

from dec_17_data import JET_PATTERN_FULL, iter_is_jet_rightward, iter_rocks, iter_index_and_rocks, JET_PATTERN_MINI
from dec_17_part_1 import is_collision_or_out_of_bounds, grow_tower_to_height_inplace, render_tower_to_string, get_tower_height


def iter_index_and_is_rightward(jet_pattern: str) -> Iterator[Tuple[int, bool]]:
    for i, c in itertools.cycle(enumerate(jet_pattern)):
        yield i, c == ">"


def get_tower_height_efficient(jet_pattern: str, n_rocks: int, debug=False, check_cycles = True):
    """ Approach - at each step, make a hash representing the current state of the system
    and check for a match with previous states-hashes.  If you find a match, then you've found
    the periodicity.
    """
    tower = []

    jet_ix = -1
    jet_direction_iterator = iter_index_and_is_rightward(jet_pattern)
    situation_hash_to_rock_index_and_height: Dict[int, Tuple[int, int]] = {}
    last_jet_ix = -1

    # First: Scan trhough
    for rock_count_index, (rock_ix, rock) in enumerate(iter_index_and_rocks(n_rocks)):
        highest_rock_position = len(tower)
        positioned_rock = [(x + 2, highest_rock_position + y + 3) for x, y in rock]
        for jet_ix, is_rightward in jet_direction_iterator:
            # Implement jet
            proposed_position = [(x + 1 if is_rightward else x - 1, y) for x, y in positioned_rock]

            if not is_collision_or_out_of_bounds(tower=tower, positioned_rock=proposed_position):
                positioned_rock = proposed_position

            # Implement gravity
            proposed_position = [(x, y - 1) for x, y in positioned_rock]
            if is_collision_or_out_of_bounds(tower=tower, positioned_rock=proposed_position):
                # Add to tower
                grow_tower_to_height_inplace(tower, height=max(y for _, y in positioned_rock) + 1)
                for x, y in positioned_rock:
                    tower[y][x] = True
                if debug:
                    print(f'Tower is now:\n\n{render_tower_to_string(tower)}')
                break
            else:
                positioned_rock = proposed_position

        if check_cycles:
            if jet_ix < last_jet_ix:
                situation_hash = hash((jet_ix, rock_ix, tuple(tuple(row) for row in tower[-100:])))
                if situation_hash in situation_hash_to_rock_index_and_height:
                    last_rock_count_index, last_height = situation_hash_to_rock_index_and_height[situation_hash]
                    cycle_periodicity = rock_count_index - last_rock_count_index
                    cycle_height = len(tower)-last_height
                    print(f"Cycle detected with period {cycle_periodicity} gaining height {cycle_height}")
                    n_cycles_in_total = (n_rocks-last_rock_count_index)//cycle_periodicity
                    new_n_rocks = last_rock_count_index + (n_rocks-last_rock_count_index) % cycle_periodicity
                    return get_tower_height_efficient(jet_pattern=jet_pattern, n_rocks=new_n_rocks, check_cycles=False) + n_cycles_in_total*cycle_height
                else:
                    situation_hash_to_rock_index_and_height[situation_hash] = (rock_count_index, len(tower))
            last_jet_ix = jet_ix

    return len(tower)


if __name__ == "__main__":

    # Check that part 1 still works
    MINI_TOWER_HEIGHT = get_tower_height_efficient(JET_PATTERN_MINI, n_rocks=2022, check_cycles=True)
    print(f"Tower height for mini-problem: {MINI_TOWER_HEIGHT}")
    assert MINI_TOWER_HEIGHT == 3068, "Wrong answer!"

    # Check that part 1 still works
    MINI_TOWER_HEIGHT = get_tower_height_efficient(JET_PATTERN_MINI, n_rocks=1000000000000, check_cycles=True)
    print(f"Tower height for mini-problem: {MINI_TOWER_HEIGHT}")
    assert MINI_TOWER_HEIGHT == 1514285714288, "Wrong answer!"

    print(f"Tower height for full-problem: {get_tower_height_efficient(JET_PATTERN_FULL, n_rocks=1000000000000)}")
