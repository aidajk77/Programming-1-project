import random          #importing module


alphabet="abcdefghijklmnopqrstuvwxyz"     #string with all letters in the alphabet


db={
    "a":[["aid","and","are"],["acid","ally","army"],["above","after","angle"],["absent","absurd","accept"]],
    "b":[["bad","bed","bar"],["bait","bank","belt"],["board","bread","break"],["backup","baking","ballet"]],
    "c":[["car","cat","cry"],["call","cake","cell"],["child","catch","cheap"],["cactus","camera","cancel"]],
    "d":[["day","dry","dog"],["dawn","dead","deal"],["dance","drink","daily"],["dagger","danger","decade"]],
    "e":[["ear","eat","end"],["easy","earn","east"],["empty","earth","enter"],["editor","effect","elixir"]],
    "f":[["far","fat","fan"],["fail","fake","fall"],["field","fault","fiber"],["falcon","family","father"]],
    "g":[["gas","get","gig"],["gate","gear","gene"],["gamer","glass","gloat"],["galaxy","gambit","garden"]],
    "h":[["hat","hog","hit"],["hair","head","half"],["habit","heavy","honey"],["hammer","hacker","handle"]],
    "i":[["ice","ick","ill"],["icon","idea","idol"],["idiot","issue","irony"],["ignore","incest","income"]],
    "j":[["joy","job","jun"],["jail","joke","join"],["jelly","juice","jewel"],["jersey","joking","jaguar"]],
    "k":[["key","kit","KIA"],["kiwi","kill","kick"],["kebab","knife","knock"],["kidnap","karate","keeper"]],            #mini database with words for every letter
    "l":[["lab","lap","leg"],["love","lake","long"],["labor","label","large"],["labour","layout","league"]],            #'x' and 'q' don't have words with 3 letters, so they have one less sublist from other letters
    "m":[["man","mom","mud"],["maid","make","more"],["magic","major","mango"],["magnet","makeup","manage"]],
    "n":[["new","net","now"],["name","nail","need"],["never","needy","niece"],["nectar","needle","nephew"]],
    "o":[["oil","owl","odd"],["omit","once","oven"],["ocean","occur","opera"],["occupy","office","obtain"]],
    "p":[["pet","pat","pay"],["pair","pace","pain"],["panda","panic","pants"],["palace","parent","parrot"]],
    "q":[["quiz","quad","quip"],["queen","quart","query"],["quotes","quests","quoted"]],
    "r":[["rat","raw","red"],["race","rain","rail"],["radar","reise","ratio"],["rabbit","racing","racist"]],
    "s":[["saw","sad","sun"],["soap","same","sale"],["salon","santa","scale"],["safari","safety","salary"]],
    "t":[["tag","tap","tax"],["tape","tail","tall"],["table","tango","teddy"],["tailor","talent","tablet"]],
    "u":[["use","USB","UNO"],["ugly","upon","user"],["uncle","union","until"],["unable","unfair","unique"]],
    "v":[["vet","van","var"],["vape","vein","vibe"],["value","valid","vault"],["vacuum","vaping","vector"]],
    "w":[["why","war","wet"],["what","warm","wall"],["waist","waste","water"],["window","wallet","warden"]],
    "x":[["xbox","xiao","Xray"],["xenia","xeric","xerox"],["xenial","xenias","xyloid"]],
    "y":[["yes","you","yet"],["year","yawn","yard"],["youth","young","yacht"],["yearly","yellow","yogurt"]],
    "z":[["zoo","zen","zap"],["zoom","zone","zero"],["zebra","zoned","zesty"],["zodiac","zombie","zipper"]],
}


command=""
print("Hello!")
command=input("Press 1 to play, press 2 to see a leaderboard, press 3 to exit!")        #starting menu which is making sure that user is pressing the right keys
while(command !="1" and command !="2" and command !="3"):   
    print("Press valid key!")              
    command=input()
   
    
