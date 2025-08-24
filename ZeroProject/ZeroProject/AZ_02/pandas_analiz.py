import pandas as pd
import numpy as np

data = {
    'Ученик': [f'Ученик_{i+1}' for i in range(10)],
    'Математика': np.random.randint(2, 6, 10),
    'Физика': np.random.randint(3, 6, 10),
    'Химия': np.random.randint(2, 5, 10),
    'Литература': np.random.randint(3, 6, 10),
    'История': np.random.randint(4, 6, 10)
}

df = pd.DataFrame(data)

print("Первые 5 строк DataFrame:")
print(df.head())

print("Средние оценки по предметам:")
mean_grades = df.mean(numeric_only=True)
print(mean_grades)


print("Медианные оценки по предметам:")
median_grades = df.median(numeric_only=True)
print(median_grades)


print("Квантили для оценок по математике:")
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR_math = Q3_math - Q1_math

print(f"Q1 (25-й перцентиль) по математике: {Q1_math}")
print(f"Q3 (75-й перцентиль) по математике: {Q3_math}")
print(f"IQR по математике: {IQR_math}")


print("Стандартное отклонение по предметам:")
std_grades = df.std(numeric_only=True)
print(std_grades)
