
def sort(l):
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if l[i]>l[j]:
               l[i],l[j] = l[j],l[i]
    return l
# print(sort([1,3,6,2,6,3,7,3,9]))        # ? both outputs
if __name__=="__main__":                       # to define main function
    print(sort([1,4,5,2,5,6,2,4,52]))