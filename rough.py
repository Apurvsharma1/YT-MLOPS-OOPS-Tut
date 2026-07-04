#lst = [1,2,3]
#mystr = "Mlops playlist"
#my_int = 155

#print(type(lst))
#my_mster = mystr.capitalize
#print(my_mster)

#Function vs Method (Method is also a function which is used in the classes.)
#function
lst = [1,2,3]
a1 = len(lst)
print(a1)
from oops_proj import chatbook
user1 = chatbook()
print(user1.id)

#Using static method directly from class rather than object
chatbook.set_id(10)
user2 = chatbook()
print(user2.id)

user3 = chatbook()
print(user3.id)







#getter and setter
# print(user1._chatbook__name)
# print(user1.get_name())
# user1.set_name("Apurv")
# print(user1.get_name())

# METHOD
#from oops_proj import chatbook
#user1 = chatbook()
#user1.sendmsg()
#print(user1._chatbook__name)
