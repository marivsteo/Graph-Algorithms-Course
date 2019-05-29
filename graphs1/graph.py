'''
Created on 18 Mar 2019

@author: Marius
'''
import copy
import math

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Graph:
    def __init__(self, n, m):
        '''
        Creates a graph with n vertices 
        (numbered from 0 to n-1 and m edges
        '''
        self.__outbound={}
        self.__inbound={}
        self.__costs={}
        self.n = n
        self.m = m
        for i in range(n):
            self.__outbound[i]=[]
            self.__inbound[i]=[]
        #for i in range(0,m):
        #self.__costs[i]=[]
            
    def isEdge(self, x, y):
        '''
        returns True if there is an edge from x to y
        '''
        return y in self.__outbound[x]
    
    def isVertex(self, x):
        '''
        returns True if x is a vertex
        '''
        return x in self.__outbound.keys()
    
    def addEdge(self, x, y, c):
        '''
        adds an edge to the graph
        pre: the edge from x to y should not be in the graph
             x and y should be vertices in the graph
        '''
        if x not in self.__outbound.keys() or y not in self.__outbound.keys() or y in self.__outbound[x]:
            return False
            print("X or Y is not a vertex!")
        self.__outbound[x].append(y)
        self.__inbound[y].append(x)
        self.__costs[(x,y)] = c
        #print(x, " ", y, " ", c)
        
    def addVertex(self, x):
        '''
        adds a vertex to the graph
        pre: x should not be a vertex
        '''
        if x in self.__outbound.keys():
            return False
            print("Already a vertex in the graph!")
        else:
            self.__inbound.update({x : 0})
            self.__outbound.update({x:0})
            self.__outbound[x] = []
            self.__inbound[x] = []
            self.n += 1
            #for i in self.__outbound.keys():
            #print(i, " ")
    
    def parseVertices(self):
        '''
        returns all vertices
        '''
        vertices=[]
        for i in self.__inbound.keys():
            vertices.append(i)
        return vertices
    
    def numberVertices(self):
        '''
        returns the number of vertices
        '''
        return self.n
    
    def deleteVertex(self, x):
        '''
        deletes a vertex x
        x should be a vertex
        '''
        if x not in self.__inbound.keys():
            return False
            print("x is not a vertex!")
        for i in self.parseVertices():
            if x in self.parseOutbound(i):
                self.__outbound[i].remove(x)
                self.deleteEdge(i, x)
            if x in self.parseInbound(i):
                self.__inbound[i].remove(x)
                self.deleteEdge(x, i)
        del self.__inbound[x]
        del self.__outbound[x]
        return 1
        
    
    def deleteEdge(self, a, b):
        '''
        deletes the edge from a to b
        a and b should be vertices and (a, b) should be an edge
        '''
        if a not in self.__outbound.keys() or b not in self.__outbound.keys() or b not in self.__outbound[a]:
            return False
            print("a or b is not a vertex!")
        self.__inbound[b].remove(a)
        self.__outbound[a].remove(b)
        del self.__costs[(a,b)]
        return 1
    
    def inDegree(self, x):
        '''
        returns the in-degree of vertex x
        x should be a vertex
        '''
        c = 0
        if x not in self.__inbound.keys():
            return False
            print("x is not a vertex!")
        for i in self.__inbound[x]:
            c+=1
        return c
    
    def outDegree(self, x):
        '''
        returns the out-degree of vertex x 
        x should be a vertex
        '''
        c = 0
        if x not in self.__inbound.keys():
            return False
            print("x is not a vertex!")
        for i in self.__outbound[x]:
            c+=1
        return c
    
    def parseInbound(self, x):
        '''
        x should be a vertex
        returns the list of inbound vertices
        '''
        if x not in self.__outbound.keys():
            return False
            print("x is not a vertex!")
        vertices=[]
        for i in self.parseVertices():
            if x in self.__outbound[i]:
                vertices.append(i)
        return vertices
    
    def parseOutbound(self, x):
        '''
        x should be a vertex
        returns the list of outbound vertices
        '''
        if x not in self.__outbound.keys():
            return False
            print("x is not a vertex!")
        vertices=[]
        for i in self.__outbound[x]:
            vertices.append(i)
        return vertices
    
    def updateCost(self, a, b, c):
        '''
        the edge (a, b) should be in the graph
        updates the cost of the edge (a, b) to c
        '''
        if b not in self.__outbound[a]:
            return False
            print("(a, b) is not an edge!")
        self.__costs[(a,b)] = c
        #return self.__costs[(a,b)]
    
    def copyGraph(self):
        '''
        copies the graph to graph2
        '''
        n = self.n
        m = self.m
        graph2 = Graph(n, m)
        graph2.__inbound = copy.deepcopy(self.__inbound)
        graph2.__outbound = copy.deepcopy(self.__outbound)
        graph2.__costs = copy.deepcopy(self.__costs)
        
        return graph2
    
    def checkCost(self, a, b):
        '''
        returns the cost of the edge from a to b
        a and b should be vertices
        (a, b) should be an edge
        '''
        return self.__costs[(a,b)]
    
    
    def minLenPath(self, s, e):
        '''
        returns the lowest length path between vertices s and e
        pre: s and e should be vertices in the graph
        '''
        q = Queue()
        visited = []
        prev = {}
        dist = {}
        found = 0
        for i in range(self.n):
            dist[i]=0
            prev[i]=-1
            
        visited.append(s)
        q.enqueue(s)
        while not q.isEmpty() and found != 1:
            x = q.dequeue()
            for i in self.parseOutbound(x):
                if i not in visited:
                    q.enqueue(i)
                    visited.append(i)
                    prev[i]=x
                    dist[i]=dist[x]+1
                    if i == e:
                        found = 1
        if dist[e] != 0:
            print("The path from ",s," to ",e," is: ", end="")
            list=[]
            x = e
            while prev[x] != -1:
                list.append(x)
                x = prev[x]
            list.append(s)
            while(len(list)>0):
                x = list.pop(len(list)-1)
                print(x, end=" ")
            print("\n", end="")
            return dist[e]
        else:
            return -1
    
    
    def ford(self, s, e):
        '''
        finds a minimum cost walk between vertices s and e
        pre: s and e should be vertices in the graph
             if there are negative cost cycles accessible from the starting vertex a message is printed
        '''
        prev = {}
        dist = {}
        changed = 1
        cycle = []
        for i in range(self.n):
            dist[i]=math.inf
            prev[i]=-1
            cycle.append(0)
        dist[s] = 0
        while changed == 1:
            changed = 0
            for (x,y) in self.__costs.keys():
                if dist[y] > dist[x] + self.__costs[(x,y)]:
                    dist[y] = dist[x] + self.__costs[(x,y)]
                    prev[y] = x
                    changed = 1
                    if cycle[y]>self.n:
                        print("Negative cycle found!\n")
                        return False
                    else:
                        cycle[y]+=1
        '''
        another method to check for negative cycles
        for (x,y) in self.__costs.keys():
            if dist[y] > dist[x] + self.__costs[(x,y)]:
                print("Negative cycle found!\n")
                return False
        '''
           
        if dist[e] != math.inf:
            print("The lowest cost walk from ",s," to ",e," is: ", end="")
            list=[]
            x = e
            while prev[x] != -1:
                list.append(x)
                x = prev[x]
            list.append(s)
            while(len(list)>0):
                x = list.pop(len(list)-1)
                print(x, end=" ")
            print("\n", end="")
            return dist[e]
        else:
            print("There is no walk from ",s," to ",e,"\n")
            return False
    
    def topoSort(self):
        '''
        performs a topological sort on the graph given as parameter
        input: a directed graph
        output: a list of vertices in topological order or -1 if
        the graph has cycles
        '''
        sorted=[]
        q = Queue()
        count={}
        for x in self.parseVertices():
            count[x]=self.inDegree(x)
            if count[x]==0:
                q.enqueue(x)
                
        while not q.isEmpty():
            x = q.dequeue()
            sorted.append(x)
            for y in self.parseOutbound(x):
                count[y]-=1
                if count[y]==0:
                    q.enqueue(y)
                    
        if len(sorted) < self.numberVertices():
            return -1
        
        return sorted
        
        
        
    def highestCost(self, s, e):
        '''
        Finds a highest cost path between s and e
        pre: s and e should be vertices in the graph
        '''
        dist ={}
        prev = {}
        for i in range(self.n):
            dist[i]=-math.inf
            prev[i]=-1
        dist[s]=0
        topo=self.topoSort()
        for x in topo:
            if x == e:
                break
            for y in self.parseOutbound(x):
                if dist[y] < dist[x] + self.__costs[(x,y)]:
                    dist[y] = dist[x] + self.__costs[(x,y)]
                    prev[y] = x          
    
        if dist[e] != -math.inf:
            print("The highest cost path from ",s," to ",e," is: ", end="")
            list=[]
            x = e
            while prev[x] != -1:
                list.append(x)
                x = prev[x]
            list.append(s)
            while(len(list)>0):
                x = list.pop(len(list)-1)
                print(x, end=" ")
            print("\n", end="")
            return dist[e]
        else:
            print("There is no path from ",s," to ",e,"\n")
            return False

def readGraph(filename):
    try:
        with open(filename,"r") as file:
            lines = file.readlines()
            data = lines[0].split(" ")
            n = int(data[0])
            m = int(data[1])
            g = Graph(n, m)
            for i in range(1,m+1):
                if lines[i] != "":
                    params = lines[i].split(" ")
                    x = int(params[0])
                    y = int(params[1])
                    c = int(params[2])
                    g.addEdge(x, y, c)
        return g
    except FileNotFoundError:
        print("File not found !\n")