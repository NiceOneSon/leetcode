from collections import defaultdict
from typing import Optional
from typing import Union
import heapq


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        self.distance_cached_dict = None
        INF: float = float('inf')
        # alphabet_length = ord('z') - ord('a') + 1
        
        def main(
            source: str, 
            target: str, 
            original: List[str], 
            changed: List[str], 
            cost: List[int]
        ) -> int:
            answer: int = 0
            distance_cached_dict: dict[str, int] = get_cached_dict()
            
            for idx_convert in range(len(source)):
                src_alphabet: str = source[idx_convert]
                trg_alphabet: str = target[idx_convert]
                if src_alphabet == trg_alphabet:
                    continue
                # print(idx_convert, src_alphabet, trg_alphabet, distance_cached_dict[src_alphabet][trg_alphabet])
                if distance_cached_dict[src_alphabet][trg_alphabet] == INF:
                    return -1 
                
                answer += distance_cached_dict[src_alphabet][trg_alphabet]
            return answer
        
        def dijkstra(alphabet: str) -> None:
            # print(alphabet, "dijkstra start.")
            start_node: str = alphabet
            distance_cached_dict = self.distance_cached_dict
            queue: list[tuple[int, str]] = []
            for nextnode, cost in distance_cached_dict[start_node].items():
                heapq.heappush(queue, (cost, nextnode))
            
            while queue:
                # print(queue)
                distance, node = heapq.heappop(queue)
                for end_node in distance_cached_dict[node]:
                    # print(end_node)
                    if distance_cached_dict[node][end_node] == INF:
                        # print('first passed')
                        continue
                    total_dist = distance + distance_cached_dict[node][end_node]
                    if distance_cached_dict[start_node][end_node] <= total_dist:
                        # print('second passed')
                        continue
                    distance_cached_dict[start_node][end_node] = total_dist
                    heapq.heappush(queue, (total_dist, end_node))
            
            return 
                
            
        
        def get_cached_dict() -> dict[str, int]:
            "```return the minimum distance dictionary```"
            
            if self.distance_cached_dict == None:
                distance_cached_dict: dict[str, dict[str, Union[int, float]]] = defaultdict(lambda: defaultdict(lambda: INF))
                
            for idx_cost_spec in range(len(cost)):
                from_alpha: str = original[idx_cost_spec]
                to_alpha: str = changed[idx_cost_spec]
                convert_cost: int = cost[idx_cost_spec]
                distance_cached_dict[from_alpha][to_alpha] = min(convert_cost, distance_cached_dict[from_alpha][to_alpha])
            self.distance_cached_dict = distance_cached_dict
            for alphabet_ord in range(ord('a'), ord('z')+1):
                alphabet = chr(alphabet_ord)
                dijkstra(alphabet)
            return self.distance_cached_dict
        
        return main(
            source = source, 
            target = target, 
            original = original, 
            changed = changed, 
            cost = cost
        )
        
        