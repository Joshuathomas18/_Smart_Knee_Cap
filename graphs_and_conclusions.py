import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
df = pd.read_excel('C:/Users/User/Desktop/capstone/synthetic_dataset.xlsx')
#COllisions during sports activity frequency
'''collision_counts = df['Have you experienced these collision during any sports activity?'].str.get_dummies(sep='; ').sum()
collision_counts.plot(kind='bar', color='skyblue')
plt.title('Collision Types Experienced')
plt.xlabel('Collision Type')
plt.ylabel('Frequency')
plt.show()'''
#Types of injuries experienced
'''injury_counts = df['What kind of injuries have you experienced during game?'].str.get_dummies(sep='; ').sum()
injury_counts.plot(kind='bar', color='salmon')
plt.title('Types of Injuries Experienced')
plt.xlabel('Injury Type')
plt.ylabel('Frequency')
plt.show()'''
# symptoms ecperienced post injury
'''symptom_counts = df['Symptoms experienced by player after injury?'].str.get_dummies(sep='; ').sum()
symptom_counts.plot(kind='bar', color='lightgreen')
plt.title('Symptoms Experienced Post-Injury')
plt.xlabel('Symptom')
plt.ylabel('Frequency')
plt.show()'''


# Knee injury over time
'''overtime_counts = df['Did you experience knee injury overtime?'].value_counts()
overtime_counts.plot(kind='pie', autopct='%1.1f%%', labels=['Yes', 'No'], colors=['#ff9999','#66b3ff'])
plt.title('Knee Injury Over Time')
plt.ylabel('')
plt.show()

# Knee injury instantaneously
instant_counts = df['Did you experience knee injury at one instant of the game?'].value_counts()
instant_counts.plot(kind='pie', autopct='%1.1f%%', labels=['Yes', 'No'], colors=['#ffcc99','#99ff99'])
plt.title('Knee Injury Instantaneously')
plt.ylabel('')
plt.show()'''

'''gear_counts = df['Protective gear used by you when participating in game?'].str.get_dummies(sep='; ').sum()
gear_counts.plot(kind='bar', color='orange')
plt.title('Protective Gear Used')
plt.xlabel('Protective Gear')
plt.ylabel('Frequency')
plt.show()'''

surgery_effect_counts = df['Did the surgery affect your ability to play?'].value_counts()
surgery_effect_counts.plot(kind='pie', autopct='%1.1f%%', labels=['Yes', 'No'], colors=['#ffb3e6','#c2c2f0'])
plt.title('Effect of Surgery on Playing Ability')
plt.ylabel('')
plt.show()


