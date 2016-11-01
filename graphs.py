
def dfs_iterative(graph, start, goal):
	visited, stack = set(), [start]
	while stack:
		vertex = stack.pop()
		if vertex not in visited:
			visited.add(vertex)
			stack.extend(graph[vertex] - visited)

			if vertex == goal:
				return visited
	print('Goal not found.')
	return visited

def dfs(graph, start, goal, visited = None):
	if visited is None:
		visited = set()

	if start == goal:
		return visited

	visited.add(start)
	neighbors = graph[start]
	
	for neighbor in neighbors - visited:
		dfs(graph, neighbor, goal, visited)

	print('Goal not found.')
	return visited


graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def run_test(option, goal):
	if option == 'r' or option == 'R':
		return dfs(graph, 'A', goal)
	elif option == 'i' or option == 'I':
		return dfs_iterative(graph, 'A', goal)
	else:
		print('Option not recognized. Usage: run_test option goal (i : iterative, r: recursve)')

