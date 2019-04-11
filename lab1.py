
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   
   if(int_list== None):
      raise ValueError

   if(int_list == []):
      return None 

   max = int_list[0]   

   for i in range(1, len(int_list), 1):
      if(int_list[i] > max):
         max= int_list[i]

   return max         

def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""

   if(int_list == None):
      raise ValueError

   if(int_list == []):
      a = []
      return a
   
   if(len(int_list)==1):
      return int_list 

   return [int_list[-1]] + reverse_rec(int_list[:len(int_list)-1])
   

def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   
   if(int_list == None):
      raise ValueError

   if(low > high):
      return None

   #if(len(int_list) == 0):
    #  return None

   mid = (low+high)//2   

   if(target == int_list[mid]):
      return mid

   elif(target > int_list[mid]):
      low = mid+1
      return bin_search(target, low, high, int_list)

   elif(target < int_list[mid]):
      high = mid-1
      return bin_search(target, low, high, int_list)
     
   


