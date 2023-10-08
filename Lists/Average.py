l = []
while(True):
    inp = input("Enter a number: ")
    if inp == "done":
        break
    l.append(float(inp))
avg = sum(l)/len(l)
print(avg)