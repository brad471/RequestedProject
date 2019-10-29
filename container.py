import pandas as pd
import numpy as np
#This will be the file that contains all the methods for the dataframe
df = pd.DataFrame(columns = ["Author","Quote","Topic","Thoughts","Source"])

#this should add a new row to the df given the user input
def add_information():
    data = df.copy()
    author = input("Type the author of the quote then press enter: ")
    quote  = input("Type the quote then press enter: ")
    topic  = input("Type the topic of the quote then press enter: ")
    thought = input("Type your thought on the quote then press enter: ")
    source = input("Type the source of the quote then press enter: ")
    data.loc[data.size + 1] = [author,quote,topic,thought,source]
    return data
print(add_information())
#edit information
#remove Quote
#sorting/retrival

