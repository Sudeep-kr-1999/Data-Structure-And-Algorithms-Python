# <<<<<<<<<<<<<<<<<<<<[ Return all keypad combinations]>>>>>>>>>>>>>>>>>>>>>

def getstirng(d):
    if d==2:
        return "abc"
    if d==3:
        return "def"
    if d==4:
        return "ghi"
    if d==5:
        return "jkl"
    if d==6:
        return "mno"
    if d==7:
        return "pqrs"
    if d==8:
        return "tuv"
    if d==9:
        return "wxyz"
    return " "


def keypad(n):
    if n==0:
        output=[]
        output.append("")
        return output
    smaller_number=n//10
    last_digit=n%10
    smaller_output=keypad(smaller_number)
    options_for_last_digit=getstirng(last_digit)
    output_list=[]
    for s in smaller_output:
        for c in options_for_last_digit:
            option=s+c
            output_list.append(option)

    return output_list

print(keypad(23))
print(len(keypad(23)))






