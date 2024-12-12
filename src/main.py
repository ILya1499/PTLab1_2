# -*- coding: utf-8 -*-
import argparse
import sys
from CalcRating import CalcRating
from CalcRatingOtl import CalcRatingOtl
from TextDataReader2 import TextDataReader2


def get_path_from_arguments(args) -> dict:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args


def main():
    args = get_path_from_arguments(sys.argv[1:])
    path = args.path
    # reader = TextDataReader()
    # students = reader.read(path)
    # print("Students: ", students)
    # rating = CalcRating(students).calc()
    # print("Rating: ", rating)

    reader = TextDataReader2()
    students = reader.read(path)
    so = CalcRatingOtl(students).so()
    print("Student:", so)


if __name__ == "__main__":
    main()
