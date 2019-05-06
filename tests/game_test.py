import sys
import io

from context import game
import test_helpers

class TestRunGame():
    def test_full_gameplay(self):
        commands = ["play", "north", "south", "west", "east", "east", "quit"]
        sys.stdin = io.StringIO("\n".join(commands))
        out, err = test_helpers.split_io(game.run_game)
        assert err == ""
        for k, v in test_helpers.expected_gameplay_out.items():
          assert (v in out[k]) == True
