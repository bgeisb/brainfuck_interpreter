#!/usr/bin/env python3

import sys


def read_input():
    return sys.stdin.read(1)


storage = [0]
pointer = 0

with open(sys.argv[1]) as first_arg:
    source_code = first_arg.read()

i = 0
while i < len(source_code):
    currentOperation = source_code[i]

    if currentOperation == "<":
        pointer -= 1
        if pointer == -1:
            storage = [0] + storage
            pointer = 0
    elif currentOperation == ">":
        pointer += 1
        if pointer == len(storage):
            storage += [0]
    elif currentOperation == "-":
        storage[pointer] -= 1
    elif currentOperation == "+":
        storage[pointer] += 1
    elif currentOperation == ".":
        sys.stdout.write(chr(storage[pointer]))
        sys.stdout.flush()
    elif currentOperation == ",":
        storage[pointer] = ord(read_input())
    elif currentOperation == "[":
        if storage[pointer] == 0:
            counter = 1
            while counter > 0:
                i += 1
                if source_code[i] == "[":
                    counter += 1
                elif source_code[i] == "]":
                    counter -= 1
            i -= 1
    elif currentOperation == "]":
        if storage[pointer] != 0:
            counter = 1
            while counter > 0:
                i -= 1
                if source_code[i] == "[":
                    counter -= 1
                elif source_code[i] == "]":
                    counter += 1
            i -= 1
    i += 1
