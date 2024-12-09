import pandas as pd
import matplotlib.pyplot as plt

# Load the synthetic dataset (make sure to specify the correct path)
df = pd.read_excel(r'C:\Users\User\Desktop\capstone\DEPARTMENT OF MECHANICAL ENGINEERING,NITK SURATHKAL (Responses).xlsx')

# Function to plot a pie chart for a question
def plot_pie_chart(column, title):
    # Count the occurrences of each unique response
    response_counts = df[column].value_counts()

    # Plot the pie chart
    plt.figure(figsize=(8, 6))
    plt.pie(response_counts, labels=response_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title(title)
    plt.show()

# Plot pie charts for the first 5 questions
plot_pie_chart("Have you experienced these collision during any sports activity?", "Collisions Experienced During Sports Activity")
#plot_pie_chart("What kind of injuries have you experienced during game?", "Types of Injuries Experienced During Game")

#plot_pie_chart("Symptoms experienced by player after injury?", "Symptoms Experienced After Injury")
#plot_pie_chart("Did you experience knee injury overtime?", "Knee Injury Experienced Over Time")
#plot_pie_chart("Did you experience knee injury at one instant of the game?", "Instantaneous Knee Injury During Game")
