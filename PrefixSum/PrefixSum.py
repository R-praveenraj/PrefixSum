#Given an array A of N integers. Construct prefix sum of the array in the given array itself.

def PrefixSum(array):
    new=0
    for i in array:
        new+=i
        array[i-1]=new
    return array



array = [1, 2, 3, 4, 5]
print(PrefixSum(array))