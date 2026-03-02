prices=[100,200,300,400]
discount=10
dicounted_list=[]
for price in prices:
    discountt=price-(price*discount/100)
    dicounted_list.append(discountt)
print(dicounted_list)
