def knight_poss:
    -

test_cases = int(input())
main=[]
for t in range(0,test_cases):

    knight_no = int(input())

# now this takes care of knight positions
    for i in range(0,knight_no):
        s = input()
        numbers = list(map(int, s.split()))
        main.append(numbers)

# so main has list of lists which has knight position
    print("the input is")
    for i in range(len(main)):
        print(main[i])p

