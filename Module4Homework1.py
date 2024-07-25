from fake_math import divide as fake_div
from true_math import divide as true_div


result1 = fake_div(7, 2)
result2 = fake_div(43, 0)
result3 = true_div(18, 3)
result4 = true_div(99, 0)


print(result1)
print(result2)
print(result3)
print(result4)
