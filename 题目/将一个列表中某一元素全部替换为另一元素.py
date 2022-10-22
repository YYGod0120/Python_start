lst = ['python','teacher','Java','c++']
for i in range(len(lst)):
    word = lst[i]
    if word.capitalize() == word:
        continue
    else:
        lst[i] = word.capitalize()
print(lst)


