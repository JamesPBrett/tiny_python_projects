#!/usr/bin/env python3
'''
This script prints a greeting to the user.
Usage: hello.py [-h] [-n name]

Options:
  -h, --help            show this help message and exit
  -n name, --name name  Name to greet (default: World)


To run:
    hello.py -n Jane
    hello.py
'''
import argparse


def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name', metavar='name',
                        default='World', help='Name to greet')
    return parser.parse_args()


def main():
    """Make a jazz noise here"""
    args = get_args()
    print('Hello, ' + args.name + '!')


if __name__ == '__main__':
    main()
