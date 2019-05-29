from graph import MatrGraph, readGraph
from console import Console

'''
Created on 28 May 2019

@author: Marius
'''

g = readGraph("graphHam1.txt")
#g = readGraph("graph1k.txt")
c = Console(g)
c.run()