while(command=="1" or command=="2"):
  
    if(command=="1"):
        print("Welcome to our little guessing game!")
        print("The goal is to have the smallest score!")          #asking user for his username
        print("Type your username!")
        username=input()
       

        print("For the first guessing task, you need to guess the first letter of a word I imagined!")
        print("For every miss you get +1 on your score!")

        first_letter=random.randrange(0,len(alphabet))          #first_letter is getting random number which represents a place of the letter in the alphabet
        
        score=0           #variable score represents the users score in the game

        letter_guess=input("Your first guess is: ")
        while(letter_guess not in alphabet):
            letter_guess=input("Enter a letter, nothing else!")
        while(letter_guess!=alphabet[first_letter]):                         #asking user to guess the first letter of the word which is stored in the variable letter_guess while making sure that the user is entering letter and nothing else   
            letter_guess=input("Wrong, try again! Your next guess is: ")     #if user doesn't guess right he gets +1 score, and program asks him to guess again
            while(letter_guess not in alphabet):
                letter_guess=input("Enter a letter, nothing else!")
            score+=1
        print("Good job!")

    


        if(letter_guess=="q" or letter_guess=="x"):
            number_of_letter=random.randrange(0,3)               #computer randomly chooses how many letters is there going to be in the word and store the length of the word in the variable number_of_letter
        else:
                number_of_letter=random.randrange(0,4)
        
        print("Now try to guess number of letters of the word I imagined!")
        print("For every miss you get +3 on your score!")
       
        number_guess=input("If your words starts with 'q' or 'x' try to guess a number between 4 and 6, or else try to guess number between 3 and 6. Your first guess of how many letters are there in the word I imagined is: ")

        while((letter_guess=="x" or letter_guess=="q") and (number_guess.isalpha() or (number_guess!="4" and number_guess!="5" and number_guess!="6"))):
            number_guess=input("Enter a valid number, nothing else!")                                                                                                              
        while(letter_guess!="x" and letter_guess!="q" and (number_guess.isalpha() or (number_guess!="3" and number_guess!="4" and number_guess!="5" and number_guess!="6"))):      #Protection from errors
            number_guess=input("Enter a valid number, nothing else!")
        
        
        if(number_of_letter==0 and (letter_guess=="q" or letter_guess=="x")):
            while(number_guess!="4"):                                           #checking if the user guessed the correct number, if not he gets +3 score, and he guesses again
                number_guess=input("Wrong, try again! Your next guess is: ")
                while((letter_guess=="x" or letter_guess=="q") and (number_guess.isalpha() or (number_guess!="4" and number_guess!="5" and number_guess!="6"))):
                    number_guess=input("Enter a valid number, nothing else!")                                                                                                               
                while(letter_guess!="x" and letter_guess!="q" and (number_guess.isalpha() or (number_guess!="3" and number_guess!="4" and number_guess!="5" and number_guess!="6"))):
                    number_guess=input("Enter a valid number, nothing else!")
                score+=3


        if(number_of_letter==0 and letter_guess!="q" and letter_guess!="x"):
            while(number_guess!="3"):                                          #checking if the user guessed the correct number, if not, he gets +3 score and he guesses again
                number_guess=input("Wrong, try again! Your next guess is: ")
                while((letter_guess=="x" or letter_guess=="q") and (number_guess.isalpha() or (number_guess!="4" and number_guess!="5" and number_guess!="6"))):
                    number_guess=input("Enter a valid number, nothing else!")
                while(letter_guess!="x" and letter_guess!="q" and (number_guess.isalpha() or (number_guess!="3" and number_guess!="4" and number_guess!="5" and number_guess!="6"))):
                    number_guess=input("Enter a valid number, nothing else!")
                score+=3

       
        if(number_of_letter==1 and (letter_guess=="q" or letter_guess=="x")):
            while(number_guess!="5"):                                           #checking if the user guessed the correct number, if not he gets +3 score, and he guesses again
                number_guess=input("Wrong, try again! Your next guess is: ")
                while((letter_guess=="x" or letter_guess=="q") and (number_guess.isalpha() or (number_guess!="4" and number_guess!="5" and number_guess!="6"))):
                    number_guess=input("Enter a valid number, nothing else!")
                while(letter_guess!="x" and letter_guess!="q" and (number_guess.isalpha() or (number_guess!="3" and number_guess!="4" and number_guess!="5" and number_guess!="6"))):
                    number_guess=input("Enter a valid number, nothing else!")
                score+=3

           
        if(number_of_letter==1 and letter_guess!="q" and letter_guess!="x"):
            while(number_guess!="4"):                                            #checking if the user guessed the correct number, if not he gets +3 score, and he guesses again
                number_guess=input("Wrong, try again! Your next guess is: ")
                while((letter_guess=="x" or letter_guess=="q") and (number_guess.isalpha() or (number_guess!="4" and number_guess!="5" and number_guess!="6"))):
                    number_guess=input("Enter a valid number, nothing else!")
                while(letter_guess!="x" and letter_guess!="q" and (number_guess.isalpha() or (number_guess!="3" and number_guess!="4" and number_guess!="5" and number_guess!="6"))):
                    number_guess=input("Enter a valid number, nothing else!")
                score+=3

               
        if(number_of_letter==2 and (letter_guess=="q" or letter_guess=="x")):
            while(number_guess!="6"):                                            #checking if the user guessed the correct number, if not he gets +3 score, and he guesses again
                number_guess=input("Wrong, try again! Your next guess is: ")
                while((letter_guess=="x" or letter_guess=="q") and (number_guess.isalpha() or (number_guess!="4" and number_guess!="5" and number_guess!="6"))):
                    number_guess=input("Enter a valid number, nothing else!")
                while(letter_guess!="x" and letter_guess!="q" and (number_guess.isalpha() or (number_guess!="3" and number_guess!="4" and number_guess!="5" and number_guess!="6"))):
                    number_guess=input("Enter a valid number, nothing else!")
                score+=3

               
        if(number_of_letter==2 and letter_guess!="q" and letter_guess!="x"):
            while(number_guess!="5"):                                           #checking if the user guessed the correct number, if not he gets +3 score, and he guesses again
                number_guess=input("Wrong, try again! Your next guess is: ")
                while((letter_guess=="x" or letter_guess=="q") and (number_guess.isalpha() or (number_guess!="4" and number_guess!="5" and number_guess!="6"))):
                    number_guess=input("Enter a valid number, nothing else!")
                while(letter_guess!="x" and letter_guess!="q" and (number_guess.isalpha() or (number_guess!="3" and number_guess!="4" and number_guess!="5" and number_guess!="6"))):
                    number_guess=input("Enter a valid number, nothing else!")
                score+=3


        if(number_of_letter==3 and letter_guess!="q" and letter_guess!="x"):
            while(number_guess!="6"):                                           #checking if the user guessed the correct number, if not he gets +3 score, and he guesses again
                number_guess=input("Wrong, try again! Your next guess is: ")
                while((letter_guess=="x" or letter_guess=="q") and (number_guess.isalpha() or (number_guess!="4" and number_guess!="5" and number_guess!="6"))):
                    number_guess=input("Enter a valid number, nothing else!")
                while(letter_guess!="x" and letter_guess!="q" and (number_guess.isalpha() or (number_guess!="3" and number_guess!="4" and number_guess!="5" and number_guess!="6"))):
                    number_guess=input("Enter a valid number, nothing else!")
                score+=3
                

        print("Good job! Now all you need to do is guess the word I imagined!")
        print("For every miss you get +5 on your score!")


        print("Guess the word I imagined between these words: ", db[letter_guess][number_of_letter])  

        number_of_word=random.randrange(0,3)        #computer randomly chooses the word
       
        word_guess=input("Your first guess is: ")

        while(word_guess.lower()!=db[letter_guess][number_of_letter][0].lower() and word_guess.lower()!=db[letter_guess][number_of_letter][1].lower() and word_guess.lower()!=db[letter_guess][number_of_letter][2].lower()):
            word_guess=input("Enter the correct word!")                       #ensuring that the user correctly writes a word from the list

     
        while(word_guess.lower()!=db[letter_guess][number_of_letter][number_of_word].lower()):
            word_guess=input("Wrong! Try again! Your next guess is: ")            #user guesses the word, if he doesn't pick correctly, he gets +5 on the score and guesses again
            while(word_guess.lower()!=db[letter_guess][number_of_letter][0].lower() and word_guess.lower()!=db[letter_guess][number_of_letter][1].lower() and word_guess.lower()!=db[letter_guess][number_of_letter][2].lower()):
                word_guess=input("Enter the correct word!")                       
            score+=5


        print("Well done,",username,"your score is",score)

        
        f=open("project_leaderboard.txt","a")
        f.write(username+" "+str(score)+"\n")       #storing users score in the file called project_leaderboard.txt
        f.close()

        command=input("Press 1 to play, press 2 to see a leaderboard, press 3 to exit!")
        while(command !="1" and command !="2" and command !="3"):                       #asking user what does he want to do now
            command=input("Press valid key!")
    
    if(command=="2"):
        f=open("project_leaderboard.txt","r")
        for line in f:                          #letting user see the list from the file project_leaderboard.txt
            print(line)
        f.close()
        
        print("Press 1 to play, press 2 to see a leaderboard, press 3 to exit!")    #asking user what does he want to do now
        command=input()
        while(command !="1" and command !="2" and command !="3"):
            command=input("Press valid key!")    
           
print("Goodbye")   