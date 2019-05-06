import sys
import io
import contextlib

# capture_io will run the given function and redirect the printed
# output (and possible errors) to a variable which can be checked
def capture_io(call_func, *args):
    tmp_stdout, tmp_stderr = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(tmp_stdout):
        with contextlib.redirect_stderr(tmp_stderr):
            call_func(*args)
    out = tmp_stdout.getvalue().strip()
    err = tmp_stderr.getvalue().strip()
    return out, err

# split_io calls capture_io but splits the recorded output by the game prompt '>'.
# this will allow the output from individual moves to be checked against the
# desired gameplay order.
def split_io(call_func):
    out, err = capture_io(call_func)
    return out.split(">"), err

# some game functions have other functions as a required parameter
# when testing (with capture_io) we can pass in dummy
def dummy():
    return 0

# we don't want to test against the entire text of the game story,
# the first line will do.
# we should aim to have these lines defined in one place so that changes do not
# have to be copied across multiple test files.
first_line_of = {
    "welcome": "Welcome to Epacseon",
    "alley": "You are standing in a near pitch-black alley which",
    "house": "The door creaks as you push through. When it closes",
    "west_alley": "You follow the alley to the west. You feel the ground tilt",
    "east_alley": "You follow the alley to the east. It seems to be getting",
    "quit": "You may yet live to see another day.",
    "idk": "I don't know what that means...",
    "rules": "This is a complex world but I am a simple guide.",
    "noway": "There is nothing in that direction",
}

# when running the full game we expect to see output in this order
# further playbooks can be added to cover multiple routes
expected_gameplay_out = {
    0: first_line_of["welcome"],
    1: first_line_of["alley"],
    2: first_line_of["house"],
    3: first_line_of["alley"],
    4: first_line_of["west_alley"],
    5: first_line_of["alley"],
    6: first_line_of["east_alley"],
    7: first_line_of["quit"],
}

# all possible moves from the start menu
start_moves = {
    "play": first_line_of["alley"],
    "rules": first_line_of["rules"],
    "quit": first_line_of["quit"],
    "nonsense": first_line_of["idk"],
}

# all possible moves from the starting point in the alley
alley_moves = {
    "rules": first_line_of["rules"],
    "quit": first_line_of["quit"],
    "nonsense": first_line_of["idk"],
    "n": first_line_of["house"],
    "north": first_line_of["house"],
    "s": first_line_of["noway"],
    "south": first_line_of["noway"],
    "w": first_line_of["west_alley"],
    "west": first_line_of["west_alley"],
    "e": first_line_of["east_alley"],
    "east": first_line_of["east_alley"],
}

# all possible moves after entering the door to the house
house_moves = {
    "s": first_line_of["alley"],
    "south": first_line_of["alley"],
    "rules": first_line_of["rules"],
    "quit": first_line_of["quit"],
}

# all possible moves after moving one command to the eastern end of the alley
east_alley_moves = {
    "w": first_line_of["alley"],
    "west": first_line_of["alley"],
    "rules": first_line_of["rules"],
    "quit": first_line_of["quit"],
}

# all possible moves after moving one command towards the western end of the alley
west_alley_moves = {
    "e": first_line_of["alley"],
    "east": first_line_of["alley"],
    "rules": first_line_of["rules"],
    "quit": first_line_of["quit"],
}
