#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
def text(root,permit,*confir):
    text=open(root,permit)
    if confir:
        text_text=text.readlines()
    else:
        text_text=text.read()
    text.close()
    return(text_text)

def main():
    letter=text('Input/Letters/starting_letter.txt',"r")
    invited=text('Input/Names/invited_names.txt',"r",True)

    # acc=''
    # array_invited=[]
    # for x in invited:
    #     if not x=='\n':
    #         acc+=x
    #     else:
    #         array_invited.append(acc)
    #         acc=''
    for invite in invited:
        stripped_name = invite.strip()
        result=letter.replace('[name]',stripped_name)
        save=open(f"Output/{stripped_name}.txt",'w')
        save.write(result)
        
    

main()     