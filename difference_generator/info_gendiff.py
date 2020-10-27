# -*- coding: utf-8 -*-


import argparse


def info_gendiff():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.parse_args()
