# Data Structures - (Python Implementation💻)
This is my main reference for anyone who's looking to sharpen their skills with datastructures, feel free to take the work and 
change it up. There's a wide variety of topics I've implemented throughout my learning of datastructures and algorithms and love to
share the knowledge with the community. All the code is in Python as it's my goto language of choice but anyone is more than welcome
to use it as a practice guide or refresher on any topics you're not too strong in.

**All credit goes to - > Holczer Balazs (Udemy Python instructor)**


# 🛠️ The Data Structures + Use case

**Arrays are useful for storing a collection of data of the same type (ints, floats, strings), when deleting an item everything shifts to the left O(n). When inserting an item everything is shifted to the right to make room for the new element O(n). Appending and poping is O(1) since it adds or removes at the end of the list.** 

|    Arrays        |Time Complexity:watch:|Space Complexity:black_large_square:|Description:books:|                                                                                                                    
|------------------|---------------                                 |----------------|--------------------------|
|Array reversal    | O(n) - Where n is number of elements reversed. |  O(1) - No matter how big the array, it requires same space. |We take in n amounts of data within an array and take two pointers which take the start and end of an index. We then swap the starting index with the end index until they reach the two pointers meet. *e.g. [1,2,3,4] -> [4,3,2,1]*                                                                                                                                  
|Integer reversal  | O(log n) - Where n is the number of digits in the integer.| O(1) - No matter how big the array, it requires same space.            | Take in integer values which we use a log n approach as input size grows, we swap the first index with last index. *e.g. 1234 -> 4321*
|Palindrome        | O(n) - Where n is the length of the string. | O(n) - Additional space needed to store the new filtered and reversed string.   | String values that can be read forwards and backwards. Similar to the array reversal, we swap string values to see if they match. *e.g. 'madam'*                                                                                                           
|Anagram           | O(n log n) - Due to the number of string letters sorted within both arrays.                                                | O(1) - Since no extra space is being taken, just prints True or False. | Words that can be rearranged to mean the same thing. Takes two string values and compares the length of the strings within sorted chars. *e.g. 'restful' -> 'fluster'*                                                                                                                
|Duplicate within Int list | O(n) - Due to the use of a for loop to iterate n numbers. | O(n) - Since space requitred is same size of input. | Checking a list to see whether two of the same integers are within it. We traverse through the list converting positive ints into negatives based on the value, array elements must be less than array size. *e.g. [2, 3, 4, 3, 1] -> [2, 3, -4, -3, -1] - > [2, -3, -4, -3, -1] dup = 3*

|Linked lists |Time Complexity:watch:|Space Complexity:black_large_square:|Description:books:|    
|-------------|-----------------------|------------------------------------|------------------|
|
These are some of many structures to implement, feel free to mess around and make operations that take in a faster time and spcae complexity. 
If you look into each file you'll see that there's plenty of comments to understand what each line of code is doing. Enjoy using this source, again I don't take 
credit for it visit the author. [![Link - Udemy Course](https://img.shields.io/badge/Link-Udemy_Course-0099e5)](https://www.udemy.com/course/algorithms-and-data-structures-in-python/)
