function solution(A,K) {
    const arr = A.splice(-K)
    return arr.concat(A)
}

console.log(solution([1,2,3,4], 3));