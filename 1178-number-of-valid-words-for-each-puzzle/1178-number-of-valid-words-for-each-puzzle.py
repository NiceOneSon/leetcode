from collections import defaultdict

class Solution:
    
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        allcases = defaultdict(int)
        words = [''.join(sorted(set(word))) for word in words if len(set(word)) <= 7]
        
        for word in words:
            allcases[word] += 1
            
        answer = []
        
        BASE = (1 << 6)
        
        for puzzle in puzzles:
            result = 0
            for i in range(BASE, BASE << 1):
                string = ''
                for j in range(7):
                    if i & BASE >> j:
                        string += puzzle[j]
                else:
                    string = ''.join(sorted(string))
                    # print(puzzle, string, allcases[string], format(i, 'b'))
                    result += allcases[string] 
            answer.append(result)
            
        return answer
            