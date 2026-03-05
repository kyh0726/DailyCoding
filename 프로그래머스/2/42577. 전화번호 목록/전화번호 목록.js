function solution(phone_book) {
    var answer = true;
    
    const map = new Map();
    
    const compareFunc = (a, b) => {
        if (a.length == b.length) {
            return a - b
        }
        else {
            return a.length - b.length
        }
    }
    
    phone_book.sort(compareFunc)
    
    for (let i = 0; i < phone_book.length; i++) {
        cur_phone_book = phone_book[i]
        
        for (let j = 0; j < cur_phone_book.length; j++) {
            const sliced_num = cur_phone_book.slice(0,j+1)
            if (map.has(sliced_num)) {
                return false
            } else {
                if (j == cur_phone_book.length - 1) {
                    map.set(cur_phone_book, 1)
                }
            }
            
        }
        
    }
    
    
    
    return true;
}