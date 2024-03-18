def linear_search(list, target):
  for i in range(0,len(list)):
     if list[i] == target:
       return i
  return None
  
  
  
  
  
def verify(index):
    if index is not None:
        print("Target found on:", index+1)
    else:
        print("Target not found")
        
numbers=[1,2,3,4,5,6,7,8,9,10]


results=linear_search(numbers, 5)
verify(results)
results=linear_search(numbers, 20)
verify(results)
results=linear_search(numbers, 9)
verify(results)
results=linear_search(numbers, 2)
verify(results)