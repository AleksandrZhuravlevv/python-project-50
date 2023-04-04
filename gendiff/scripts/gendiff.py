#!/usr/bin/env python3
import argparse
from gendiff import generate_diff


def main():
    desctipt = 'Compares two configuration files and shows a difference.'
    parser = argparse.ArgumentParser(description=desctipt)
    parser.add_argument('first_file')
    parser.add_argument("second_file")
    f_help = 'set format of output'
    parser.add_argument('-f', '--format', dest='format', help=f_help)
    args = parser.parse_args()
    print(generate_diff.return_result(args.first_file, args.second_file))
    return generate_diff.return_result(args.first_file,
                                       args.second_file, args.format)


if __name__ == '__main__':
    main()
