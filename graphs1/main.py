from graph import Graph, readGraph
from console import Console

'''
Created on 18 Mar 2019

@author: Marius
'''

#g = readGraph("graph_file2.txt")
#g = readGraph("graph1k.txt")
g = readGraph("graph10k.txt")
c = Console(g)
c.run()