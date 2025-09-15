import pandas as pd
import os

data ={'Name':["dipesh","nitesh","ram","satish"],
       "Age":[23,30,35,40],
       "city":["new work","los angeles","chicago","kathmandu"]
    
}
df = pd.DataFrame(data)
print(df)

data_dir ="data"
os.makedirs(data_dir,exist_ok=True)

file_path = os.path.join(data_dir,"sample_data.csv")

df.to_csv(file_path,index=False)
print(f"csv file saved to {file_path}")

