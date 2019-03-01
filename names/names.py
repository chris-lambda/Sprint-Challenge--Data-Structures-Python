import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


l_dict = {}
duplicates = []
for name in names_1:
    l = len(name)
    if str(l) in l_dict.keys():
        l_dict[str(l)].append(name)
    else:
        l_dict[str(l)] = [name]

for name in names_2:
    l = len(name)
    if str(l) in l_dict.keys():
        if name in l_dict[str(l)]:
            duplicates.append(name)
        else:
            l_dict[str(l)].append(name)
    else:
        l_dict[str(l)] = [name]


# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

