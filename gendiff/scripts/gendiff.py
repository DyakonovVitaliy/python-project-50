#!/usr/bin/env python3
import argparse


def main():    
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('indir', type=str, help='first_file')
    parser.add_argument('outdir', type=str, help='Second_file')
    args = parser.parse_args()
    print(args.indir)

if __name__ == '__main__':
    main()
