import random
input_tuple=('mumbai','chennai','delhi','panaji')
final_tuple=()
flag=False
lst=list(input_tuple)
random.shuffle(lst)
final_tuple=final_tuple+tuple(lst)
charlst=list(final_tuple[0])
random.shuffle(charlst)
new_word=''.join(charlst)
print("Jumbled word is:",new_word)
print("User has 10 chances to guess the word:")
for i in range(0,11):
    user_guess=raw_input("enter the guess:")
    if user_guess==final_tuple[0]:
        print("You Have Won in:",i+1,"chances")
        flag=True
        break
    else:
        continue
if flag==False:
        print("You have lost the game")
