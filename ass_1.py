import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def question_8():
   df = pd.read_csv('data.csv', encoding='latin-1')
   posc = df[df['HS'] == 0].count()
   ngvc = df[df['HS'] == 1].count()
   
   divisions = ["Positive", "Negative"]
   division_average_marks = [posc['HS'], ngvc['HS']]
   plt.bar(divisions, division_average_marks, color='green')
   plt.title("bar graph")
   plt.xlabel("Tweet")
   plt.ylabel("Count")
   plt.show()

if __name__ == "__main__":
    question_8()
