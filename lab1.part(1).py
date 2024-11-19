"""
27. Написати функцію, що за послідовністю цілих знаходить елементи, що зустрічаються в ній
найчастіше.
"""
dict1 = {}


def count_amounts_of_values(list1):
    for x in list1:
        if x in dict1:
            dict1[x] += 1
        else:
            dict1[x] = 1
    print(dict1)


def most_frequent_var(dict1):
    list2 = []
    max_amount = 0
    for k, v in dict1.items():
        if v > max_amount:
            max_amount = v
            list2 = [k]
        elif v == max_amount:
            list2.append(k)
    print("The most frequent variables are " + str(list2))


list1 = [2, 2, 2, 2, 8, 8, 8, 8, 4, 4, 4, 4, 3, 3, 3, 1, 1, 7, 6]
count_amounts_of_values(list1)
most_frequent_var(dict1)

