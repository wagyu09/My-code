import sys
input=sys.stdin.readline

n=int(input())
answer_list=[]
for i in range(n):
    usr_input=int(input())
    answer_list.append(usr_input)

temp_list,comp_list,final_list=[],[],[]
count_a=1
count_b=0
while True:
    if len(final_list)==2*n:break
    if len(temp_list)==0:
        temp_list.append(count_a)
        final_list.append('+')
        count_a+=1
    elif answer_list[count_b]==temp_list[-1]:
        comp_list.append(temp_list.pop());final_list.append('-');count_b += 1
    else:
        temp_list.append(count_a)
        final_list.append('+')
        count_a+=1
if answer_list==comp_list:
    for i in final_list:
        print(i)
else: print('NO')

