#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Author: taixiurong(taixiurong@126.com)
"""
import pathlib

import xlwt

with open('/home/taixiurong/work/output/gop/200_result/gop.1_score_result', 'r') as fp1:
    lines = fp1.readlines()

with open('/home/taixiurong/work/output/xs/200_result_dir/result.txt', 'r') as fp2:
    lines2 = fp2.readlines()

xx = {}

for line in lines:
    # print(line)
    bb = line.splitlines(False)
    print(bb[0])
    aa = bb[0].split(' ')
    print(aa[0])
    xx[aa[0]] = [aa[1]]
    # print(xx)

for line2 in lines2:
    bb = line2.splitlines(False)
    print(bb[0])
    aa = bb[0].split(' ')
    print(aa[0])
    print(aa[-1])
    cc = aa[0].split('/')
    dd = cc[-1]
    dd = dd.replace('.wav', '')
    print(dd)
    ll = xx[dd]
    if dd not in xx.keys():
        ll = []

    ll.append(aa[-1])

print(xx)

path = "/home/taixiurong/study_work/python/output/exp_bz_200.xls"
file = pathlib.Path(path)
if file.exists():
    pathlib.Path.unlink(file)

workbook = xlwt.Workbook()
sheet = workbook.add_sheet("bz")

key = list(xx.keys())

size = len(key)

for i in range(1, size):
    sheet.write(i, 0, key[i])
    values = xx[key[i]]
    for j in range(1, len(values) + 1):
        sheet.write(i, j, values[j - 1])

workbook.save(path)
print("sauces!!!")
