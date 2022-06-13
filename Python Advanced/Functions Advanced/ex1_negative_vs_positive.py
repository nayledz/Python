def negative_vs_positive(*args):
    sum_negatives = 0
    sum_positives = 0
    for num in args:
        if num < 0:
            sum_negatives += num
        else:
            sum_positives += num
    return sum_positives, sum_negatives


nums = [int(x) for x in input().split()]


sum_positives, sum_negatives = negative_vs_positive(*nums)

print(sum_negatives)
print(sum_positives)
if abs(sum_negatives) > sum_positives:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")