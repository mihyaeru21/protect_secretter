# -*- coding: utf-8 -*-

import re
import zenhan

re_not = re.compile(u'[\w"\'‘’“”]', re.U)
mask = u'■'

def protect_secret(text):
    protected = re_not.sub(mask, text)
    return protected


if __name__ == '__main__':
    text = u'''声に出して読みたい７つのPython用語 - None is None is None doloopwhile.hatenablog.com/entry/20120120…'''
    print protect_secret(text)

