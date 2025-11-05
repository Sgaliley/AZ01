import pandas as pd


print("=== Анализ random_stock_market_dataset.csv ===")
stock_df = pd.read_csv('random_stock_market_dataset.csv')

print("Первые 5 строк:")
print(stock_df.head())

print("\nИнформация о данных:")
stock_df.info()

print("\nСтатистическое описание:")
print(stock_df.describe())

print("\n\n=== Анализ dz.csv: средняя зарплата по городам ===")
salary_df = pd.read_csv('dz.csv')
avg_salary_by_city = salary_df.groupby('City')['Salary'].mean()

print("Средняя зарплата по городам:")
print(avg_salary_by_city)