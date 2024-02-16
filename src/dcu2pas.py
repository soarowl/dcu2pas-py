#!/usr/bin/env python

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        prog="dcu2pas",
        description="Decompile dcu(Delphi Compiled Unit) to pas.",
        epilog="Best wishes for your happiness and success",
    )

    parser.add_argument("files", nargs="+", help="dcu file to decompile")
    args = parser.parse_args()
    for file in args.files:
        print(file)
