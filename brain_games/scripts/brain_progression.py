#!/usr/bin/env python3

from brain_games.games.brain_progression import progression
from brain_games.logics import start_of_game


def main():
    start_of_game(progression)


if __name__ == '__main__':
    main()
