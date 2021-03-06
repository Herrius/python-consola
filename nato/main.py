student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
phonetic_alphabet=pandas.read_csv("D:/python-consola/nato/nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
dictionray_phonetic={row.letter:row.code for (index,row) in phonetic_alphabet.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def natoPhonetic():
    name=input("Should you write a name?").upper()
    name_phonetic=[dictionray_phonetic[letter] for letter in name]  
    print(name,name_phonetic)
loop=False
while not loop:
    try:
        natoPhonetic()
    except KeyError:
        print("Por favor solo insertar letras")
    else:
        loop=True
        
