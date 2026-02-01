from collections import defaultdict
def solution(phone_book):
    
    dicts = defaultdict(int)
    phone_book.sort(key = lambda x: len(x))

    for book in phone_book:
        temp = ''
        for char in book:
            temp += char
            if dicts[temp] == 1 and temp != book:
                return False
        dicts[temp] = 1
    
    
        
        
    return True