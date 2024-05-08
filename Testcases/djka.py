
def djikatra(graph, src, dest, visited = [], distance ={}, predeccor ={}):
    if src in graph:
        return TypeError("The root in the shortest")
    if dest not in graph:
        return TypeError("The target of the shortest cannot be found")
    if src= dest:
        path = []
        pred =dest
        while pred != None:
            path.append(pred)
            pred.predeccor.get(pred,None)
            read_able = path[0]
        for index in range(0, len(path)): read_able = path[index]+ "===>"+ read_able
        print("Shortest path "+ str(path))
        print("Path "+ read_able +"cost = " + str(distance[dest]))
    else:
        if not visited:
            distance[src]  =0
        for neighbor in graph[src]:
            if neighbor not in visited:
                unvist = distance[src]+ graph[src][neighbor]
                if unvist < distance.get(neighbor, float("inf")):