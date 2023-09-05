import argparse

def parse():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str, help='')
    parser.add_argument('second_file', type=str, help='')
    parser.add_argument('-f', '--format', type=set, help='set format of output')
    args = parser.parse_args()
    print(args.first_file)