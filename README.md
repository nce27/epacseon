```
                     #################################################
                                    Welcome to Epacseon               
                     #################################################
```

### About
This repo is just a starting point for people who are new to code and are looking
for a simple idea to work on.

It is written in python and inspired by the [open-adventure](https://gitlab.com/esr/open-adventure) and `dunnet` games,
which I suggest you check out! (All mac users have `dunnet` on their machines by default,
type `emacs -batch -l dunnet` into your terminal to welcome your new obsession!)

#### Text-based adventure?
The common themes in games like these are:
1) There is either some mystery to be solved or some sequence of tasks which let you progress.
1) Players can collect objects (eg keys, shovel) without which they cannot continue/access certain areas.
1) There are many ways to die and be forced to start over.
1) There is at least one way to win.
1) There are 'easter eggs' which may not help you win but are just lovely to find.
1) They deliberately limit what players can type/do.
1) Players can quit or see a help/rules menu at any time.
1) They give the player all the information they need to act.
1) And because we all expect the above rule to be true, game designers sometimes throw
  in miscellaneous info which has no relevance just to drive players mad.

For your version of the game it doesn't matter if you follow all these patterns or none of
them or if you invent your own! Do what you like!

The code here is just boilerplate: you can expand it as you like, or throw it all away.

### Tips
Code for games like these can get pretty out of hand: lots of printed text, endless if/else
statements, monstrous files etc. This makes adding new code or even just finding stuff a pain.
I have done the tiniest bit of a game, and already it is looking messy.

As you go, try to do the following:
- Refactor: put common things into reusable functions
- Can different objects and/or locations go into separate classes (and thus separate files)?
- Is there something you can use instead of if/else to handle player decisions? (python does not have switch statements, but it does have powerful dictionaries.)
- Try to keep [writing tests](https://docs.python-guide.org/writing/tests/). I have written some using [`pytest`](https://docs.pytest.org/en/latest/) to include the current state of play, obviously change the tests as you change the flow. Testing will save you the time of running through the whole game manually after every change, will help ensure you don't break your code while adding something else, AND will keep dead code to a minimum. (For the basics on testing, see [Intro to TDD](https://github.com/fouralarmfire/square-one/blob/master/tutorials/fizzbuzz-tdd.md#intro-to-test-driven-development-fizzbuzz))
- Keep the text you print out to 80 characters or less per line. The first computers (which could render text on screen) had space for max 80 characters per line, so it's the number we like to stick with out of habit and for readability.
- You do **not** need a grid or game-board (unless you want one). Simply restricting a player's movements by only processing some actions is enough.


### Get started!

Fork this repo to your own user area, then clone your fork. Unfamiliar with Git and/or the terminal? [Learn here](https://queenofdowntime.com/resources/tutorials/git).

I have set this up using [`pipenv`](https://docs.pipenv.org/en/latest/) to manage the environment and dependencies.
  - Install `pipenv`: `pip3 install pipenv` or `brew install pipenv` (mac only)
  - Install deps from the existing `Pipfile`: `pipenv install`
  - To enter the virtual environment: `pipenv shell`
  - To install new project dependency: `pipenv install <dep>` (`--dev <dep>` for a package just used in tests)

Run the tests:
```sh
$ pipenv run pytest
```

Play the game:
```sh
$ pipenv shell
(epacseon) bash-3.2$ python play.py
```

(`exit` to leave the shell).

The game is partially implemented, obviously, to let you take it forward. As it stands you can only make about 4 moves in a circle, and only some of the commands listed in the `rules` have a response.

_Disclaimer: I do not work in or use python day-to-day, I have no idea of what the best practices or industry favourite tools for testing or dep management may be._
_This boilerplate could make a true pythonista faint! Once you wake up, please PR the correct thing!_
