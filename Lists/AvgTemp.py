inp = int(input("How many day's temperature? "))
temp = []
for i in range(inp):
    temp.append(float(input("Enter temperature "+str(i+1)+": ")))
avg_temp = sum(temp)/len(temp)
print("Average temperature: "+str(round(avg_temp,2)))
avgTempCnt = [high for high in temp if high > avg_temp]
if len(avgTempCnt) == 1:
    print(str(len(avgTempCnt))+" day temperature is higher than average temperature")
else:
    print(str(len(avgTempCnt))+" days temperature are higher than average temperature")
