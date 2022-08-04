#!/usr/bin/python3
#
# riscv_misa_covpt_gen.py    Generates coverpoints for each of the relevant bits
#                            in the extension field of misa register given a valid
#                            RISC-V ISA string containing only ratified extensions
#
# REQUIRES: Python 3.6+ (f'' strings support)
# 
# USAGE: ./riscv_misa_covpt_gen.py <riscv-isa-string>  
#
# AUTHOR: Priyansh Rathi (techiepriyansh@gmail.com)

import sys

def coverpoint_check_misa_bit_set(bit):
    bit_hex = hex(1<<bit)
    return f"misa & {bit_hex} == {bit_hex}"

def coverpoint_check_misa_bit_unset(bit):
    bit_hex = hex(1<<bit)
    return f"misa & {bit_hex} == 0x0"

def get_misa_coverpoints_from_isa_string(riscv_string):
    extensions = ""

    if riscv_string.startswith("rv32") or riscv_string.startswith("rv64"): 
        extensions = riscv_string[4:]
    else: # riscv_string.startswith("rv128")
        extensions = riscv_string[5:]

    # remove additional standard extension names
    if 'z' in extensions: 
        extensions = extensions[:extensions.index('z')] 

    # expand G
    extensions = extensions.replace("g", "imafd")

    # add implied extensions
    if 'q' in extensions and not 'd' in extensions: 
        extensions = extensions.replace("q", "dq") 
    if 'd' in extensions and not 'f' in extensions: 
        extensions = extensions.replace("d", "fd")

    coverpoints = []

    for extension_char in extensions:
        misa_bit = ord(extension_char) - ord('a')
        coverpoints.append(coverpoint_check_misa_bit_set(misa_bit))
        coverpoints.append(coverpoint_check_misa_bit_unset(misa_bit))

    return coverpoints


if __name__ == "__main__":
    riscv_string = sys.argv[1].strip().lower()
    coverpoints = get_misa_coverpoints_from_isa_string(riscv_string)

    for coverpoint in coverpoints:
        print(coverpoint)
