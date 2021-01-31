graph = {
  '1' : ['2'],
  '2' : ['3','8'],
  '3' : ['4','5'],
  '8' : [],
  '4' : [],
  '5' : ['6','7'],
  '6' : [],
  '7' : []
}

visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
bfs(visited, graph, '2')
