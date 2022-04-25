#!/usr/bin/python2
# -*- code: utf-8 -*-
import unicodedata as ud
import codecs

u = u'۱۰۰۰مصیب'

for i, c in enumerate(u):
    print(i, ':', c, '%08x' % ord(c), ud.category(c), ud.name(c))
print(ud.numeric(u[0]))

f = codecs.open(u'فایل.txt', encoding='utf-8', mode='w+')
f.write(u)
f.seek(0)
print(f.read())
f.close()
