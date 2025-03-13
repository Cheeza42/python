def sort_algorithm(): # We made a function that sorts a list into a orginized list.


     numbers = input('please enter numbers for list').split() # First we ask from the user to create a list.
  
     list1 = [int(num) for num in numbers] #Tghe list itself that contains a condition to execute the other list.
     sort_list1 = list1.copy() # The other list that have a copy function('.copy') from the input list.

     for _ in range(len(sort_list1)): # The first loop will always check the original list to make sure hes not getting confused on the way.
          for j in range(len(sort_list1)-1): # The child loop sorts the numbers from the OG list to make a new sorted lst. 
               if sort_list1[j] > sort_list1[j + 1]: # The condition says if the number is bigger form itself by 1:
                sort_list1[j], sort_list1[j + 1] = sort_list1[j + 1], sort_list1[j] # it will place them in order from the small one to the bigger one. 

     print("The original list:", list1) # Display the original list.
     print("Sorted list:", sort_list1) # display the sorted list.


sort_algorithm() # Execute the function.