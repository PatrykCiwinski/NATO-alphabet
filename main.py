import pandas as pd

df=pd.read_csv("nato_phonetic_alphabet.csv")

df_dic={row.letter:row.code for (index,row) in df.iterrows()}

word=input("Enter word: ").upper()

nato_word=[df_dic[letter]for letter in word]

print(nato_word)
