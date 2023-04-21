import argparse


def arguments():
    desc = "Compares two configuration files and shows a difference."
    parser = argparse.ArgumentParser(description=(desc))
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument('-f', '--format',
                        default='stylish',
                        choices=['stylish', 'plain', 'json'],
                        help='set format of output')
    args = parser.parse_args()
    args1, args2, format_name = args.first_file, args.second_file, args.format
    return args1, args2, format_name
