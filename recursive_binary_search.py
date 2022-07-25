# -*- coding: utf-8 -*-
# @Date    : 2022-07-23 11:50:14
# @Author  : DENCODER (hetcjoshi1684@gmail.com)
# @GitHub    : (https://github.com/D-ENCODER)
# @Twitter    : (https://twitter.com/Hetjoshi1684)
# @Version : 1.0.0

from jovian.pythondsa import evaluate_test_cases

test = [{'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}, 'output': 3},
        {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0],
                   'query': 1}, 'output': 6},
        {'input': {'cards': [4, 2, 1, -1], 'query': 4}, 'output': 0},
        {'input': {'cards': [3, -1, -9, -127], 'query': -127}, 'output': 3},
        {'input': {'cards': [6], 'query': 6}, 'output': 0},
        {'input': {'cards': [9, 7, 5, 2, -9], 'query': 4}, 'output': -1},
        {'input': {'cards': [], 'query': 7}, 'output': -1},
        {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 3},
         'output': 7},
        {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
                   'query': 6},
         'output': 2}]


def test_location(cards, query, mid):
    mid_number = cards[mid]
    print("mid:", mid, ", mid_number:", mid_number)
    if mid_number == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'


def locate_card_binary(cards, query):
    lo, hi = 0, len(cards) - 1

    while lo <= hi:
        print("lo:", lo, ", hi:", hi)
        mid = (lo + hi) // 2
        result = test_location(cards, query, mid)

        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
    return -1


evaluate_test_cases(locate_card_binary, test)
