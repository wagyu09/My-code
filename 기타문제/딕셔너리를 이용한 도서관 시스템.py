running_day=int(input())
book_dict={}
for i in range(running_day):
    usr_input=input().split() # 띄어쓰기가 있든 없든 무조건 리스트로 취급됨
    if len(usr_input)==2: #대출일 경우 [학생이름, 책이름]이므로 원소개수가 두개이다
        book_dict[i+1]=usr_input #대출일 경우에 딕셔너리에 추가
    else: #반납일 경우에는 책 이름만 usr_input에 입력된다. 따라서 원소의 개수가 하나이다.
        for k,v in book_dict.items(): #(중요) value와 key 둘다 받기
                if v==0: continue #vaule가 0이면 이미 반납된 것이므로 인식 안함
                if usr_input[0] in v and (i+1)-k<=3:#대출한 지 3일이 지나지 않은 경우
                    print('late fee: 0won')
                    book_dict[k]=0 #반납된 경우 value 초기화
                elif usr_input[0] in v and (i+1)-k>3: #대출한 지 3일이 지난 경우
                    late_fee=((i+1)-k-3)*1000
                    print(v[1], ',', 'late fee :',late_fee)
                    book_dict[k] = 0 #반납된 경우 value 초기화

for k,v in book_dict.items(): #운영기간 전에 별도로 반납이 되지 않은 경우
    if v!=0 and running_day-k>=3:
        late_fee=(running_day-k-3)*1000
        print(v[0], ':', v[1], ',', 'late fee :',late_fee)
    elif v!=0 and running_day-k<3:
        print(v[0], ':', v[1], ',', 'late fee : 0')
