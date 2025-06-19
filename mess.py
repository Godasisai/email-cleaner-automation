import pandas as pd

# Load your CSV — make sure the file exists in the same folder
filename = "input_data.csv"  # 👈 Replace with your actual CSV file
df = pd.read_csv(filename)

# 1. Remove duplicate rows based on 'email'
df = df.drop_duplicates(subset='email')

# 2. Normalize 'has_joined_event' (replace 'Yes'/'No' with True/False)
df['has_joined_event'] = df['has_joined_event'].map({'Yes': True, 'No': False})

# 3. Flag missing or incomplete LinkedIn profiles
linkedin_col = 'What is your LinkedIn profile?'
df['linkedin_missing_or_incomplete'] = (
    df[linkedin_col].isna() |
    df[linkedin_col].str.strip().eq('') |
    ~df[linkedin_col].str.contains('linkedin.com', na=False)
)

# 4. Flag missing job titles
df['job_title_missing'] = (
    df['Job Title'].isna() |
    df['Job Title'].str.strip().eq('')
)

# 5. Create personalized message
def create_message(row):
    name = row['name'].split()[0]  # Get first name
    job = row['Job Title'] if pd.notna(row['Job Title']) else 'professional'
    joined = row['has_joined_event']

    if joined:
        return f"Hey {name}, thanks for joining our session! As a {job}, we think you’ll love our upcoming AI workflow tools. Want early access?"
    else:
        return f"Hi {name}, sorry we missed you at the last event! We’re preparing another session that might better suit your interests as a {job}."

df['message'] = df.apply(create_message, axis=1)

# 6. Save cleaned data and messages
df.to_csv('cleaned_output.csv', index=False)
df[['email', 'message']].to_csv('messages.csv', index=False)

print("✅ Cleaning and messaging done. Files saved: cleaned_output.csv, messages.csv")
