# def main(**kwargs):
#     print(kwargs)
#     for k, v in kwargs.items():
#         print(k, v)

# print(main(name='Akni', age='24', i=123, b={'name':'Akni'}))


# def rec():
#     return rec()

# rec()


# a=10
# for i in a:
    # print(i)

# def rec_num(number:int):
#     if number==0:
#         return 1
#     return number*rec_num(number-1)

# # print(rec_num(15))

# # factorial=rec_num(5)


# num=int(input("Vvedite chislo:"))
# factorial=rec_num(num)
# print("Factorial chisla", num, "raven", factorial)


def max_find_num(lists:list, n):
    if n==0:
        return "Кума"
    if n==1:
        return lists[0]
    
    return max(lists[n-1], max_find_num(lists, n-1))


arr=[1,2,3]
n=len(arr)
print(max_find_num(arr, n))








