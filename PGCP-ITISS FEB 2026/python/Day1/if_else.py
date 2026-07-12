# WAP to check if student has 75% att or not
# if yes --> then allowed for exam
# else if att > 50% 
# allowed with 40% reduction in marks
# else not allowed for exam
# take attended lectures and total lectures as
# input
tot_lect = int(input("Enter total lectures"))
att_lect = int(input("Enter attended lectures"))
print(att_lect,tot_lect)
per_att = att_lect / tot_lect * 100

if(per_att > 75):
    print("Allowed for exam")
elif( per_att > 50):
    print("allowed with 40% reduction in marks")
else:
    print("Not allowed")



# WAP for banking application
# Here we want to allocate credit card 
# to customers based on their income slab
# platinum card income > 100000
# gold card income between 50000 to 100000
# silver card income between 25000 to 50000
# bronze for all others

#if inc > 10000
#elif 50000 < inc <= 100000





# ternary operator

# if temp is > 40 then summer=True
# else summer =False
"""
temp=38
if temp > 40:
    summer = True
else:
    summer = False

summer = True if temp > 40 else False
"""











