import pytest
from Day_01_chess import determine_color


def test_determine_color_valid():
    assert determine_color('a1') == 'Black'
    assert determine_color('h1') == 'White'
    assert determine_color('C3') == 'Black'


def test_determine_color_invalid():
    with pytest.raises(ValueError):
        determine_color('z9')
