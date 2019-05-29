'''
Created on 28 May 2019

@author: Marius
'''

import copy
import math

class MatrGraph:
    """A directed graph, represented by adjacency matrix.
    Vertices are numbers from 0 to n-1"""
    
    def __init__(self, n):
        """Creates a graph with n vertices (numbered from 0 to n-1)
        and no edges"""
        self.matr = []
        self.n = n
        for i in range(n):
            self.matr.append([])
            for j in range(n):
                self.matr[i].append(False)
                
    def parseX(self):
        """Returns an iterable containing all the vertices"""
        nrOfVertices = len(self.matr)
        return range(nrOfVertices)
        
    def parseNout(self, x):
        """Returns an iterable containing the outbound neighbours of x"""
        list =[]
        for i in range(len(self.matr[x])):
            if self.matr[x][i] :
                list.append(i)
        return list
        
    def parseNin(self,x):
        """Returns an iterable containing the inbound neighbours of x"""
        list =[]
        for i in range(len(self.matr)):
            if self.matr[i][x] :
                list.append(i)
        return list
        
    def isEdge(self,x,y):
        """Returns True if there is an edge from x to y, False otherwise"""
        return self.matr[x][y]
    
    def addEdge(self,x,y):
        """Adds an edge from x to y.
        Precondition: there is no edge from x to y"""
        self.matr[x][y] = True
        self.matr[y][x] = True

    def hamCycleUtil(self, path, pos):
        if pos == self.n:
            if self.matr[path[pos-1]][path[0]]==True:
                return True
            else:
                return False
            
        for v in range(1,self.n):
            if self.isSafe(v, pos, path) == True:
                path[pos]=v
                if self.hamCycleUtil(path,pos+1) == True:
                    return True
                path[pos]=-1
            
        return False
    
    def hamCycle(self):
        path = [-1] * self.n
        path[0]=0
        
        if self.hamCycleUtil(path, 1) == False:
            return False
        
        return path
    
    def isSafe(self, v, pos, path):
        if self.matr[path[pos-1]][v]==False:
            return False
        for vertex in path:
            if vertex == v:
                return False
        return True
    
    def printSolution(self, path):
        print ("The Hamiltonian cycle we found is: ")
        for vertex in path:
            print(vertex, end=" ")
        print(path[0], "\n", end="")
    
def readGraph(filename):
    try:
        with open(filename,"r") as file:
            lines = file.readlines()
            data = lines[0].split(" ")
            n = int(data[0])
            m = int(data[1])
            g = MatrGraph(n)
            for i in range(1,m+1):
                if lines[i] != "":
                    params = lines[i].split(" ")
                    x = int(params[0])
                    y = int(params[1])
                    c = int(params[2])
                    g.addEdge(x, y)
        return g
    except FileNotFoundError:
        print("File not found !\n")