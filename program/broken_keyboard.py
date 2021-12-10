keyNum = int(input())
keyList = []
checkList = []
result = ""
keyFlag = True

for item in range(keyNum):
    keyList.append(input())
keyword = input()

print("hgitp" in keyList)
while keyFlag:
ll

for H in range(HW[0]):
    chocoSum = 0
    check = ""
    for W in range(HW[1]):
        if sum(chocoList[H]) % 2 != 0:
            flag = 0
            break
        if chocoSum == sum(chocoList[H]) / 2:
            check = check + ("B" * (HW[1] - (W)))
            checkList.append(check)
            break
        chocoSum = chocoSum + chocoList[H][W]
        if chocoSum > sum(chocoList[H]) / 2:
            flag = 0
            break
        check = check + "A"
        result = "Yes"
    if flag == 0:
        result = "No"
        break

print(result)
if result == "Yes":
    for item in range(HW[0]):
        print(checkList[item])
