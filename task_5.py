import pandas as pd

df = pd.read_csv('fit_trackr_data.csv')


# 1. Ukloni potpune duplikate
df = df.drop_duplicates()

# 2. Ukloni redove gde nema vrednosti u koloni 'Username'
df = df.dropna(subset=['Username'])

# 3. Ekstrahuj numericke vrednosti iz Duration 
df['Duration'] = df['Duration'].str.replace('min', '', case=False).str.strip()
df['Duration'] = pd.to_numeric(df['Duration'], errors='coerce')

# 4. Ekstrahuj numericke vrednosti iz Calories 
df['Calories'] = df['Calories'].str.replace('kcal', '', case=False).str.strip()
df['Calories'] = pd.to_numeric(df['Calories'], errors='coerce')

# 5. Standardizuj kolonu Activity

df['Activity'] = df['Activity'].str.lower().str.strip()
activity_map = {
    'walking': 'walking',
    'walk': 'walking',
    'run': 'running',
    'running': 'running',
    'cycle': 'cycling',
    'cycling': 'cycling',
    'yoga': 'yoga',
    'joga': 'yoga',
}

df['Activity'] = df['Activity'].replace(activity_map)

#  ANALIZE 

# 1. Prosecno trajanje aktivnosti 
avg_duration = df['Duration'].mean()
print(f"Prosecno trajanje aktivnosti: {avg_duration:.2f} min")

# 2. Najcesce raspolozenje korisnika nakon aktivnosti 
most_common_mood = df['Mood'].mode()
if not most_common_mood.empty:
    print(f"Najcesce raspolozenje nakon aktivnosti: {most_common_mood[0]}")
else:
    print("Nema podataka o raspolozenju.")

# 3. Varijacija broja potrosenih kalorija 
calories_std = df['Calories'].std()
print(f"Standardna devijacija potrosenih kalorija: {calories_std:.2f} kcal")

# 4. Razlika u godinama izmedju najstarijeg i najmladjeg korisnika iz sredisnjih 50% podataka
q1_age = df['Age'].quantile(0.25)
q3_age = df['Age'].quantile(0.75)
iqr_age = q3_age - q1_age
print(f"Interkvartilni raspon godina korisnika: {q1_age:.2f} - {q3_age:.2f} (IQR = {iqr_age:.2f} godina)")
