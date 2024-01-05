#!/usr/bin/env python

import argparse

def count_bytes(file_path):
    with open(file_path, 'rb') as file:
        byte_count = len(file.read())

    return byte_count

def count_lines(file_path):
    with open(file_path, 'rb') as file:
        line_count = file.read().count(b'\n')

    return line_count

def count_words(file_path):
    with open(file_path, 'r') as file:
        word_count = sum(len(line.split()) for line in file)

    return word_count

def count_chars(file_path):
    with open(file_path, 'rb') as file:
        char_count = len(file.read().decode('utf-8'))

    return char_count        

def main():
    parser = argparse.ArgumentParser(description='Byte count tool (mywc)')
    parser.add_argument('file', help='Path to the file for byte count')
    parser.add_argument('-c', '--bytes', action='store_true', help='Print the byte count')
    parser.add_argument('-l', '--lines', action='store_true', help='Print line count')
    parser.add_argument('-w', '--words', action='store_true', help='Print word count')
    parser.add_argument('-m', '--characters', action='store_true', help='Print character count')


    args = parser.parse_args()

    try:
        if args.bytes and args.lines and args.words or not args.bytes and not args.lines and not args.words:
            num_bytes = count_bytes(args.file)
            num_lines = count_lines(args.file)
            num_words = count_words(args.file)
            print(f'  {num_lines} {num_bytes} {num_words} {args.file}') 
        elif args.bytes and args.lines:
            num_bytes = count_bytes(args.file)
            num_lines = count_lines(args.file)
            print(f'  {num_lines} {num_bytes} {args.file}')

        elif args.characters:
            char_count = count_chars(args.file)
            print(f'{char_count} {args.file}')

        elif args.words:
            num_words = count_words(args.file)
            print(f'{num_words} {args.file}')  

        elif args.lines:
            num_lines = count_lines(args.file)
            print(f'{num_lines} {args.file}')    

        elif args.words:
            num_words = count_words(args.file)
            print(f'{num_words} {args.file}')              

    except FileNotFoundError:
        print(f"Error: File '{args.file}' not found.")

if __name__ == "__main__":
    main()


