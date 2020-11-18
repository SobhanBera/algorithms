# Python program for counting sort
  
def counting_sort(arr): 
    max_element = int(max(arr)) 
    min_element = int(min(arr)) 
    range_element = max_element - min_element + 1
    # Create a count array to store count of individual elements and initialize count array as 0 
    counting_arr = [0 for _ in range(range_element)] 
    output = [0 for _ in range(len(arr))] 
  
    # Store count of each character 
    for i in range(0, len(arr)): 
        counting_arr[arr[i]-min_element] += 1
  
    for i in range(1, len(counting_arr)): 
        counting_arr[i] += counting_arr[i-1]
  
    # Build the output character array 
    for i in range(len(arr)-1, -1, -1): 
        output[counting_arr[arr[i] - min_element] - 1] = arr[i] 
        counting_arr[arr[i] - min_element] -= 1

    for i in range(0, len(arr)): 
        arr[i] = output[i] 
  
    return arr 
  
print("Enter the elements of the array : ")
arr = list(map(int, input().split()))
ans = counting_sort(arr) 
print("Sorted array is : " + str(ans)) 