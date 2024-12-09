
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'path_to_modified_synthetic_dataset.xlsx'
data = pd.read_excel(file_path)


plt.figure(figsize=(6, 6))
data['Training Received'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'))
plt.title('Training Received')
plt.ylabel('')
plt.show()




