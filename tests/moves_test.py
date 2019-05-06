import sys
import io

from context import game
import test_helpers

class TestMoves():
    def test_start_options(self):
        for move, text in test_helpers.start_moves.items():
            sys.stdin = io.StringIO("{}\nquit\n".format(move))
            out, err = test_helpers.capture_io(game.start_options)
            assert (text in out) == True
            assert err == ""

    def test_alley(self):
        for move, text in test_helpers.alley_moves.items():
            sys.stdin = io.StringIO("{}\nquit\n".format(move))
            out, err = test_helpers.capture_io(game.alley_start)
            assert (text in out) == True
            assert err == ""

    def test_house(self):
        for move, text in test_helpers.house_moves.items():
            sys.stdin = io.StringIO("{}\nquit\n".format(move))
            out, err = test_helpers.capture_io(game.house)
            assert (text in out) == True
            assert err == ""

    def test_east_alley(self):
        for move, text in test_helpers.east_alley_moves.items():
            sys.stdin = io.StringIO("{}\nquit\n".format(move))
            out, err = test_helpers.capture_io(game.east_alley)
            assert (text in out) == True
            assert err == ""

    def test_west_alley(self):
        for move, text in test_helpers.west_alley_moves.items():
            sys.stdin = io.StringIO("{}\nquit\n".format(move))
            out, err = test_helpers.capture_io(game.west_alley)
            assert (text in out) == True
            assert err == ""
