#!/usr/bin/env python3
from gendiff.cli import parse
from gendiff.gen_diff import generate_diff


def main():
    args = parse()
    print(
        generate_diff(args.first_file, args.second_file, formater=args.format)
        )


if __name__ == '__main__':
    main()
