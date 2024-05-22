h = "the weather is great"
words = h.split(' ')
for i in range(len(words)):
    if words[i] == "weather":
        temp = words[i]
        break
    else:
        temp = "not found"
print(temp)