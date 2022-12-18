from typing import Sequence, Tuple, List

from dec_17_data import iter_is_jet_rightward, iter_rocks, JET_PATTERN_MINI, JET_PATTERN_FULL

CHAMBER_WIDTH = 7


def is_collision_or_out_of_bounds(tower: Sequence[Sequence[bool]], positioned_rock: Sequence[Tuple[int, int]]):
    if any(x < 0 or x >= CHAMBER_WIDTH for x, _ in positioned_rock):  # Check if it would hit walls
        return True
    for x, y in positioned_rock:
        if not (0 <= x < CHAMBER_WIDTH):
            return True
        if y < 0:
            return True
        if y < len(tower):
            if tower[y][x]:
                return True
    return False


def grow_tower_to_height_inplace(tower: List[Sequence[bool]], height: int):
    for _ in range(height - len(tower)):
        tower.append([False] * CHAMBER_WIDTH)


def render_tower_to_string(tower: List[Sequence[bool]]) -> str:
    return "\n".join(["".join("#" if full else "." for full in row) for row in tower][::-1])


def get_tower_height(jet_pattern: str, n_rocks: int, debug=False):
    tower = []

    jet_direction_iterator = iter_is_jet_rightward(jet_pattern)

    for rock in iter_rocks(n_rocks):
        highest_rock_position = len(tower)
        positioned_rock = [(x + 2, highest_rock_position + y + 3) for x, y in rock]
        for is_rightward in jet_direction_iterator:
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

    return len(tower)


if __name__ == "__main__":
    MINI_TOWER_HEIGHT = get_tower_height(JET_PATTERN_MINI, n_rocks=2022)
    print(f"Tower height for mini-problem: {MINI_TOWER_HEIGHT}")
    assert MINI_TOWER_HEIGHT == 3068, "Wrong answer!"
    print(f"Tower height for mini-problem: {get_tower_height(JET_PATTERN_FULL, n_rocks=2022)}")
