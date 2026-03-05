function solution(word) {
    var answer = 0;
    
    var chars = ["A","E","I","O","U"]
    var cases = []
    const make_cases = (count, cur_string) => {
        
        if (cur_string != "") {
            cases.push(cur_string)
        }

        if (count == 5) {
            return
        }
        
        for (let i = 0; i < chars.length; i++) {
            make_cases(count + 1, cur_string + chars[i])
        }
        
    }
    make_cases(0,"")
    
    cases.sort()
    
    answer = cases.indexOf(word) + 1
    
    
    return answer;
}