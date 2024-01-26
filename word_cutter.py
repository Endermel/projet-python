import pandas as pd



def list_treater(word_list,cut_len):
    # creating dataframe
    df=pd.DataFrame(columns=("preceding_group","letter"))

    #for each words
    for string in word_list:
        # reverse string
        string=string[::-1]

        # Using for loop and string slicing
        out = []
        letter=[]
        # for each letter except the first of the word, checking previous letters
        for i in range(0, len(string)-1):
            #memorizing substring
            sub_string=string[i+1:i+cut_len+1][::-1]
            out.append(sub_string)
            try:
                # memorizing the letter coming after the substring
                letter.append(string[i])
            except Exception:
                pass
        #associating the data gathered with this word in the global dataframe
        for i in range(0,len(out)):
            df.loc[len(df)]=[out[i],letter[i]]

    # listing each substring gathered
    group_list=df.preceding_group.unique()
    #preparing dataframe to add percentages for each data gathered
    group_percent=pd.DataFrame(columns=("preceding_group","letter","percent"))

    #for each unique substring extracted from main data
    for group in group_list:
        # listing all the possibilities for the next letters
        next_letters=df.loc[df["preceding_group"]==group].value_counts()
        j=0
        # need total occurrences of this substring in main data
        total=len(df.loc[df["preceding_group"]==group])
        # calculating stat of each potential next letter
        for occurrence in next_letters:
            chance=occurrence*100/total
            letter=next_letters.index[j][1]
            #adding it to result dataframe
            group_percent.loc[len(group_percent)]=[group,letter,chance/100]
            j+=1

    print(group_percent)

    print(group_list)
    # returning dataframe with stats
    return group_percent

if __name__ == "__main__":
    # Defining splitting point
    n = 3
    string_list=["dzadkzaopdzaodkzapodkazp","kdozkdoplazkdazopkdzapodkzaopdkoazpzaop","dojeicvnroabpramasd","opdzkaodlpdzapdkzodpaz","azsxcdwzlapszps"]

    list_treater(word_list=string_list,cut_len=n)

