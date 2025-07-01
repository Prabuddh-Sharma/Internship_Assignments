import matplotlib.pyplot as plt
import numpy as np

sem1_subjects = ['Engg. Math I', 'Programming in C', 'Engg. Physics', 'Basic Electrical Engg.']
sem1_scores = np.array([75, 80, 68, 72])

sem2_subjects = ['Engg. Math II', 'Data Structures', 'Environmental Sci.', 'Engg. Graphics']
sem2_scores = np.array([70, 85, 78, 65])

print("Semester 1 vs Semester 2 comparison graph.")

bar_width = 0.35

index = np.arange(len(sem1_subjects))

plt.bar(index - bar_width/2, sem1_scores, bar_width, label='Semester 1', color='skyblue')

plt.bar(index + bar_width/2, sem2_scores, bar_width, label='Semester 2', color='lightcoral')

plt.title('Semester 1 vs Semester 2 Results Comparison')

plt.xlabel('Subjects')

plt.ylabel('Scores (out of 100)')

plt.xticks(index, sem1_subjects, rotation=20, ha='right')

plt.legend()

plt.show()

print("\nResults comparison graph generated successfully!")