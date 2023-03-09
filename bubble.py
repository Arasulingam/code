#Program for bubble sort
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0,n-i-1):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
    print('Sorted List:\n',lst)

#Getting Input
input_lst = input('Enter a List:')
lst= [int(x) for x in input_lst.split()]
bubble_sort(lst)
