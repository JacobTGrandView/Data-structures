class Graph():

    def __init__(self, vertices_num):
        # number of nodes (an integer)
        self.v = vertices_num
        # (maybe not useful here) : list of nodes from "A0", "A1" ... to "A index (vertices_num - 1)"
        self.nodes = None

    # from adjacency matrix to dictionary
    def adjmat_2_graph(self, adjm):
        nd = {}
        for i in range(len(adjm)):
            nodeList = []
            strVal = 'A'+str(i)
            for j in range(len(adjm[i])):                
                if adjm[i][j] != 0:
                    nodeVal = 'A'+str(j)
                    nodeList.append((nodeVal,adjm[i][j]))
                    
                
            nd[strVal] = nodeList
    # from dictionary to adjacency matrix
    #def graph_2_mat(self, graph):
    
    # from dictionary to adjacency list    
    #def graph_2_list(self, graph):
        
    # from adjacency list to dictionary
    #def list_2_graph(self, lst):
        
    # from adjacency matrix to adjacency list    
    #def mat_2_list(self, mat):
    
    # from adjacency list to adjacency matrix
    #def list_2_mat(self, lst):
        
    def dfs(self):
        for vertex in self:
            vertex.color = "white"
            vertex.previous = -1
            for vertex in self:
                if vertex.color == "white":
                    self.dfs_visit(vertex)
        
    # find all path from node start_vertex to node end_vertex
    def find_all_paths(self, graph, start_vertex, end_vertex):
        #DFS
        original_vertex = start_vertex
        #add start point to path
        outPaths = []
        globalneighbors = []
        vertexPath = [start_vertex]
        #need a local list of neighbors
        neighbors = graph[start_vertex]
        #need a global list of visited
        globalneighbors.append(neighbors)
        
        while len(globalneighbors) >0:
            previousVertex = start_vertex
            intVert = neighbors.pop()
            start_vertex = intVert[0]
            #keep track of the path taken
            #add neighbors to a list of lists
            #four scenarios the vertex is the start, the end, previous, or a new vertex
            if start_vertex == end_vertex:
                #add end vertex to vertex path and add to outPaths
                vertexPath.append(end_vertex)
                outPaths.append(vertexPath)
            elif start_vertex != original_vertex:
                vertexPath.append(start_vertex)
                neighbors = graph[start_vertex]
                #remove path back to neighbor
                #todo remove the vertex right now it's still in tuple form
                neighbors.remove(previousVertex)
                #if neighbors exist add them to the global list
                if len(neighbors)>0:
                    globalneighbors.append(neighbors)
                
            #check if it has any other neighbors
            #check if it's neighbors are the end vertex
            #check if it's neighbors are the original vertex
            #keep a list of the verticies visited
        

        
       
class vertex():
    def __init__(self,name,previous):
        self.name = name
        self.color = "white"
        self.previous
    
    def get_neighbor(self, other):
        return self.neighbors.get(other, None)
    



g = Graph(5)

o=[[0, 2, 0, 6, 0],[2, 0, 3, 8, 5],[0, 3, 0, 0, 7],[6, 8, 0, 0, 9],[0, 5, 7, 9, 0]]


g.adjmat_2_graph(o)

dct = {'A5': [('A3', 1),('A0', 1)], 'A3': [('A0', 1), ('A2', 1),('A5', 1)], 'A0': [('A3', 1), ('A5', 1)], 'A4': [('A2', 1)], 'A1': [('A2', 1)], 'A2': [('A1', 1), ('A3', 1), ('A4', 1)]}
g = Graph(6)
g.find_all_paths(dct, "A0", "A1")
# ['A0-A3-A2-A1', 'A0-A5-A3-A2-A1'])


#step 1 get all neighbors to the starting vertex











