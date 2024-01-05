#!/usr/bin/env python

import argparse
import sys

def count_bytes(file_content):
    return len(file_content)

def count_lines(file_content):
    return file_content.count(b"\n")

def count_words(file_content):
    return sum(len(line.split()) for line in file_content.decode("utf-8").splitlines())

def count_chars(file_content):
    return len(file_content.decode("utf-8"))       

def main():
    parser = argparse.ArgumentParser(description="Byte count tool (mywc)")
    parser.add_argument("file", nargs="?", help="Path to the file for byte count")
    parser.add_argument("-c", "--bytes", action="store_true", help="Print the byte count")
    parser.add_argument("-l", "--lines", action="store_true", help="Print line count")
    parser.add_argument("-w", "--words", action="store_true", help="Print word count")
    parser.add_argument("-m", "--characters", action="store_true", help="Print character count")

    args = parser.parse_args()

    try:
        if args.file:
            with open(args.file, "rb") as file:
                file_content = file.read()
        else:
            file_content = sys.stdin.buffer.read()

        if args.bytes and args.lines and args.words:
            num_bytes = count_bytes(file_content)
            num_lines = count_lines(file_content)
            num_words = count_words(file_content)
            print(f"  {num_lines} {num_bytes} {num_words} {args.file or ''}") 

        elif args.bytes and args.lines:
            num_bytes = count_bytes(file_content)
            num_lines = count_lines(file_content)
            print(f"  {num_lines} {num_bytes} {args.file or ''}")

        elif args.bytes:
            num_bytes = count_bytes(file_content)
            print(f"  {num_bytes} {args.file or ''}")

        elif args.characters:
            char_count = count_chars(file_content)
            print(f"  {char_count} {args.file or ''}")

        elif args.words:
            num_words = count_words(file_content)
            print(f"  {num_words} {args.file or ''}")  

        elif args.lines:
            num_lines = count_lines(file_content)
            print(f"  {num_lines} {args.file or ''}")    

        elif args.words:
            num_words = count_words(file_content)
            print(f"  {num_words} {args.file or ''}")    

        elif not args.bytes and not args.lines and not args.words:
            num_bytes = count_bytes(file_content)
            num_lines = count_lines(file_content)
            num_words = count_words(file_content)
            print(f"  {num_lines} {num_bytes} {num_words} {args.file or ''}") 

    except FileNotFoundError:
        print(f"Error: File '{args.file}' not found.")

if __name__ == "__main__":
    main()


