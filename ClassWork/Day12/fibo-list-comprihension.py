#!/usr/bin/python

fibo_series = [0,1]
[fibo_series.append([fibo_series[-1]+fibo_series[-2]]) for x in range(100) ]
print fibo_series
