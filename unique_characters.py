


def count(str1 ,str2) :
   
    set_string1 = set(str1)
  
    # set of characters of string2
    set_string2 = set(str2)

    matched_characters = set_string1 & set_string2
    print("No. of matching characters are : " + str(len(matched_characters)) )
  
  
# Driver code
if __name__ == "__main__" :
  
    str1 = 'aabcddekll12@'  # first string
    str2 = 'bb2211@55k'     # second string
  
    # call count function 
    count( str1 , str2 )
     
