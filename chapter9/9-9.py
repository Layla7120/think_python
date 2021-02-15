def is_palindrome(word):
    i = 0
    j = len(word)-1
    while i < j:
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1
    return True

# gap = 0
# while gap < 99:
#    age = 0
#    count = 0
#    while age < 100:
#       mom_age = age + gap 
#       str_age = str(age)
#       if age < 10:
#          str_age = str_age.zfill(2)
#          test = str(mom_age) + str_age
#          if is_palindrome(test):
#                count += 1

#       else:
#          test = str(mom_age) + str_age
#          if is_palindrome(test):
#                count += 1
#       age += 1
#       if count == 8:
#          print(age, mom_age, gap)  
#    gap += 1  

gap = 18

age = 0
count = 0
while age < 98:
   mom_age = age + gap 
   str_age = str(age)
   if age < 10:
      str_age = str_age.zfill(2)
      test = str(mom_age) + str_age
      if is_palindrome(test):
            count += 1
            print(age, mom_age, gap)

   else:
      test = str(mom_age) + str_age
      if is_palindrome(test):
            count += 1
            print(age, mom_age, gap, "in")

   if count == 8:
      print(age, mom_age, gap)
      break 
   
   age += 1
    
gap += 1  
  