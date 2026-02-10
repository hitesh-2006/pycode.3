n=int(input("Enter no of students:"))

marks=[]

        #personalization logic , the student who scored 70 marks,he is the lucky winner 
for i in range(n):
  m=int(input("enter mark:"))
  marks.append(m)

valid_count=0
fail_count=0


for mark  in marks:


  if mark<0 or mark>100:
    category="invalid"


  elif mark>=90:
   category ="excellent"
   valid_count+=1

  elif mark>=75:
   category ="very good"
   valid_count+=1

  elif mark>=60:
    #personalization logic
    if mark==70 :
      print("he is the lucky winner")
      valid_count+=1      
    else :  
      category ="good"
      valid_count+=1

  elif mark>=40:
   category ="average"
   valid_count+=1

  else:
   category ="Fail"
   valid_count+=1
   fail_count+=1

  print(str(mark) + "->" + category)


print("total valid students:" , valid_count)
print("total failed students:",fail_count)


     

