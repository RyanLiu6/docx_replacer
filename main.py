#!/usr/bin/env python3

import argparse

from parser.parser import Parser


def main():
    parser = argparse.ArgumentParser(
        description="Parse and replace input for a docx file")
    parser.add_argument(
        "file_path", help="Absolute path to docx file")
    parser.add_argument(
        "old", help="Old value to find and be replaced")
    parser.add_argument(
        "new", help="New value to replace with")

    args = parser.parse_args()
    print(args)

    parser = Parser(file_path=args.file_path)
    parser.paragraph_replace(
        old=args.old,
        news=args.new)


if __name__ == "__main__":
    main()
