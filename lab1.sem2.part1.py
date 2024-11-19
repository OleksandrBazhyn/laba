# 26. Написати функцію, що за послідовністю цілих будує список її елементів,
# що зустрічаються в ній більше одного разу.

from random import randint
amount = 20
list1 = []
for i in range(amount):
    list1.append(randint(1, 30))
print(list1)

list2 = []
for i in list1:
    if list1.count(i) > 1:
        list2.append(i)
print(set(list2))


