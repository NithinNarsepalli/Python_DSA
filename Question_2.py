'''
Coding Exercise - Python: Monotonic Array
Question:-
An array is monotonic if it is either monotone increasing or monotone decreasing.
An array is monotone increasing if all its elements from left to right are non-decreasing.
An array is monotone decreasing if all  its elements from left to right are non-increasing. 
Given an integer array return true if the given array is monotonic, or false otherwise.
'''
def monotonic_array(array):
  if len(array)==0:
      return True
  else:
      left = array[0]
      right = array[len(array)-1]
      
    
      if left == right:
        for i in range(len(array)-1):
          if(array[i+1]!=array[i]):
            return False
            
      elif left > right:
        for i in range(len(array)-1):
          if(array[i+1]>array[i]):
            return False
      else:
        for i in range(len(array)-1):
          if(array[i+1]<array[i]):
            return False
      return True
