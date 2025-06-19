import pandas as pd

# 🔹 STEP 1: Load your CSV file into a DataFrame
df = pd.read_csv("input_data.csv")  # 🔁 Replace 'input.csv' with your actual file name

# 🔹 STEP 2: Column name constants
EMAIL_COL = 'email'
JOINED_COL = 'has_joined_event'
LINKEDIN_COL = 'What is your LinkedIn profile?'
JOB_TITLE_COL = 'Job Title'

# 🔹 STEP 3: Remove duplicate rows based on 'email'
df = df.drop_duplicates(subset=EMAIL_COL)

# 🔹 STEP 4: Normalize 'has_joined_event' → "Yes" to True, "No" to False
df[JOINED_COL] = df[JOINED_COL].map({'Yes': True, 'No': False}).astype('boolean')

# 🔹 STEP 5: Check incomplete LinkedIn profiles
def linkedin_incomplete(link):
    if pd.isna(link) or link.strip() == "" or "linkedin.com" not in link.lower():
        return True
    return False

df['linkedin_missing_or_incomplete'] = df[LINKEDIN_COL].apply(linkedin_incomplete)

# 🔹 STEP 6: Flag missing job titles
df['job_title_missing'] = df[JOB_TITLE_COL].isna() | (df[JOB_TITLE_COL].str.strip() == "")

# 🔹 STEP 7: Save cleaned data to new file
df.to_csv("cleaned_output.csv", index=False)

print("✅ Cleaning complete. Saved to 'cleaned_output.csv'")
