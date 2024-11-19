"""
27. Написати функцію, що за послідовністю цілих знаходить елементи, що зустрічаються в ній
найчастіше.
"""


def count_amounts_of_values(list_):
    dict1 = {}
    for x in list_:
        if x in dict1:
            dict1[x] += 1
        else:
            dict1[x] = 1
    return dict1


def most_frequent_var(new_list):
    dict1 = count_amounts_of_values(new_list)
    print(dict1)
    list_0 = []
    max_amount = 0
    for k, v in dict1.items():
        if v > max_amount:
            max_amount = v
            list_0 = [k]
        elif v == max_amount:
            list_0.append(k)
    return list_0


list1 = [2, 2, 2, 2, 8, 8, 8, 8, 4, 4, 4, 4, -3, -3, -3, 1, 1, 7, 6]
list2 = [1, 1, 1, 4, 4, 4, 7, 7, 7]
list3 = [-8]
list4 = []

print(most_frequent_var(list1))
print(most_frequent_var(list2))
print(most_frequent_var(list3))
print(most_frequent_var(list4))
