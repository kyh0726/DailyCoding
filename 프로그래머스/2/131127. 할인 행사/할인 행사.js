function solution(want, number, discount) {
    var counts = {}
    var result = 0
    var answer = 0

    function add(key) {
        counts[key] = (counts[key] || 0) + 1;
        if (counts[key] == number[want.indexOf(key)]) {
            result += 1
        }
    }

    function reduce(key) {
        counts[key] = counts[key] - 1;
        if (counts[key] == number[want.indexOf(key)] - 1) {
            result -= 1
        }
    }
    
    for (let i = 0; i < 10; i++){
        add(discount[i])
    }
    if (result == want.length) {
        answer += 1
    }

    for (let i = 10; i < discount.length; i++) {
        add_target = discount[i]
        reduce_target = discount[i-10]
        add(add_target)
        reduce(reduce_target)
        if (result == want.length) {
            answer += 1
        }
    }

    
    return answer;
}