import itertools
from typing import Sequence, Tuple
import numpy as np

from dec_18_data import FULL_SCAN, MINI_SCAN, scan_to_voxels


def measure_surface_area(voxels: Sequence[Tuple[int, int, int]]) -> int:
    voxel_locs = np.array(voxels)
    neighbour_matrix = (np.abs(voxel_locs[:, None, :]-voxel_locs[None, :, :]).sum(axis=2))==1
    return len(voxel_locs)*6-np.sum(neighbour_matrix)


def measure_surface_from_scan(scan: str) -> int:
    voxels = scan_to_voxels(scan)
    print(f"Got {len(voxels)} voxels from {voxels[0]} to {voxels[-1]}")
    return measure_surface_area(voxels)


if __name__ == "__main__":

    print(f"Surface area for mini-scan is: {measure_surface_from_scan(MINI_SCAN)}")
    print(f"Surface area for full-scan is: {measure_surface_from_scan(FULL_SCAN)}")
