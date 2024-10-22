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
    #if the length of the given array is empty then we return true
      return True
  #if the given array is full then we check following conditions
  else:                      
      #assiging the left most element of an array to the variable left
      left = array[0]
      #assiging the right most element of an array to the variable right
      right = array[len(array)-1]
      
      #if the left and right of the given array is equals then
      if left == right:
        #we are going to loop over the array to check the values are same or not 
        for i in range(len(array)-1):
          #if the value of the next index is not equals to the present index then we return false as it is not a monotonic array
          if(array[i+1]!=array[i]):
            return False
            
      #if the leftmost is greater than the rightmost then the array  values must be decreasing in nature if not we return false   
      elif left > right:
        #we are looping through the array to check the values of the array
        for i in range(len(array)-1):
          #if the value of the next index in array is not lesser than the current index value then we return false as it is not a monotonic array
          if(array[i+1]>array[i]):
            return False
      #this block refers to the if leftmost value  is lesser than right most value then array values must be increasing in nature if not false
      else:
        #we are looping through the array to check the values of the array
        for i in range(len(array)-1):
          #if the next index value is lesser than the current index value then we return false 
          if(array[i+1]<array[i]):
            return False
      #if all the conditions are satified the we return true as it is a monotonic array
      return True
