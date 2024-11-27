import dice
print("*"*9,"HILL CLIMB FALL","*"*9)
player_1=input("enter player_1 name:")
player_2=input("enter player_2 name:")
list_a=[]
list_b=[]
i=0
while(sum(list_a)!=10 and sum(list_b)!=10):
    if(i%2==0 and input("player_1 enter p to play:")=='p'):
        if(sum(list_a)<10):
            diceno=dice.diceroll()
            print("\n diceno-->",diceno)
            list_a.append(diceno)
        else:
            list_a.clear()
        print("step no.-->",sum(list_a))
        i+=1
    elif(i%2!=0 and input("player_2 enter p to play:")=='p'):
        if(sum(list_b)<10):
           diceno=dice.diceroll()
           print("\n diceno-->",diceno)
           list_b.append(diceno) 
        else:
            list_b.clear()
        print("stepno.-->",sum(list_b))
        i+=1
    else:
        break
if(sum(list_a)==10):
    print(f"{player_1} is the winner...")
elif(sum(list_b)==10):
    print(f"{player_2} is the winner...")
else:
    print("thank you!!!")           