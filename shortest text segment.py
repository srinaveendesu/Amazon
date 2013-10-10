#!/usr/bin/python
import re

if __name__ ==  '__main__':
    text = raw_input()
    k = int(raw_input())

    h = []

    para = text.split()
    d = dict()
    for i in xrange(0,k):
        d[raw_input()] = -1

    result = 20000001
    f_x = -1
    f_y = -1

    for i in xrange(0,len(para)):
        word = re.sub('[^A-Za-z0-9]','',para[i])
        word = word.lower()

        if word not in d:
            continue

        d[word] = i

        x = min(d.values())
        y = max(d.values())

        if ( x == -1 ):
            continue
        else:
            if ( result > y-x+1 ):
                f_x, f_y, result = x, y, y-x+1

        if result == len(d):
            break

    if f_x == -1:
        print 'NO SUBSEGMENT FOUND'
    else:

        x = " ".join(para[f_x:f_y+1] )
        print re.sub('[^A-Za-z  ]','',x)
































