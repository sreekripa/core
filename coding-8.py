# odd=[]
# for i in range(0,100):
#     if i%2==1:
#         odd.append(i)
# print(odd)

odd=[i for i in range(0,100) if i%2==1]
print("odd numbers=",odd)