#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Generation of the blockchain 5.0.
"""

import string
from base64 import b64encode

SHA_1_DISCOVER_TAB = "23e2e7dcc98e0866665c2dea042b5e562bb4df98"
FLAG_2 = "FLAG:(C)VestaTech2018"

#blockchain-5.0-poc

def rot(s, n=13):
    """Encode string s with ROT-n, i.e., by shifting all letters n positions.
    When n is not supplied, ROT-13 encoding is assumed."""
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    upper_start = ord(upper[0])
    lower_start = ord(lower[0])
    out = ''
    for letter in s:
        if letter in upper:
            out += chr(upper_start + (ord(letter) - upper_start + n) % 26)
        elif letter in lower:
            out += chr(lower_start + (ord(letter) - lower_start + n) % 26)
        else:
            out += letter
    return(out)

with open("discover.tab") as f:
    lines = f.readlines()

result_lines = []
for index, line in enumerate(lines):
    # add the FLAG_2 at the end
    line = line.replace('\n', FLAG_2)
    # awesome new generation encryption 
    line = "".join(list(map(lambda x: rot(x, n=index%26), line)))
    result_lines.append(line)


#result_lines.append('\n')

# all blocks are connected with SHA_1_DISCOVER_TAB
result_string = SHA_1_DISCOVER_TAB.join(result_lines)

# the final awesome encryption
result_string_base64 = b64encode(result_string.encode())

# write the result in a file
with open("chain", 'w') as f:
    f.write(result_string_base64.decode())
