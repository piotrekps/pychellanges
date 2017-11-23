""" Script for find result of poker game saved in
txt file with following structure:

    - each line is one game
    - each item is one card
    - first 5 items in line is player_1 hand
    - last 5 items in line is player_2 hand

8C TS KC 9H 4S 7D 2S 5D 3S AC
5C AD 5D AC 9C 7C 5H 8D TD KS
3H 7H 6S KC JS QH TD JC 2D 8S

"""

import re
import pdb

PATH = 'C://repositories//files//poker_1.txt'
FIGURES_ORDER = ['A', 'K', 'Q', 'J', 'T', '9', '8',
                 '7', '6', '5', '4', '3', '2']
FIGURES = ''.join(FIGURES_ORDER)
COLORS = 'HDCS'

five_cards = [FIGURES[i:i+5] for i in range(len(FIGURES)-4)]

poker = r'(%s)' % '|'.join((''.join('[%s]' % j + ('([%s])' % COLORS if m == 0 else '\%d' % (n+2)) for m, j in enumerate(i))) for n, i in enumerate(five_cards))
street = r'(%s)' % '|'.join((''.join(j + '[%s]' % COLORS for j in i)) for n, i in enumerate(five_cards))
print('\n', poker)
print('\n', street)
trio = lambda x: r'(([{f}])[{c}]\%d[{c}]\%d[{c}])' % (2+x, 2+x)
couple = lambda x: r'(([{f}])[{c}]\%d[{c}])' % (2+x)

schemes = [
    ('0_poker_krolewski', r'(A([{c}])K\2Q\2J\2T\2)'),
    ('1_poker', poker),
    ('2_kareta', r'(([{f}])[{c}]\2[{c}]\2[{c}]\2[{c}])'),
    ('3_full', r'(%s%s|%s%s)' % (couple(1), trio(3), trio(5), couple(7))),
    ('4_kolor', r'([{f}]([{c}])[{f}]\2[{f}]\2[{f}]\2[{f}]\2)'),
    ('5_street', street),
    ('6_trojka', trio(0)),
    ('7_dwie_pary', '((?<=[{f}][{c}])%s%s|%s(?=[{f}][{c}])%s|%s%s(?=[{f}][{c}]))' % (couple(1), couple(3), couple(5), couple(7), couple(9), couple(11))),
    ('8_para', couple(0)),
    ('9_pusta', ''),
]
schemes_exp = [i[1].format(f=FIGURES, c=COLORS) for i in schemes]


def sort_hand(hand):
    hand_sorted = sorted(hand, key=lambda x: FIGURES_ORDER.index(x[0]))
    return ''.join(hand_sorted)


def find_pattern(hand):
    hand_aggr = [None, None, None]
    for i, exp in enumerate(schemes_exp):
        # if i == 7: pdb.set_trace()
        figure = re.search(exp, hand)
        print('\n\n', i, figure)
        if figure:
            hand_aggr[0] = i
            hand_aggr[1] = figure.group()
            break

    hand_aggr[2] = hand

    print(hand_aggr)

    return hand_aggr


def compare(player_1, player_2, result):
    result_updated = None
    return result_updated


# result = {'gracz_1': 0, 'gracz_2': 0}
#
# with open(PATH) as file:
#     for line in file:
#         hands = line.replace('\n', '').split(' ')
#         hand_1 = find_pattern(sort_hand(hands[:5]))
#         hand_2 = find_pattern(sort_hand(hands[5:]))
#         result = compare(hand_1, hand_2, result)
#
# print(result['gracz_1'])


def test_find_pattern():
    pass

    # poker_krolewski:
    # assert find_pattern('AHKHQHJHTH')[0] == 0

    # # poker:
    # assert find_pattern('KHQHJHTH9H')[0] == 1

    # kareta:
    # assert find_pattern('AHADACASJS')[0] == 2
    # assert find_pattern('AHJDJCJSJH')[0] == 2

    # full:
    # assert find_pattern('AHADAS2H2D')[0] == 3
    # assert find_pattern('AHAD2S2H2D')[0] == 3

    # kolor:
    # assert find_pattern('AHQHJHTH9H')[0] == 4

    # street:
    # assert find_pattern('JHTD9C8S7H')[0] == 5

    # trojka:
    # assert find_pattern('AHADAC2SJS')[0] == 6
    # assert find_pattern('AHKDKCKHJS')[0] == 6
    # assert find_pattern('AHKDQCQHQS')[0] == 6

    # dwie_pary:
    # assert find_pattern('AHKHKD3H3D')[0] == 7
    assert find_pattern('AHADKDKC2S')[0] == 7
    assert find_pattern('AHADKSQDQC')[0] == 7

    # para:
    # assert find_pattern('AHKDKDQC2S')[0] == 8
    # assert find_pattern('AHKDJD3C3S')[0] == 8
    # assert find_pattern('AHKDJD3C3S')[0] == 8

    # pusta:
    # assert find_pattern('')[0] == 9







