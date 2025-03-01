#Write a recursive fuction to print all elements in the list.

def element_list(lst,idx):
    if (idx==len(lst)):
        return
    print(lst[idx])
    element_list(lst,idx+1)
element_list([1,2,3,4,5],0)