#!/usr/bin/env python

import argparse

def count_bytes(file_path):
    with open(file_path, 'rb') as file:  # Open the file in binary mode
        num_bytes = len(file.read())

    return num_bytes

def main():
    parser = argparse.ArgumentParser(description='Byte count tool (mywc)')
    parser.add_argument('file', help='Path to the file for byte count')
    parser.add_argument('-c', '--bytes', action='store_true', help='Print the byte count')

    args = parser.parse_args()

    try:
        if args.bytes:
            num_bytes = count_bytes(args.file)
            print(f'Bytes: {num_bytes}')

    except FileNotFoundError:
        print(f"Error: File '{args.file}' not found.")

if __name__ == "__main__":
    main()


