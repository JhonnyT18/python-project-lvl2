# -*- coding: utf-8 -*-


from gendiff.cli import make_parser


def get_diff(diff):
    args = make_parser()
    diff = diff.generate_diff(args.first_file, args.second_file)
    print(diff)
