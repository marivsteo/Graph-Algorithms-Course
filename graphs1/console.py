from graph import Graph

'''
Created on 18 Mar 2019

@author: Marius
'''
class Console():
    

    def __help(self):
        self.__menu()
    
    
    def __isVertexUI(self, params):
        if len(params) != 1:
            print("Invalid number of parameters! \n")
            return
        x = int(params[0])
        if self.__graph.isVertex(x):
            print("It is a vertex! \n")
        else:
            print("It is not! \n")
    
    def __copyGraphUI(self, params):
        if len(params) != 0:
            print("Invalid number of parameters! \n")
            return
        graph2 = self.__graph.copyGraph()
        print("Graph was copied into graph2")
    
    def __updateCostUI(self, params):
        if len(params) != 3:
            print("Invalid number of parameters! \n")
            return
        a = int(params[0])
        b = int(params[1])
        c = int(params[2])
        d = self.__graph.updateCost(a, b, c)
        print(d)
    
    
    def __parseVerticesUI(self, params):
        if len(params) != 0:
            print("Invalid number of parameters! \n")
            return
        vertices = self.__graph.parseVertices()
        for i in vertices:
            print(i," ")
    
    
    def __checkCostUI(self, params):
        if len(params) != 2:
            print("Invalid number of parameters! \n")
            return
        a = int(params[0])
        b = int(params[1])
        c = self.__graph.checkCost(a, b)
        print(c)
    

    def __bfsUI(self, params):
        if len(params) != 2:
            print("Invalid number of parameters! \n")
            return
        s = int(params[0])
        e = int(params[1])
        if not self.__graph.isVertex(s) or not self.__graph.isVertex(e):
            print("One or more of these vertices are not in the graph!\n")
            return
        l = self.__graph.minLenPath(s, e)
        if l != -1:
            print("The length of the path from ",s," to ", e, " is: ", l)
        else:
            print("No minimum length path from ",s," to ", e,"\n")
    
    
    def __fordUI(self, params):
        if len(params) != 2:
            print("Invalid number of parameters! \n")
            return
        s = int(params[0])
        e = int(params[1])
        if not self.__graph.isVertex(s) or not self.__graph.isVertex(e):
            print("One or more of these vertices are not in the graph!\n")
            return
        l = self.__graph.ford(s, e)
        if l != False:
            print("The length of the path from ",s," to ", e, " is: ", l,"\n")
    
    
    def __topoSortUI(self, params):
        if len(params) != 0:
            print("Invalid number of parameters! \n")
            return
        if self.__graph.topoSort() == -1:
            print("The graph contains cycles! \n")
            return
        else:
            list=self.__graph.topoSort()
            for x in list:
                print(x, end=" ")
            print("\n", end="")
    
    
    def __highCostUI(self, params):
        if len(params) != 2:
            print("Invalid number of parameters! \n")
            return
        s = int(params[0])
        e = int(params[1])
        if not self.__graph.isVertex(s) or not self.__graph.isVertex(e):
            print("One or more of these vertices are not in the graph!\n")
            return
        if self.__graph.topoSort() == -1:
            print("The graph is not a DAG! \n")
            return
        l = self.__graph.highestCost(s, e)
        if l != False:
            print("The length of the path from ",s," to ", e, " is: ", l,"\n")
    
    
    def __init__(self, Graph):
        self.__graph = Graph
        self.__commands = {"addVertex" : self.__addVertexUI,
                           "deleteVertex" : self.__deleteVertexUI,
                           "addEdge" : self.__addEdgeUI,
                           "deleteEdge" : self.__deleteEdgeUI,
                           "vertexNumber" : self.__vertexNumberUI,
                           "isEdge" : self.__isEdgeUI,
                           "isVertex" : self.__isVertexUI,
                           "inDegree" : self.__inDegreeUI,
                           "outDegree" : self.__outDegreeUI,
                           "parseInbound" : self.__parseInboundUI,
                           "parseOutbound" : self.__parseOutboundUI,
                           "updateCost" : self.__updateCostUI,
                           "copyGraph" : self.__copyGraphUI,
                           "parseVertices" : self.__parseVerticesUI,
                           "checkCost" : self.__checkCostUI,
                           "bfs" : self.__bfsUI,
                           "ford" : self.__fordUI,
                           "topoSort" : self.__topoSortUI,
                           "highCost" : self.__highCostUI}
        
    
    def __menu(self):
        
        print("\n To check if from x to y there is an edge enter command: 'isEdge x y' \n")
        print("To add a vertex x enter command 'addVertex x' \n")
        print("To delete a vertex x enter command 'deleteVertex x' \n")
        print("To add an edge from x to y enter command 'addEdge x y' \n")
        print("To delete an edge from x to y enter command 'deleteEdge x y' \n")
        print("To see the number of vertices enter command 'vertexNumber' \n")
        print("To see the in degree of vertex x enter command 'inDegree x' \n")
        print("To see the out degree of vertex x enter command 'outDegree x' \n")
        print("To see all inbound edges of vertex x enter command 'parseInbound x' \n")
        print("To see all outbound edges of vertex x enter command 'parseOutbound x' \n")
        print("To change the cost of an edge (a, b) to c enter command 'updateCost a b c' \n")
        print("To make a copy of the graph enter command 'copyGraph' \n")
        print("To parse all vertices enter command 'parseVertices' \n")
        print("To check the cost of the edge from a to b enter command 'checkCost a b' \n")
        print("To see the minimum length path from a to b enter command 'bfs a b' \n")
        print("To see the lowest cost walk from a to b enter command 'ford a b' \n")
        print("To see the vertices in topological order or if the graph is a DAG enter command: 'topoSort' \n")
        print("To see the highest cost path between a and b enter command 'highCost a b' \n")
        print("For help enter command 'Help' \n")
    
    def __isEdgeUI(self, params):
        if len(params) != 2:
            print("Invalid number of parameters! \n")
            return
        x = int(params[0])
        y = int(params[1])
        if self.__graph.isEdge(x, y):
            print("It is an edge! \n")
        else:
            print("It is not! \n")
    

    def __addVertexUI(self, params):
        if len(params) != 1:
            print("Invalid number of parameters! \n")
            return
        x = int(params[0])
        self.__graph.addVertex(x)
    
    
    def __deleteVertexUI(self, params):
        if len(params) != 1:
            print("Invalid number of parameters! \n")
            return
        x = int(params[0])
        c = self.__graph.deleteVertex(x)
        if c == 1:
            print(x," was deleted \n")
    
    
    def __addEdgeUI(self, params):
        if len(params) != 3:
            print("Invalid number of parameters! \n")
            return
        x = int(params[0])
        y = int(params[1])
        c = int(params[2])
        self.__graph.addEdge(x, y, c)
    
    
    def __deleteEdgeUI(self, params):
        if len(params) != 2:
            print("Invalid number of parameters! \n")
            return
        a = int(params[0])
        b = int(params[1])
        c = self.__graph.deleteEdge(a, b)
        if c == 1:
            print("The edge from ",a," to ",b," was deleted \n")
        if c == False:
            print("nope")
    
    
    def __vertexNumberUI(self, params):
        if len(params) != 0:
            print("Invalid number of parameters! \n")
            return
        n = self.__graph.numberVertices()
        print("The number of vertices is: ",n,"\n")
    
    
    def __outDegreeUI(self, params):
        if len(params) != 1:
            print("Invalid number of parameters! \n")
            return
        x = int(params[0])
        c = self.__graph.outDegree(x)
        print("The out degree of ",x," is ",c,"\n")
    
    def __inDegreeUI(self, params):
        if len(params) != 1:
            print("Invalid number of parameters! \n")
            return
        x = int(params[0])
        c = self.__graph.inDegree(x)
        print("The in degree of ",x," is ",c,"\n")
    
    
    def __parseInboundUI(self, params):
        if len(params) != 1:
            print("Invalid number of parameters! \n")
            return
        x = int(params[0])
        list=self.__graph.parseInbound(x)
        for i in list:
            print(i," ")
    
    
    def __parseOutboundUI(self, params):
        if len(params) != 1:
            print("Invalid number of parameters! \n")
            return
        x = int(params[0])
        list=self.__graph.parseOutbound(x)
        for i in list:
            print(i," ")
    
    
    def run(self):
        self.__menu()
        while True:
            cmd = input(">>")
            params = cmd.split(" ")
            if cmd == "exit":
                return
            elif params[0] in self.__commands.keys():
                self.__commands[params[0]](params[1:])
            elif params[0] == "help":
                self.__menu()
            elif params[0] == "vertexNumber":
                self.__vertexNumberUI()
                
            else:
                print("invalid command!")