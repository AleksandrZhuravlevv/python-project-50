#!/usr/bin/env python
import argparse
from gendiff.cli import generate_diff


def parse_args():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('filename1', metavar='first_file')
    parser.add_argument('filename2', metavar='second_file')
    parser.add_argument('-f', '--format', help='set format of output')

    return parser.parse_args()


def main():
    args = parse_args()
    filename1, filename2 = args.filename1, args.filename2
    if not args.format:
        args.format = 'stylish'

    generate_diff(filename1, filename2)


if __name__ == '__main__':
    main()
