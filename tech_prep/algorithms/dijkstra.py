import heapq

class Dijkstra:
    @staticmethod
    def dijkstra(graph, start):
        heap = [(0, start)]
        distances = {node: float('inf') for node in graph}
        distances[start] = 0
        
        while heap:
            curr_dist, node = heapq.heappop(heap)
            if curr_dist > distances[node]:
                continue
            for neighbor, weight in graph[node]:
                distance = curr_dist + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(heap, (distance, neighbor))
                    
            return distances
