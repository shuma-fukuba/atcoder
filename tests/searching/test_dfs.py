from searching.dfs import dfs_v1


def test_bfs_v1_01():
    R = 7
    C = 8
    sy, sx = 2, 2
    gy, gx = 4, 5
    stage = [list('########'),
             list('#......#'),
             list('#.######'),
             list('#..#...#'),
             list('#..##..#'),
             list('##.....#'),
             list('########')]
    visited = [[-1] * C for _ in range(R)]
    assert dfs_v1(sy-1, sx-1, gy-1, gx-1, stage, visited) == 11


def test_bfs_v1_02():
    R, C = 5, 8
    sy, sx = 2, 2
    gy, gx = 2, 4
    stage  = [list('########'),
              list('#.#....#'),
              list('#.###..#'),
              list('#......#'),
              list('########')]
    visited = [[-1] * C for _ in range(R)]
    assert dfs_v1(sy-1, sx-1, gy-1, gx-1, stage, visited) == 10


def test_bfs_v1_03():
    R, C = 50, 50
    sy, sx = 2, 2
    gy, gx = 49, 49
    stage = '''##################################################
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
#................................................#
##################################################'''
    stage = [list(s) for s in stage.split('\n')]
    visited = [[-1] * C for _ in range(R)]

    assert dfs_v1(sy-1, sx-1, gy-1, gx-1, stage, visited) == 94
