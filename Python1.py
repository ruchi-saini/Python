
# (1) WAP to take input from user

"""input1=int(input("enter a first number:"))
input2=int(input("enter a second number:"))
sum=input1 + input2
print(sum)"""

# (2) List [Description: List is mutable and we can use slicing in List]

# Wap to check the list is Palindrome or not

"""l1=[1,2,1]
listt= l1.copy()
listt.reverse()
if(l1==listt):
  print("Palindrome")
else:
   print("Not Palindrome")"""


# (3) Tuple (immutable) : We can't use tuple and list in set
  
"""t1=(1,2,3)
print(t1[0:2])"""

# (4) Dictionary (mutable) : It stores value in the form of key value pairs and they are unordered , don't allow duplicate keys
#  dict["keys"]= "value"   -> to assign or add value     ;  "key" : value

"""student = {
    "name" : "Ruchi " ,
    " age" : 23 ,
    "marks" :  [94,56,98],
    "subjects" : {
        "Phy": 98,
        "chem" : 95 ,

        }

    }
print(student[" age"])
print(student)
student["city"] = " Sambhal"
print(student)
print(student["subjects"]["chem"])   # Nested dict 
"""


# Methods -> (1) dict.keys()  : returns all keys (only outer keys return if data contain nested dictionary )
#            (2) dict.values() : returns all values of dictionary 
#            (3) dict.items() : returns all (key,value) pairs as tuple
#            (4) dict.get("key") : return the key according to the value
#            (5) dict.update("new_dict") : insert the specified item to the dictionary


# (5) Set : Collections of unordered items and each element in the set are unique and set elements are immutable but itself sets is mutable
# set() -> this is empty set ..... if we print the type of empty set like [stud= {}] then this is not set but this is empty dictionary.  Unhashable value-> set do not support list and dict.
# Mthods in Set -> (1) stud.add() , (2) stud.remove() , (3) stud.clear() , (4) stud.pop()-> they pop element in random order
#                   (5) set.union() , (6) set.intersection()
 
"""collection= {1, 3, 1, 4, "python" ,4}
print(collection)    # o/p -> {1,3,4,"python}
stud=set("ruchisaini")
print(stud)          # o/p -> {'r', 'u', 'c' , 'h', 'i', 's', 'a', 'n'}
set= set() -> empty set
"""

