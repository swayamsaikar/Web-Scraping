import pandas as pd

# reading the dataset
df = pd.read_csv("finaldata.csv")

del df["duplicateStars"], df['duplicateConst'], df["DuplicateAncesion"], df["Discovery_year_sorted"]

# df.dropna(axis="columns")


df.to_csv("cleaned_data.csv")
