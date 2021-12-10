HW = [int(ax) for ax in input().split()]
chocoList = []
checkList = []
result = ""
flag = 1

for item in range(HW[0]):
    choco = []
    choco.append([int(ax) for ax in input().split()])
    chocoList.append(choco[0])
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
