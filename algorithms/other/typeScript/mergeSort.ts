const mergeSort = (arr: number[]) => {
    if (arr.length < 2) {
        return arr;
    }
    let mid = Math.floor(arr.length / 2);
    let left = arr.slice(0, mid);
    let right = arr.slice (mid);
    return merge(mergeSort(left), mergeSort(right));
}

const merge = (l: number[], r: number[]) => {
    let result: number[] = [];
    while (l.length && r.length) {
        if (l[0] <= r[0]) {
            result.push(l.shift());
        }
        result.push(r.shift());
    }
    while (l.length) {
        result.push(l.shift());
    }
    while (r.length) {
        result.push(r.shift());
    }
    return result;
}

// test
let test_mergeSort: number[];
test_mergeSort = [2, 13 , 1, 4, 5, -1];
console.log(mergeSort(test_mergeSort));
