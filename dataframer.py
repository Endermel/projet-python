import pandas as pd
import numpy as np
from word_cutter import list_treater

#first u have to open  the file and seperate every line like below:

df = open('./liste_francais/liste_francais.txt', "r")
lines = df.readlines()
df.close()

# remove /n at the end of each line
for index, line in enumerate(lines):
      lines[index] = line.strip().lower()



#creating a dataframe(consider you want to convert your data to 2 columns)

df_result = pd.DataFrame(columns=('word','first_letter','last_letter'))
i = 0  
for line in lines:
    first=line[0]
    last=line[-1]
    df_result.loc[i] = [line,first,last]
    i =i+1

print(df_result)

first_letter_occurrences=df_result["first_letter"].value_counts()
last_letter_occurrences=df_result["last_letter"].value_counts()

print(first_letter_occurrences)

total=len(df_result["first_letter"])



df_stat=pd.DataFrame(columns=("letter","first_stat"))
j=0
#print(first_letter_occurrences)
#print(last_letter_occurrences)
for letter_occurrence in first_letter_occurrences:
    first_stat=letter_occurrence*100/total
    #print(first_stat)
    letter=first_letter_occurrences.index[j]
    print(j)
    print(letter)
    df_stat.loc[j]=[letter,first_stat/100]
    j+=1


df_last_stat=pd.DataFrame(columns=("letter","last_stat"))
j=0
for letter_occurrence in last_letter_occurrences:
     last_stat=letter_occurrence*100/total
     print(last_stat)
     letter=last_letter_occurrences.index[j]
     print(j)
     print(letter)
     df_last_stat.loc[j]=[letter,last_stat/100]
     j+=1

#print(df_last_stat)
final_percentages=df_stat.merge(df_last_stat, on="letter", how="outer").fillna(0)

print(final_percentages)

#print(df_result.word.to_list())

#first letter
letter_list=final_percentages.letter.to_list()
first_letter_stat_list=final_percentages.first_stat.to_list()
print(sum(first_letter_stat_list))

for i in range(5):
    first_letter=np.random.choice(
    letter_list,
    p=first_letter_stat_list
    )
    print(first_letter)

# last letter check
print(sum(last_letter_occurrences))
letter_test_listing=["a","b","c","d","t"]
for letter_testing in letter_test_listing:
    last_letter_chance=final_percentages.loc[final_percentages['letter'] == letter_testing, "last_stat"].iloc[0]
    not_last_letter_chance=1-last_letter_chance
    last_letter_check=np.random.choice([True,False],p=[last_letter_chance,not_last_letter_chance])
    print(letter_testing)
    print(last_letter_chance)
    print(last_letter_check)
    
    last_letter_check=np.random.choice([True,False],p=[last_letter_chance,not_last_letter_chance])
    print(last_letter_check)

group_stats=list_treater(lines,cut_len=3)

middle_letter_test_list=["aze","mel","ose"]
for group in middle_letter_test_list:
    group_df=group_stats.loc[group_stats['preceding_group']==group]
    next_letters_list=group_df.letter.to_list()
    next_letters_stats=group_df.percent.to_list()
    print(group_df)
    print(next_letters_list)
    print(next_letters_stats)
    for i in range(5):
        next_letter=np.random.choice(next_letters_list,p=next_letters_stats)
        print(next_letter)