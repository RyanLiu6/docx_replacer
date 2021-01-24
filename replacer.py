#!/usr/bin/env python3
import argparse

from lib.utils import *
from lib.parser import Parser


def main():
    parser = argparse.ArgumentParser(
        description="Parse and replace input for a docx file.")
    parser.add_argument(
        "file_path", help="Absolute path to docx file.")
    parser.add_argument(
        "old", help="Old value to find and be replaced.")
    parser.add_argument(
        "new", help="New value to replace with.")
    parser.add_argument(
        "--type", choices=REPLACE_TYPES,
        default=REPLACE_TYPES[0], help="Type of replacing needed. Defaults to all")

    args = parser.parse_args()

    parser = Parser(file_path=args.file_path)
    parser.replace(
        old=args.old,
        new=args.new,
        input_type=args.type)


if __name__ == "__main__":
    main()
