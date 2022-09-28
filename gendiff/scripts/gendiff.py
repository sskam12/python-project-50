import argparse


def main():
    """Parser for command-line options, arguments and sub-commands"""
    parser = argparse.ArgumentParser(prog='gendiff',
                                     description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format',
                    choices=['stylish', 'plain', 'json'],
                    default='stylish',
                    help='set format of output')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    main()
