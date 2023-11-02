# comphrehension of the python

square= [x**2 for x in range(5)]
print(square)

even_numbers=[x for x in range(10) if x%2==0]
print(even_numbers)

result=['Pass' if score >=60 else 'Fail' for score in [75, 30, 85, 50, 20, 12]]
print(result)

names=['John', 'Jane', 'Jim']
name_lengh=[len(name) for name in names]
print(name_lengh)