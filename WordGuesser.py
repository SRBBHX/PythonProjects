import random
myList = ["Ram", "Shyam", "Laxmana", "Sita", "Hanuman", "Ravan", "Bali", "Angad", "Akshay", "Jatayu", "Indrajeet"]
# Name=input("Enter your good name please!\n")
# print("Hello ", Name)
RanWord = random.choice(myList)
print(RanWord)
print("Chouse a random character of *RAYAMANA*")
BlankList = []

for Blank in range(0, len(RanWord)):
    BlankList.append("_")
flag=1

def WordChecker():
    for i in range(0, len(RanWord)):
        char = input("Enter a random alphabet: ")
        for index, k in enumerate(RanWord, start=0):
            if char == k:
                print("Alphabet matched")
                alphaFiller(index, char)  
                print(f"len {len(RanWord) , index}")
                # if index + 1 == len(RanWord):
                #     break
            else:
                global flag
                flag = 0
                print("You guessed a wrong characte\nYou lost!")
        if flag == 0:
            break
            
                
                
def alphaFiller(idx,C):
    BlankList[idx]= C
    fOutput(BlankList)
    
    
def fOutput(listt):
        for j in listt:
            print(j)

                   
                
        


WordChecker()



