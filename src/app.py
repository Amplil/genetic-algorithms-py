import argparse
from runner import Runner
from player import Player
from targets import get_choices
from grape import Algorithm
from tools import IO


def main():
    parser = argparse.ArgumentParser(description='Genetic Algorithm for Python')
    parser.add_argument('target', help='target', choices=get_choices())
    parser.add_argument('-f', '--file', help='file name', default='chromosome.json')
    parser.add_argument('-p', '--player', help='player mode', action='store_true')
    args = parser.parse_args()

    io = IO(args.file)
    if args.player:
        Player(args.target, io.load_chromosome())
    else:
        Runner(Algorithm(args.target, io.save_chromosome))


if __name__ == "__main__":
    main()
