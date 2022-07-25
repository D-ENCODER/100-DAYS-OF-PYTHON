# -*- coding: utf-8 -*-
# @Date    : 2022-07-24 10:49:36
# @Author  : DENCODER (hetcjoshi1684@gmail.com)
# @GitHub    : (https://github.com/D-ENCODER)
# @Twitter    : (https://twitter.com/Hetjoshi1684)
# @Version : 1.0.0

import os

for i in range(1, 365*2 + 1):
    d = str(i) + ' day ago'
    with open('bot.txt', 'a') as file:
        file.write(d)
    os.system('git add bot.txt')
    os.system('git commit --date="' + d + '" -m "first commit"')
os.system('git push -u origin master')
