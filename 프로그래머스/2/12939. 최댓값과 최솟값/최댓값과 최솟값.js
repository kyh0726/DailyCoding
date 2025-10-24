function solution(s) {
    var answer = '';
    
    vals = s.split(" ").map((val) => Number(val))
    vals.sort(function(a,b) {return a - b})
    val_len = vals.length

    answer += String(vals[0]) + " " + String(vals[val_len-1])

    return answer;
}