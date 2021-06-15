from os import path

from matplotlib import colors

import seqfold

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

import matplotlib

import random

# 设置matplotlib正常显示中文和负号
matplotlib.rcParams['font.sans-serif']=['SimHei']   # 用黑体显示中文
matplotlib.rcParams['axes.unicode_minus']=False     # 正常显示负号

print(seqfold.__file__)

DIR = path.dirname(path.realpath(__file__))

data = []
seqs_score_under_6 = []
score_num = {}
for index in range(100, 161):
    results = []
    with open(path.join(DIR, "rand_dna_seq_result", "rand_dna_seq_result_" + str(index) + ".csv"), 'r',encoding='utf-8-sig') as f_input:
        for line in f_input:
            score =  int(round(10 - 25 * 2 * line.count('[') / index, 2))
            lastcomma_index = line.rindex(',')
            seq = line[lastcomma_index + 1:]
            line = str(score) + ',' + seq
            results.append(line)
            data.append(score)
            if str(score) not in score_num:
                score_num[str(score)] = 1
            else:
                if score <= 5:
                    score_num[str(score)] += 10
                score_num[str(score)] += 1

    with open(path.join(DIR, "..", "examples","rand_dna_seq_result_" + str(index) + ".csv"), "w") as ex:
        for item in results[1:]:
            ex.write(item)

seqs_score_under_6.sort(key=lambda x:int(x[0]))
for index in range(161, 200):
    times = 0
    with open(path.join(DIR, "..", "examples","rand_dna_seq_result_" + str(index) + ".csv"), "w") as ex:
            for item_ in seqs_score_under_6:
                item = list(item_)
                if times < 1000:
                    for i in range(5):
                        pos = random.randint(3, len(item) - 2)
                        if item[pos] == 'A': item[pos] = 'T'
                        elif item[pos] == 'T': item[pos] = 'A'
                        elif item[pos] == 'C': item[pos] = 'G'
                        else: item[pos] = 'C'
                    ex.write(''.join(item))
                    times += 1

# print(min(data))
# plt.hist(data, bins=40, facecolor="blue", edgecolor="black", alpha=0.7)
# # 显示横轴标签
# plt.xlabel("score")
# # 显示纵轴标签
# plt.ylabel("frequency")
# # 显示图标题
# plt.title("frequency-score.hist")
# plt.show()

# scores = ['0-3', '4', '5', '6', '7', '8', '9']
# nums = [945, 2410, 12177, 11123, 16843, 16803, 12270]
# colors = ['red', 'gray', 'yellow', 'blue', 'hotpink', 'goldenrod', 'olivedrab']
# plt.figure(figsize=(10,10), dpi=100)
# plt.pie(nums, labels=scores, autopct="%1.2f%%", colors=colors, textprops={'fontsize':12}, labeldistance=1.05)
# plt.legend(fontsize=12)
# plt.title('The initial distribution of the scores', fontsize=12)
# plt.show()