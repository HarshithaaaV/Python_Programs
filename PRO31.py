#WAF to print the elements of a list in a single line.(list in the parameter).

def print_list(lst):
    for i in lst:
        print(i,end=" ")
    return
color = ["black", "red", "blue", "green", "yellow", "white"]
print_list(color)