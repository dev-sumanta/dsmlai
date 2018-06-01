# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 12:17:22 2017

@author: Samar
"""

import re
import math


def re_match_group(m):
    if m is not None:
        return m.group()
    else:
        return None


# matching strings with match
m = re.match('some', 'some')
if m is not None:
    print('pattern and string similar ', m.group())
print(type(m))

m_match_longer = re.match('some', 'some longer string')
print('stirng longer than pattern',
      re_match_group(m_match_longer))
# m's type is a match object


# if we do not have a match , AttributeError
# will be raised on calling group
m_none = re.match('some', 'else')
# print(m_none.group())

# match vs search - beginning vs all
m_match_inside_none = re.match('some', 'a string some')
# match has to find pattern at the beginning
print(re_match_group(m_match_inside_none))
# search can find it anywhere
print(re_match_group(re.search('some', 'a string some')))
print(re_match_group(re.search('some',
                               'a string some with more than one some')))
# findall to find all matches
all_somes = re.findall('some', 'a string some with ' +
                       'more than one some')
print(all_somes, type(all_somes))

# matching more than one string using alteration |
bt = 'bat|bet|bit'
m = re.match(bt, 'bat')
print(re_match_group(m))
m = re.match(bt, 'bet')
print(re_match_group(m))
m = re.match(bt, 'bit')
print(re_match_group(m))

# matching any single character .
anying = '.ing'
print(re_match_group(re.match(anying, 'ring')))
print(re_match_group(re.match(anying, 'sing')))

# use escape \ to match special character
print(re_match_group(re.match('3\.14', str(math.pi))))

# character classes []
m = re.match('[cr][23][dp][o2]', 'r3d2')
print(re_match_group(m))

# quantifiers and greedy and lazy behaviour
# *, +, ? are greedy operators
# so in the examples below, as many as possible of cs will
# be matched
print(re.match('abc+', 'abcccd').group())
print(re.match('abc*', 'abcccd').group())

# ? will match 0 or one character
print(re.match('abc?', 'abcccd').group())

# *, + both followed by ? become lazy - as less as
# is needed to match will be used
print(re.match('abc+?', 'abcccd').group())  # will match abc
print(re.match('abc*?', 'abcccd').group())  # will match ab

'''
Reluctant/lazy quantifiers give up to entertain other quantifiers
'''
print(re.match('abc+?d', 'abcccd').group())  # entire string matched
print(re.match('abc*?d', 'abcccd').group())  # entire string matched

patt = '\w+@(\w+\.)?\w+\.com'
# the ? is greedy and it matches xxx. but when it reaches
# \.com it gives it up so that it uses the 0 option
# the regex engine backtracks and the whole expression
# can match
print(re.match(patt, 'nobody@xxx.com').group())
# since the regex gave back here groups will be none
print(re.match(patt, 'nobody@xxx.com').groups())
# here we will hvae one match for the ? and the rest matches
print(re.match(patt, 'some@xxx.yyy.com').group())
# here patt can match xxx and the rest matches so
# groups will give us ('xxx', )
print(re.match(patt, 'some@xxx.yyy.com').groups())
# the one below fails to match
print(re.match(patt, 'some@xxx.yyy.zzz.com').group())
# we modifiy the pattern so that we can have
# any number of parts to the domain
pattm = '\w+@(\w+\.)*\w+\.com'
print(re.match(pattm, 'some@xxx.yyy.zzz.com').group())
# in this instance the last bit satisfying (\w+\.)
# will be the group matched
print(re.match(pattm, 'some@xxx.yyy.zzz.com').groups())
pattmq = '\w+@(\w+\.)*?\w+\.com'
print(re.match(pattmq, 'some@xxx.yyy.zzz.com').group())
# same as mentioned for pattm above
print(re.match(pattmq, 'some@a.b.c.xxx.yyy.zzz.com').groups())

# groups
patt_w_groups = '\w+@(\w+\.)*?(\w+)\.com'
# same logic as for pattm and pattmq above
# so we have (\w+) matching zzz and last match to yyy
m_groups = re.match(patt_w_groups, 'some@xxx.yyy.zzz.com').groups()
print(m_groups)
# the groups are available with group and indexing
# beginning from 1
print(re.match(patt_w_groups, 'some@xxx.yyy.zzz.com').group(1))

m_groups_n = re.match(patt_w_groups, 'some@a.b.c.xxx.yyy.zzz.com').groups()
print(m_groups_n)
print(re.match(pattm, 'some@xxx.yyy.zzz.com').groups())

m_search = re.search('^The', 'The end')
print(re_match_group(m_search))

m_search_beg_fail = re.search('^The', 'not at The beginning')
print(re_match_group(m_search_beg_fail))

# matching on word boundaries
# since \b is both an ascii character and a regex symbol
# we need to either escape it or use raw strings
m_word_boundary = re.search('\\bhear', 'wear you hear')
print(re_match_group(m_word_boundary))
m_word_boundary = re.search(r'\bhear', 'wear you hear')
print(re_match_group(m_word_boundary))

m_word_boundary_fail = re.search(r'\bhear', 'wear from shear')
print(re_match_group(m_word_boundary_fail))


# findall and finditer
s = 'This and that.'
print(re.findall(r'(th\w+) and (th\w+)', s, re.I))
# finditer iterates over match objects
# in contrast to findall which returns a list
print(next(re.finditer(r'(th\w+) and (th\w+)', s, re.I)).group())
print(next(re.finditer(r'(th\w+) and (th\w+)', s, re.I)).groups())
print(next(re.finditer(r'(th\w+) and (th\w+)', s, re.I)).group(1))
print(next(re.finditer(r'(th\w+) and (th\w+)', s, re.I)).group(2))

# replcacing with sub and subn
print(re.sub('X', 'Mr. Smith', 'attn: X\n\nDear X,\n'))
# sbun will also give us the number of replacements
print(re.subn('X', 'Mr. Smith', 'attn: X\n\nDear X,\n'))

print(re.sub(r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})',
             r'\2/\1/\3', '2/20/91'))
print(re.sub(r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})',
             r'\2/\1/\3', '2/20/1991'))

# extension notations
# (?ilMsux) can be used to pass flags
print(re.findall(r'(?i)find', 'find Find Findings by finder'))

# the m flag enables search across multiple lines
print(re.findall(r'(?im)(^th[\w]+)', """
This line is the first
another line
that line was some other line
"""))

print(re.findall(r'^th.+', '''The first line
the second line
the third line''', re.I | re.MULTILINE))

# ?s is equivalent to re.S/DOTALL and will
# match the \n character
print(re.findall(r'(?s)th.+', '''
           The first line
           the second line
           the third line
           '''))

# the verbose flag ?x enables creation of nicely
# formatted regexes. White space will be ignored
# they are not within a character class backslash escaped
print(re.search(r'''(?x)
\((\d{3})\)  # area code
[ ]  # space
(\d{3})  # prefix
-      # dash
(\d{4}) # endpoint number
''', '(800) 224-3344223').groups())


# (?:...) notation to group parts of a regex but
# not save them
print(re.findall(r'http://(?:\w+\.)*(\w+\.com)',
                 'http://google.com http://www.google.com'
                 'http://www.ml.datascience.cloudera.com'))

# ?P<name> can be used to save named groups
# rather than incrementing numbered groups
print(re.sub(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})',
             '(\g<areacode>) \g<prefix>-xxxx', '(800) 555-1212'))

# ?P=name can be used to reuse a pattern
# specified earlier using ?P<name>
print(re.match(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4}) (?P=prefix)',
               '(800) 234-3394 234').groups())

# using a compiled regex
re_compiled = re.compile('(\d{3})-(\d{4})')
print(re_compiled.match('300-2144').groups())
