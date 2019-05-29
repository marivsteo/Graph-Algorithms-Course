from graph import MatrGraph
'''
Created on 28 May 2019

@author: Marius
'''

class Console():
    

    def __help(self):
        self.__menu()
    
    def __init__(self, MatrGraph):
        self.__graph = MatrGraph
        self.__commands = {"hamCycle" : self.__hamCycleUI,
                           }
        
    
    def __menu(self):
        
        print("\n To check if the graph contains a hamiltonian cycle enter command: 'hamCycle' \n")
    
    
    
    def __hamCycleUI(self, params):
        if len(params) != 0:
            print("Invalid number of parameters! \n")
            return
        if self.__graph.hamCycle()==False:
            print("No hamiltonian cycle found! \n")
        else:
            path=self.__graph.hamCycle()
            self.__graph.printSolution(path)
    
    
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