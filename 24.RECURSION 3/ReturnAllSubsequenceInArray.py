# <<<<<<<<<<<<[  Returning all subsequence of in  the string]>>>>>>>>>>>>>>>>>>>>>>

def subsequence(s):
    if len(s)==0:
        output=[]
        output.append("")
        return output
    smaller_string=s[1:]
    smaller_output=subsequence(smaller_string)
    output=[]
    for sub in smaller_output:
        output.append(sub)
    for sub in smaller_output:
        subs_with_zeroth_character=s[0]+sub
        output.append(subs_with_zeroth_character)
    return output

print(subsequence("abcd"))

