import pandas as pd 


def load_Q_data():    
    #load the csv files (clinical AND SHAS) shared by Salonee into a single pandas array 
    clinic_df = pd.read_csv("CQ10 Excel(Clinic).csv")  
    SHAS_df = pd.read_csv("CQ10 Excel(SHAS).csv")  
    df = pd.concat([clinic_df, SHAS_df], ignore_index=True)
    
    
    # Choose the columns relevant to our analysis
    df = df.filter(items=['Diagnosis', 'Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11'])
    #make all text lowecase
    df = df.map(lambda x: x.lower() if isinstance(x, str) else x)
    
    # Filter out all non 'Control' or 'iRBD' diagnoses
    df = df[df["Diagnosis"].isin(["control", "irbd"])].copy()
    
    # One-hot encode diagnoses for iRBD = 1 and Control = 0
    df = df.assign(Diagnosis=df["Diagnosis"].map({"irbd": 1, "control": 0}))
    
    # Encode yes/no/idk answers 
    Qs = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11']
    for q in Qs: 
        df[q] = df[q].map({'yes':1, 'no':0, "don't know":0.5})
    
    Qs = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11']
    plot_diagnosis_Qdata(df, 0,  "Responses from control patients",Qs)
    plot_diagnosis_Qdata(df, 1,  "Responses from patients with confirmed iRBD",Qs)
    
    #combine Q3/Q4 and drop the OG dq3/4 columns, update the Qs for plotting
    conditions = [
        (df['Q3']==0) & (df['Q4']==0), 
        ((df['Q3']==0.5) & (df['Q4']!=1)) | ((df['Q3']==0) & (df['Q4']!=1)), 
        (df['Q3']==1) | (df['Q4']==1) 
    ]
    condition_values = [0,0.5,1]
    
    df["Q3/Q4"] = np.select(conditions, condition_values, default=4433)
    df = df.drop(columns=['Q3', 'Q4'])
    
    #rearrange the order of the columns for Q3/Q4 to be in the right place
    df = df[['Diagnosis','Q1', 'Q2', "Q3/Q4", 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11']]
    
    return df     

    