
def total_sum(a)->int:
    """

    :param a:
    :return:
    """
    if a==0:
        return 0
    return a + total_sum( a-1 )
a=int(input())
print(total_sum(a))

n = int(input())
print(n*(n+1)/2)

n2=int(input())
total=0
for i in range(1,n2+1):
    total+=a
print(total)