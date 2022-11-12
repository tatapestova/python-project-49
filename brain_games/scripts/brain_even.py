#!/usr/bin/env python3

from brain_games.games.brain_even import even
from brain_games.logics import start_of_game


def main():
    start_of_game(even)


if __name__ == '__main__':
    main()