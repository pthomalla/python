def all_brige(graph):
    def to_dictionary_neighbor_list(graph):
        dictionary_neighbor_list = {}
        for vertices in graph[0]:
            dictionary_neighbor_list[vertices] = []
        for edge in graph[1]:
            dictionary_neighbor_list[edge[0]].append(edge[1])  
            dictionary_neighbor_list[edge[1]].append(edge[0]) 
        return dictionary_neighbor_list
    def dfs(list_neighbor,vather):
        for neighbor in list_neighbor:
            representative = dictionary_representatives.get(neighbor)
            if representative == None :
                dictionary_representatives[neighbor] = neighbor
                stack.append(neighbor)
                if vather != None:
                     dictionary_neighbor_list[neighbor].remove(vather)
                dfs(dictionary_neighbor_list[neighbor],neighbor)
                top = stack.pop()
                if top == neighbor and vather != None:
                    briedge.append( (top, vather) )
                else:
                    stack.append(top)
            else:
                pop = stack.pop()
                while pop != representative:
                    dictionary_representatives[pop] = representative
                    pop = stack.pop()
                stack.append(pop)
    dictionary_representatives = {} 
    stack = []
    briedge = [] # list of find brige 
    dictionary_neighbor_list = to_dictionary_neighbor_list(graph)
    for vertex in graph[0]:
        if dictionary_representatives.get(vertex) == None :
            dfs([vertex],None)
    return briedge  

graph = (set([1,2,3,4,5,6,7,8,9,10]),set([(1,2),(2,3),(3,4),(2,6),(3,5),(6,5),(6,7),(7,8),(7,10),(10,8),(8,9)]))
print( all_brige(graph) )
graph = (set(range(9)),set([(0,2),(2,4),(0,4),(4,1),(1,5),(5,6),(6,8),(8,7),(6,7)]))
print( all_brige(graph) )
graph = (set(range(5)),[(0,1),(1,2),(2,3),(3,1),(3,4),(4,1)])
print( all_brige(graph) )

