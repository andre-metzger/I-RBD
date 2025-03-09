import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np



def plot_diagnosis_Qdata(data_frame, dc, plot_title, Qs, save=False, save_title=None):
    #input
    # dc (binary int) --> diagnosis code (1 or 0) 
    #plot_title (string) --> the string that you would like to be the title of the plot
    #save_title (string) --> the file name under which you want to save the plot 
    
    #output
    #the output of this function will be a plot which will be autamatically generated 
    #the plot will contain the % of answers (yes, no, idk, NaN) for each question that 
    #was asked as part of the Q10 questionare 
    
    plot_df = data_frame[data_frame["Diagnosis"]==dc].copy().drop("Diagnosis", axis=1)

    
    value_counts = plot_df.apply(pd.Series.value_counts).fillna(0)
    value_counts.loc["nan"] = plot_df.shape[0] - value_counts.sum(axis=0) 
    value_counts = value_counts/plot_df.shape[0] ##NORMALIZER###
    
    x_vals = np.arange(value_counts.shape[1])
    bar_width = 0.2

    plt.bar(x_vals- 1.5*bar_width, value_counts.loc[1], width=bar_width, color = "green", label="Yes")
    plt.bar(x_vals- 0.5*bar_width, value_counts.loc[0.5], width=bar_width, color = "orange", label="IDK")
    plt.bar(x_vals+ 0.5*bar_width, value_counts.loc[0], width=bar_width, color = "grey", label="No")
    plt.bar(x_vals+ 1.5*bar_width, value_counts.loc["nan"],width=bar_width, color = "red", label="NaN")
    plt.xticks(x_vals,Qs)
    plt.xlabel("Question", fontsize=14)
    plt.ylabel("% of patient responses (n="+str(plot_df.shape[0])+")",fontsize=18)
    plt.ylim(0,1)
    plt.legend(title='Answers')
    plt.title(plot_title, fontsize=14) 
    
    plt.grid(visible=False)
    if save: 
        plt.savefig(save_title)
    plt.show()
    
    

    
    
def plot_diagnosis_Qdata_nono(data_frame, dc, plot_title, save_title):
    #input
    # dc (binary int) --> diagnosis code (1 or 0) 
    #plot_title (string) --> the string that you would like to be the title of the plot
    #save_title (string) --> the file name under which you want to save the plot 
    
    #output
    #the output of this function will be a plot which will be autamatically generated 
    #the plot will contain the % of answers (yes, idk, NaN) for each question that 
    #was asked as part of the Q10 questionare 
    #THIS FUNCTION IS UNIQUE AS THE NO ANSWERS WILL NOT BE PLOTTED 
    
    plot_df = data_frame[data_frame["Diagnosis"]==dc].copy().drop("Diagnosis", axis=1)

    
    value_counts = plot_df.apply(pd.Series.value_counts).fillna(0)
    value_counts.loc["nan"] = plot_df.shape[0] - value_counts.sum(axis=0) 
    value_counts = value_counts/plot_df.shape[0] ##NORMALIZER###
    
    x_vals = np.arange(value_counts.shape[1])
    bar_width = 0.2

    plt.bar(x_vals- bar_width, value_counts.loc[1], width=bar_width, color = "green", label="Yes")
    plt.bar(x_vals, value_counts.loc[0.5], width=bar_width, color = "orange", label="IDK")
    plt.bar(x_vals+ bar_width, value_counts.loc["nan"],width=bar_width, color = "red", label="NaN")
    plt.xticks(x_vals,Qs)
    plt.xlabel("Question",fontsize=14)
    plt.ylabel("% of patient responses (n="+str(plot_df.shape[0])+")",fontsize=14)
    plt.ylim(0,1)
    plt.legend(title='Answers')
    plt.title(plot_title,fontsize=14) 

        
    plt.grid(visible=False)
    plt.savefig(save_title)
    plt.show()