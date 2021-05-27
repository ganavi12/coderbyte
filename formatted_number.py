# Input: ["0.232567"]
# Output: true

# Input: ["2,567.00.2"]
# Output: false


def FormattedNumber(strArr):
    c = 0
    for i in range(len(strArr[0])):
        if strArr[0][i] == '.':
            c = c + 1
    strArr = "false"
    if c == 1:
        strArr = "true"
        return strArr
    # elif c <= 0: 
    #   strArr = "true"
    #   return strArr
    else:
        return strArr

print(FormattedNumber(input()))