from standard_calc import bound_to_180, is_angle_between


""" Tests for bound_to_180() """


def test_bound_basic1():
    assert bound_to_180(0) == 0
    assert bound_to_180(2137) == -23
    assert bound_to_180(135) == 135
    assert bound_to_180(180) == -180
    assert bound_to_180(6767) == -73
    assert bound_to_180(200) == -160
    assert bound_to_180(-182.8) == 177.2
    assert bound_to_180(-1) == -1


""" Tests for is_angle_between() """


def test_between_basic1():
    assert is_angle_between(0, 1, 2)
    assert not is_angle_between(200, 120, 300)
    assert not is_angle_between(0, 300, 720)
    assert is_angle_between(0, 0, 179.2)
    assert is_angle_between(45, 45, 45)
    assert is_angle_between(45, 45, 270)
