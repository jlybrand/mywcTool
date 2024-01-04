#!/usr/bin/env python

import argparse

def count_bytes(file_path):
    with open(file_path, 'rb') as file:
        num_bytes = len(file.read())

    return num_bytes

def count_lines(file_path):
    with open(file_path, 'rb') as file:
        num_lines = file.read().count(b'\n')

    return num_lines

def main():
    parser = argparse.ArgumentParser(description='Byte count tool (mywc)')
    parser.add_argument('file', help='Path to the file for byte count')
    parser.add_argument('-c', '--bytes', action='store_true', help='Print the byte count')
    parser.add_argument('-l', '--lines', action='store_true', help='Print line count')

    args = parser.parse_args()

    try:
        if args.bytes and args.lines:
            num_bytes = count_bytes(args.file)
            num_lines = count_lines(args.file)
            print(f'  {num_lines} {num_bytes} {args.file}')

        elif args.bytes:
            num_bytes = count_bytes(args.file)
            print(f'{num_bytes} {args.file}')

        elif args.lines:
            num_lines = count_lines(args.file)
            print(f'{num_lines} {args.file}')    

    except FileNotFoundError:
        print(f"Error: File '{args.file}' not found.")

if __name__ == "__main__":
    main()


