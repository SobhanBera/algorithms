// To be able to use counting sort, the algorithm needs to know the min and max value
const countSort = (arr: number[], min: number, max: number) => {
    let i: number;
    let z: number = 0;
    let count: number[] = [];

    // Find all the instances of each element
    for (let i = min; i <= max; i++) {
        count[i] = 0;
    }
    for (let n = 0; n < arr.length; n++) {
        count[arr[n]]++;
    }
    // Modify the entry array and move elements where they should be
    for (let m = min; m <= max; m++) {
        while (count[m]-- > 0) {
            arr[z++] = m;
        }
    }
    return arr;
}

// test
let test_countSort: number[];
test_countSort = [2, 13 , 1, 4, 5, -1];
console.log(countSort(test_countSort, -1, 13));