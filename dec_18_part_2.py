import itertools
from typing import Sequence, Tuple
import numpy as np

from dec_18_data import scan_to_voxels, MINI_SCAN, FULL_SCAN


def measure_surface_area(voxels: Sequence[Tuple[int, int, int]]) -> int:
    voxel_locs = np.array(voxels)
    neighbour_matrix = (np.abs(voxel_locs[:, None, :]-voxel_locs[None, :, :]).sum(axis=2))==1
    return len(voxel_locs)*6-np.sum(neighbour_matrix)


def get_voxel_neighbour_matrix(voxel_array: np.ndarray) -> "Array['N,N', bool]":
    voxel_array = np.asarray(voxel_array)
    return (np.abs(voxel_array[:, None, :] - voxel_array[None, :, :]).sum(axis=2)) == 1


def is_connected(adjacency_matrix: "Array['N,N', bool]", home_index: int):

    connected_mask = np.zeros(len(adjacency_matrix), dtype=bool)
    last_connected_mask = connected_mask[home_index] = True
    # connected_mask.copy()
    while True:
        connected_mask = connected_mask | np.any(adjacency_matrix[connected_mask], axis=0)
        if np.array_equal(connected_mask, last_connected_mask):
            break
        last_connected_mask = connected_mask
    return connected_mask


def measure_exterior_surface_area(voxels: Sequence[Tuple[int, int, int]]) -> int:
    # General approach
    # - Create a box around the voxels where all voxels on the outside of the box are empty
    # - Get the set of empty voxels in this box
    # - Get the set of voxels in this box connected to the corner (which should be empty)
    # - Find the total surface area of this set of "outside empty voxels"
    # - Subtract the surface area of the box.

    voxel_locs = np.array(voxels)
    outside_corner_min = np.min(voxel_locs, axis=0)-1
    outside_corner_max = np.max(voxel_locs, axis=0)+1
    voxel_locs_set = set(tuple(v) for v in voxel_locs)  # For speed
    ijk_edges: Tuple[Sequence[int], Sequence[int], Sequence[int]] = tuple(list(range(omin, omax+1)) for omin, omax in zip(outside_corner_min, outside_corner_max))
    all_voxels = list(itertools.product(*ijk_edges))
    all_empty_voxels = np.array([v for v in all_voxels if tuple(v) not in voxel_locs_set])
    empty_voxel_adjacency_matrix = get_voxel_neighbour_matrix(all_empty_voxels)
    empty_voxel_on_outside_mask = is_connected(empty_voxel_adjacency_matrix, home_index=0)
    empty_voxels_connected_to_outside = all_empty_voxels[empty_voxel_on_outside_mask]
    surface_area_of_box = sum(len(ijk_edges[n])*len(ijk_edges[m]) for m, n in [(0, 1), (0, 2), (1, 2)])*2
    exterior_surface_area = measure_surface_area(empty_voxels_connected_to_outside) - surface_area_of_box
    return exterior_surface_area


def measure_exterior_surface_from_scan(scan: str) -> int:
    voxels = scan_to_voxels(scan)
    print(f"Got {len(voxels)} voxels from {voxels[0]} to {voxels[-1]}")
    return measure_exterior_surface_area(voxels)


if __name__ == "__main__":

    TEST_VALUE = measure_exterior_surface_from_scan(MINI_SCAN)
    print(f"Exterior Surface area for mini-scan is: {TEST_VALUE}")
    assert TEST_VALUE==58
    print(f"Exterior Surface area for full-scan is: {measure_exterior_surface_from_scan(FULL_SCAN)}")
