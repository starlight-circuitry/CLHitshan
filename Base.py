﻿import random
__author__ = 'Aster'

cons_no_freqs = ['h', 'ɕ', 'C', 'k', 'p', 't', 'n', 'ɲ', 'c', 's', 'Z', 'm', 'l', 'j', 'θ']

cons_no_cluster = [('h', 8324), ('ɕ', 6596), ('C', 4873), ('k', 799), ('p', 7338), ('t', 4133), ('n', 7891),
                   ('ɲ', 7474), ('c', 7083), ('s', 4332), ('Z', 1564), ('m', 4698), ('l', 7037), ('j', 2389),
                   ('θ', 7226)]

vowls_no_freqs = ['y', 'æ', 'e', 'i', 'ɪ', 'o', 'u', 'ʊ', 'ø', 'O', 'I', 'A']

vowls = [('y', 1962), ('æ', 6828), ('e', 7821), ('i', 1214), ('ɪ', 6280), ('o', 7992), ('u', 6399), ('ʊ', 3203),
         ('ø', 1852), ('O', 5036), ('I', 4604), ('A', 7051)]

phons = [('h', 8324), ('ɕ', 6596), ('C', 4873), ('k', 799), ('p', 7338), ('t', 4133), ('n', 7891), ('ɲ', 7474),
         ('c', 7083), ('s', 4332), ('Z', 1564), ('m', 4698), ('l', 7037), ('j', 2389), ('θ', 7226), ('y', 1962),
         ('æ', 6828), ('e', 7821), ('i', 1214), ('ɪ', 6280), ('o', 7992), ('u', 6399), ('ʊ', 3203), ('ø', 1852),
         ('O', 5036), ('I', 4604), ('A', 7051)]

sorted_phons = [('k', 799), ('i', 1214), ('Z', 1564), ('ø', 1852), ('y', 1962), ('j', 2389), ('ʊ', 3203), ('t', 4133),
                ('s', 4332), ('I', 4604), ('m', 4698), ('C', 4873), ('O', 5036), ('ɪ', 6280), ('u', 6399), ('ɕ', 6596),
                ('æ', 6828), ('l', 7037), ('A', 7051), ('c', 7083), ('θ', 7226), ('p', 7338), ('ɲ', 7474), ('e', 7821),
                ('n', 7891), ('o', 7992), ('h', 8324)]

cons_cluster_order = [['p', 't', 'k', 'c', 'θ', 'ɕ', 'h', 'C', 'Z', 's'], ['n', 'm', 'ɲ'], ['l', 'j']]

cons = [('p', 7338, 1), ('t', 4133, 1), ('k', 799, 1), ('c', 7083, 1), ('θ', 7226, 1), ('ɕ', 6596, 1), ('h', 8324, 1),
        ('C', 4873, 1), ('Z', 1564, 1), ('s', 4332, 1), ('n', 7891, 2), ('m', 4698, 2), ('ɲ', 7474, 2), ('l', 7037, 3),
        ('j', 2389, 3)]

# sortedphons = sorted(phons, key=lambda tup : tup[1])
# print(sortedphons)

# for ease of use, C represents affricate tɕ and Z ts, all stops unaspirated, voiced/voiceless allophones
# O represents dipthong oi, I represents ai, A represents ao

#
# for i in cons_no_freqs:
#     for j in i:
#         print('\'' + j + "\', ", end='')


# for i in vowls_no_freqs:
#     for j in i:
#         print('\'' + j + "\', ", end='')


# list = []
#
# for i in range(len(cons_cluster_order)):
#     for j in cons_cluster_order[i]:
#         for k, l in cons:
#             if k == j:
#                 list.append((k, l, (i+1)))
#
# print(list)