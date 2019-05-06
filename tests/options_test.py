import sys
import io

from context import game
import test_helpers

class TestOptions():
    def test_rules(self):
        out, err = test_helpers.capture_io(game.rules, test_helpers.dummy)
        assert ("This is a complex world but I am a simple guide." in out) == True
        assert err == ""

    def test_quit(self):
        out, err = test_helpers.capture_io(game.quit)
        assert out == "You may yet live to see another day."
        assert err == ""

    def test_play(self):
        sys.stdin = io.StringIO("quit\n")
        out, err = test_helpers.capture_io(game.play)
        assert ("You are standing in a near pitch-black alley which" in out) == True
        assert err == ""

    def test_idk(self):
        out, err = test_helpers.capture_io(game.idk, test_helpers.dummy)
        assert out == "I don't know what that means..."
        assert err == ""

    def test_noway(self):
        out, err = test_helpers.capture_io(game.noway, test_helpers.dummy)
        assert out == "There is nothing in that direction."
        assert err == ""
