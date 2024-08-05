import statistics
def mean_median_mode(list1):
    return [statistics.mean(list1),statistics.median(list1),statistics.mode(list1)]
a,b,c=mean_median_mode([1,3,4,56,7,5,3,8])
print(f"mean is {a} \nmedian is {b} \nmode is {c}")
print("done")
print("second push")
