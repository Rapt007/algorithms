from __future__ import division
def binary(array,low,high,x):
    while(low<=high):
        mid=low+(high-low)//2
        if(x==array[mid]):
            return mid
        elif(x>array[mid]):
            low=mid+1
            return binary(array,low,high,x)
        elif(x<array[mid]):
            high=mid-1
            return binary(array,low,high,x)
array=[1,2,3,4,5,6,8,7,9,0]
array.sort()
print array
low=0
high=len(array)-1
x=eval(raw_input('enter a number'))
index=binary(array,low,high,x)
print index