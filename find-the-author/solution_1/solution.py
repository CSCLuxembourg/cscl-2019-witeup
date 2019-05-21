#! /usr/bin/python
# -*- coding: utf-8 -*-

# before running this Python script:
# wget https://raw.githubusercontent.com/CSCLuxembourg/vestatech/master/challenges/find-the-author/gift.cap
# tcpflow -r gift.cap


with open("185.031.040.011.00080-010.008.000.006.37558" , "r") as flow:
    data = flow.readlines()

i = 0
for line in data:
    i += 1
    if "Content-Type" in line:
        file_type = line.split("/")[1]
        with open("result", "w") as result:
            result.write("".join(data[i+1:]))
            exit()


# base64 -d result > result.pdf
