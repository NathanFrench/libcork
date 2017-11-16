# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------
# Copyright © 2017, libcork authors
# All rights reserved.
#
# Please see the COPYING file in this distribution for license details.
# ----------------------------------------------------------------------

# Generates some test cases for our u128 types.

from __future__ import print_function

import random
import sys

test_count = 25000
random.seed()

def random_128():
    result = 0
    for i in range(4):
        result = result << 32
        result = result + int(random.random() * 2**32)
    return result

def dec_128(value):
    return format(value, "40d")

def hex_128(value):
    return ("UINT64_C(0x" + format(value >> 64, "016x") + "), " +
            "UINT64_C(0x" + format(value & 0xffffffffffffffff, "016x") + ")")


def create_one_add_test_case():
    lhs = random_128()
    rhs = random_128()
    result = (lhs + rhs) % 2**128
    print()
    print("/*    ", dec_128(lhs), sep="")
    print(" *  + ", dec_128(rhs), sep="")
    print(" *  = ", dec_128(result), sep="")
    print(" */")
    print("{", sep="")
    print("    ", hex_128(lhs), ",", sep="")
    print("    ", hex_128(rhs), ",", sep="")
    print("    ", hex_128(result), sep="")
    print("},", sep="")


def create_one_sub_test_case():
    lhs = random_128()
    rhs = random_128()
    if lhs < rhs:
        lhs, rhs = rhs, lhs
    result = (lhs - rhs) % 2**128
    print()
    print("/*    ", dec_128(lhs), sep="")
    print(" *  - ", dec_128(rhs), sep="")
    print(" *  = ", dec_128(result), sep="")
    print(" */")
    print("{", sep="")
    print("    ", hex_128(lhs), ",", sep="")
    print("    ", hex_128(rhs), ",", sep="")
    print("    ", hex_128(result), sep="")
    print("},", sep="")


if len(sys.argv) == 1:
    print("Usage: create-u128-test-cases.py [operator]")
    sys.exit(1)

if len(sys.argv) > 2:
    sys.stdout = open(sys.argv[2], 'w')

print("/* This file is autogenerated.  DO NOT EDIT! */")

for i in range(test_count):
    if sys.argv[1] == "add":
        create_one_add_test_case()
    elif sys.argv[1] == "sub":
        create_one_sub_test_case()