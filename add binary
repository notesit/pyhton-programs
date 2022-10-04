print(end="Enter First Binary Number: ")
nOne = int(input())
print(end="Enter Second Binary Number: ")
nTwo = int(input())

nOne = str(nOne)
nTwo = str(nTwo)
mLen = max(len(nOne), len(nTwo))
nOne = nOne.zfill(mLen)
nTwo = nTwo.zfill(mLen)
addRes = ""
carry = 0

for i in range(mLen - 1, -1, -1):
    re = carry
    re += 1 if nOne[i] == '1' else 0
    re += 1 if nTwo[i] == '1' else 0
    addRes = ('1' if re%2==1 else '0') + addRes
    carry = 0 if re<2 else 1

if carry!=0:
    addRes = '1' + addRes

print("\n" + nOne + " + " + nTwo + " = " + addRes)
