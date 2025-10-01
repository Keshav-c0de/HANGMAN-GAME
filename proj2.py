import random
from random_words import words

def valid_word(words):
    word= random.choice(words) 
    while '-' in word or ' ' in word:
        word= random.choice(words)

    return word



def main():
    word= valid_word(words).upper()

    word_letters= set(word)
    all_letters= set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    used_letters= set()
    chance=5

    print('you will have 5 lives to win the game\n')



    while len(word_letters)>0 and chance > 0:

        user_letter= input('enter you gussed letter \n').upper()
        
        
       
        if user_letter in all_letters - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print ('-------CORRECT GUESS------- \n')

            else:
                chance= chance-1
                print (F'-------INCORRECT GUESS------- \n YOU HAVE {chance} LIFES LEFT')
                

        elif user_letter in used_letters: 
            print (' -------SAME LETTER CAN\'T BE REUSED------- \n')

        else:
            print('-------INVAID INPUT------- \n')
            

        print('USED LETTERS',' '.join(used_letters))
        
        word_list= [letter if letter in used_letters else '-' for letter in word]  
        print ('GUESS THE WORD',' '.join(word_list))
       



    if chance == 0 :
        print('YOU DIED')

    else: print('CONGRATULATIONS! YOU WON')

main()
   
