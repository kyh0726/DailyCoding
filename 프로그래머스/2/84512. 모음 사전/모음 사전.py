def solution(word):
    answer = 0
    dicts = []

    
    def dfs(string):
        dicts.append(string)
        if len(string) == 5:
            return 
        for i in ["A","E", "I", "O", "U"]:
            dfs(string + i)
            
    
    dfs("")
    
    dicts.sort()
        
    
    return dicts.index(word)