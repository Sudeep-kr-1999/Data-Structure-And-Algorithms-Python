# <<<<<<<<<<<<<<<<[ Print all words having frequency "k" in a given string]>>>>>>>>>>>>>>>>>>>>

s="this is a word string having many many words"
# k=2
# s=s.split()
# print(s)

# d={}
# for w in s:
#     if w in d:
#         d[w]=d[w]+1
#     else:
#         d[w]=1

# print(d)



# for w in s:
#     d[w]=d.get(w,0)+1

# # print(d)
# for w in d:
#     if d[w]==k:
#         print(w)

def printFreqWords(s,k):
    words=s.split()
    d={}
    for w in words:
        d[w]=d.get(w,0)+1
    for w in d:
        if d[w]==k:
            print(w)

printFreqWords(s,1)


