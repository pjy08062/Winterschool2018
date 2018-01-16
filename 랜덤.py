import random

ans1="자 해보세요!"
ans2="됐네요"
ans3="다시 생각해보세요."
ans4="모르니 두려운 것입니다."
ans5="잘 하고 있어요!"
ans6="당신이라면 할 수 있어요!"
ans7="해도 그만, 안 해도 그만"
ans8="당신은 올바른 선택을 했어요."

print("MyMagic8Ball에 오신 것을 환영합니다.")


question = input("조언을 구하고 싶으면 질문을 입력하고 엔터 키를 누르세요.\n")

print("고민 중...\n" * 4)

choice=random.randint(1, 8)
if choice==1:
    answer=ans1
    
elif choice==2:
    answer=ans2
    
elif choice==3:
    answer=ans3
    
elif choice==4:
    answer=ans4
    
elif choice==5:
    answer=ans5
    
elif choice==6:
    answer=ans6
    
elif choice==7:
    answer=ans7
    
else:
    answer=ans8
    
print(answer)

input("\n\n마치려면 엔터 키를 누르세요.")
