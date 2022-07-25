# -*- coding: utf-8 -*-
# @Date    : 2022-07-23 12:00:40
# @Author  : DENCODER (hetcjoshi1684@gmail.com)
# @GitHub    : (https://github.com/D-ENCODER)
# @Twitter    : (https://twitter.com/Hetjoshi1684)
# @Version : 1.0.0

from jovian.pythondsa import evaluate_test_cases


def anagram(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    return sorted(word1) == sorted(word2)


tests = [
    {'input': {'word1': 'cinema', 'word2': 'iceman'}, 'output': True},
    {'input': {'word1': 'cool', 'word2': 'loco'}, 'output': True},
    {'input': {'word1': 'men', 'word2': 'women'}, 'output': False}
]

evaluate_test_cases(anagram, tests)
