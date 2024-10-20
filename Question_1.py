'''
Question

You are given an array of Integers in which each subsequent value is not less than the previous value. Write a function that takes this array as an input and returns a new array with the squares of each number sorted in ascending order.

Remember

You can solve this question in multiple ways.

Think about the following -

1.What would be the brute force way of solving this question ? What would be the Time and Space complexity of this approach?

2.Is there a better way to solve this with a more optimum Time complexity than the Brute force way ?
'''

#Method 1:-

#By Using Brute Force Algorithm

def ssr(ar): #creating function named ssr
  
  n=[]  #Initalizing a new array
  
  for i in range len(ar):  # iterating over the input array 
  
    n.append(ar[i]*ar[i])   #squaring the value in the old array and adding it into the new array
  
  n.sort()      #sorting the array
  
  return n      #returning the sorted array
  
print(ssr([-9,1,2,3]))
'''
Time Complexity:-

As we are traversing through the array using for loop the time complexity for the for loop is o(n).
And there next we are using sorting to sort the array that an average sorting technique would take a time complexity of o(nlogn).
In total time complexity is equals to o(n)+o(nlogn).We can Summarise that our code by using Brute force Algorithm it takes o(nlogn)
Time Complexity.

Space Complexity:-

As we are creating a new array and adding values into it our space complexity of this problem is o(n).As the number of elements should 
be added into the new array after squaring it from the old array.

Time Complexity  : o(nlogn) 
Space Complexity : o(n)
'''

# Method 2

def ssr(ar):
  n = [0]*len(ar)      # creating new array
  
  leftpointer = 0       #left pointer of the given array
  
  rightpointer = len(ar)-1  #right pointer of the given array
  
  for i in reversed(range(len(ar))):    #looping in reverse order
      
        new_list_left = ar[leftpointer]**2      #getting the squared value of the leftpointer and storing in new_list_left
        
        new_list_right = ar[rightpointer]**2    #getting the squared value of the rightpointer and storing in new_list_right
        
        if new_list_left>new_list_right:        #if the new_list_left value is highest then adding it into the right of new list
            
            n[i] = new_list_left          #adding the value to the right most of new list as i value is in reverse
            
            leftpointer +=1         #increasing the left pointer to move forward in the given array
            
        else:           #if the rightpointer value is greater than or equal then adding the new_list_right value to the right of new list
            
            n[i] = new_list_right  #adding the value to the right most of new list as i value is in reverse
            
            rightpointer -=1    #updating the rightpointer to move back to next element in the array
            
  return n  #returning the sorted squared array
  
print(ssr([-9,1,2,2,3,3]))

'''
Time Complexity:-

As we are traversing through the array using for loop the time complexity for the "for loop" is o(n).
In total time complexity is equals to o(n).We can Summarise that our code by using Brute force Algorithm it takes o(n)
Time Complexity.

Space Complexity:-

As we are creating a new array and adding values into it our space complexity of this problem is o(n).As the number of elements should 
be added into the new array after squaring it from the old array.

Time Complexity  : o(n) 
Space Complexity : o(n)

NOTE :- By this we have optimised the time complexity of the given problem.

'''
