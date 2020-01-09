map_temp = map(lambda x : x ** 2 if x > 7 else x ** 3, [1, 3, 5, 7, 9])

print(map)

for i in map_temp:
    print(i)
