import pandas as pd

#first u have to open  the file and seperate every line like below:

df = open('./liste_francais/liste_francais.txt', "r")
lines = df.readlines()
df.close()

# remove /n at the end of each line
for index, line in enumerate(lines):
      lines[index] = line.strip().lower()



#creating a dataframe(consider u want to convert your data to 2 columns)

df_result = pd.DataFrame(columns=('word','first_letter','last_letter'))
i = 0  
for line in lines:
    first=line[0]
    last=line[-1]
    df_result.loc[i] = [line,first,last]
    i =i+1

#print(df_result)

first_letter_occurrences=df_result["first_letter"].value_counts()
last_letter_occurrences=df_result["last_letter"].value_counts()

total=len(df_result["first_letter"])



df_stat=pd.DataFrame(columns=("letter","first_stat"))
j=0
#print(first_letter_occurrences)
#print(last_letter_occurrences)
for letter_occurrence in first_letter_occurrences:
    first_stat=letter_occurrence*100/total
    #print(first_stat)
    letter=first_letter_occurrences.index[j]
    df_stat.loc[j]=[letter,first_stat]
    j+=1


df_last_stat=pd.DataFrame(columns=("letter","last_stat"))
j=0
for letter_occurrence in last_letter_occurrences:
     last_stat=letter_occurrence*100/total
     letter=last_letter_occurrences.index[j]
     df_last_stat.loc[j]=[letter,last_stat]
     j+=1

#print(df_last_stat)

print(df_stat.merge(df_last_stat, on="letter", how="outer").fillna(0))
