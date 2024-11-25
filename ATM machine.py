print("*"*20,"atm machine","*"*20)
amount = int(input("enter the amount:"))
l = [500,200,100,50,20,10,5,2,1]
c=0
for i in l:
    notes = amount//i
    c=c+notes
    print(f"{i} notes--> {notes}")
    #amount = amount-i%notes
    amount =amount%i
print("minimum number of notes:",c)