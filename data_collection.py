import pandas as pd
import numpy as np

# Load existing dataset
file_path = r'C:\Users\User\Downloads\DEPARTMENT OF MECHANICAL ENGINEERING,NITK SURATHKAL (1).csv'

try:
    df = pd.read_csv(file_path)
    print("Original data loaded successfully!")
except FileNotFoundError as e:
    print(f"Error: {e}")
    exit()

# Display basic information about the dataset
print(df.info())

# Function to generate synthetic data
def generate_synthetic_data(df, n_samples=1000):
    synthetic_data = []

    for _ in range(n_samples):
        # Randomly select values based on existing data distributions
        timestamp = pd.Timestamp.now()  # You can modify this to create realistic timestamps
        name = f"Synthetic_{np.random.randint(1000)}"  # Generate a synthetic name
        gender = np.random.choice(df['Gender'].dropna().unique())  # Sample gender
        section = np.random.choice(df['Section'].dropna().unique())  # Sample section
        age = np.random.randint(17, 25)  # Assuming age range from 17 to 25
        
        collision_type = np.random.choice(['Body to Ground', 'Ball to body Impact', 'Head to Body collisions', 'None'])

        collision_types_str = "collision_type"
        
        injuries = np.random.choice(
            ['Knee Injury', 'Head Injury', 'Ligament Tear', 'Dislocation of joint', 'Abrasion', 'Fracture', 'None'], 
            size=np.random.randint(1, 3), replace=False
        )
        injuries_str = '; '.join(injuries)

        symptoms = np.random.choice(
            ['Swelling', 'Pain', 'Bruising', 'Weakness', 'Stiffness', 'Locking or catching sensation', 'None'], 
            size=np.random.randint(1, 4), replace=False
        )
        symptoms_str = '; '.join(symptoms)

        knee_injury_overtime = np.random.choice(['Yes', 'No'])
        knee_injury_instant = np.random.choice(['Yes', 'No'])
        
        report_injury = np.random.choice(['Yes', 'No'])
        removed_from_play = np.random.choice(['Yes', 'No'])
        
        rules_awareness = np.random.choice(['Yes', 'No'])
        received_training = np.random.choice(['Yes', 'No'])
        
        treatment_methods = np.random.choice(
            ['First Aid', 'Medical Intervention', 'Surgery', 'None'], 
            size=np.random.randint(1, 2), replace=False
        )
        treatment_methods_str = '; '.join(treatment_methods)

        protective_gear = np.random.choice(
            ['Knee support', 'Ankle braces', 'Shin guards', 'None'], 
            size=np.random.randint(1, 2), replace=False
        )
        protective_gear_str = '; '.join(protective_gear)

        surgery_done = np.random.choice(['Yes', 'No'])
        
        recovery_time_options = ['Less than a month', '1-3 months', 'Over 3 months']
        recovery_time = np.random.choice(recovery_time_options)
        
        surgery_effect_on_play = np.random.choice(['Yes', 'No'])

        synthetic_data.append([
            timestamp, name, gender, section, age,
            collision_types_str, injuries_str,
            symptoms_str, knee_injury_overtime,
            knee_injury_instant, report_injury,
            removed_from_play, rules_awareness,
            received_training, treatment_methods_str,
            protective_gear_str, surgery_done,
            recovery_time, surgery_effect_on_play
        ])
    
    # Create a DataFrame from synthetic data
    columns = [
        "Timestamp", "Name", "Gender", "Section", "Age",
        "Have you experienced these collision during any sports activity?",
        "What kind of injuries have you experienced during game?",
        "Symptoms experienced by player after injury?",
        "Did you experience knee injury overtime?",
        "Did you experience knee injury at one instant of the game?",
        "Did you report your injury to a coach, athletic trainer or medical professional?",
        "Were you immediately removed from play after a knee injury?",
        "Are you aware of the rules and regulations specific to injury prevention in your sport?",
        "Have you received training in injury prevention techniques and strategies?",
        "How are knee injuries typically treated in your sports?",
        "Protective gear used by you when participating in game?",
        "Did you undergo surgery after injury?",
        "How long did it take to recover?",
        "Did the surgery affect your ability to play?"
    ]
    
    synthetic_df = pd.DataFrame(synthetic_data, columns=columns)
    return synthetic_df

# Generate synthetic data
synthetic_df = generate_synthetic_data(df)

# Combine original and synthetic datasets if needed
combined_df = pd.concat([df, synthetic_df], ignore_index=True)

# Save the combined dataset to an Excel file (ensure no permission issues)
output_file_path = r'C:\Users\User\Documents\synthetic_dataset.xlsx'  # Change path if needed

try:
    combined_df.to_excel(output_file_path, index=False)
    print(f"Combined dataset saved successfully to {output_file_path}")
except PermissionError as e:
    print(f"Permission Error: {e}. Please ensure the file is not open elsewhere.")