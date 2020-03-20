class Graph(): 

	def __init__(self, vertices): 
		self.V = vertices 
		self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
		self.parent = {}

	def maxDistance(self, dist, sptSet): 
		maximum = float('-inf')
		for v in range(self.V): 
			if dist[v] >= maximum and sptSet[v] == False: 
				maximum = dist[v] 
				max_index = v 
		return max_index

	def getPath(self, parents, src, last):
		sentences = [last]
		i = last
		while i != src:
			temp = parents[i]
			i = temp
			sentences.append(temp)
		return sentences[::-1]

	def dijkstra(self, src, last): 

		dist = [float('-inf')] * self.V 
		dist[src] = 0
		sptSet = [False] * self.V 

		for cout in range(self.V): 
			u = self.maxDistance(dist, sptSet) 
			sptSet[u] = True
			for v in range(self.V): 
				if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] < dist[u] + self.graph[u][v]: 
					dist[v] = dist[u] + self.graph[u][v]
					self.parent[v] = u

		return self.getPath(self.parent, src, last)
