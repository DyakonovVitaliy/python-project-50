#!/usr/bin/env python3
from gendiff.cli import parse
from gendiff.diff_files import generate_diff

def main():    
    args = parse()
    print(generate_diff(args.first_file, args.second.file))

if __name__ == '__main__':
    main()
