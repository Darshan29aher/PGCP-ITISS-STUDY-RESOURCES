# WAP to ask order from user
# show menu and take one item at a time
# increase the counter every time there 
# is input from the user
# if counter ==5 , then 
# print limit reached 
# when user says 'q' then stop
# and print msg "complete"
#
# menu : 
# a. Thali b. Chapati sabji 
# c. lassi d. paratha
# q. quit

counter=0
while(counter < 5):
    print("""menu : 
    a. Thali b. Chapati sabji 
    c. lassi d. paratha
    q. quit""")
    item = input()
    if(item == 'q'):
        break
    counter +=1
else:
    print("Limit reached!")

print("complete!")
