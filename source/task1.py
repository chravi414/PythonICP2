weight_lbs = []
weight_kgs = []
CONVERSION_FACTOR = 0.453592
n = int(input('No.of Students: \n'))
i = 1
while i <= n:
    wt = int(input())
    weight_lbs.append(wt)
    i = i + 1

for i in weight_lbs:
    weight_kgs.append(round((i * CONVERSION_FACTOR), 2))

print(weight_kgs)
