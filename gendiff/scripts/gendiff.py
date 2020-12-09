#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from gendiff import gendiff
from gendiff.cli import get_parser


def main():
    parser = get_parser()
    args = parser.parse_args()
    diff = gendiff.generate_diff(args.first_file, args.second_file, args.format)  # noqa: E501
    print(diff)


if __name__ == '__main__':
    main()
