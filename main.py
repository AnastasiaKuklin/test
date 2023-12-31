
import pandas as pd
df = pd.read_excel('lab_pi_101.xlsx')
kol_grades = df['Оценка'].notna().sum()
kol_grades_pi101 = ((df['Группа']=='ПИ101') & (df['Оценка'].notna())).sum()
kol_stud = len(df[(df['Группа']=='ПИ101') & (df['Оценка'].notna())].drop_duplicates(subset=['Личный номер студента']))
id_stud = ((df[(df['Группа']=='ПИ101') & (df['Оценка'].notna())].drop_duplicates(subset=['Личный номер студента']))['Личный номер студента']).tolist()
form_contr = ((df[(df['Группа']=='ПИ101') & (df['Оценка'].notna())].drop_duplicates(subset=['Уровень контроля']))['Уровень контроля']).tolist()
years = ((df[(df['Группа']=='ПИ101') & (df['Оценка'].notna())].drop_duplicates(subset=['Год']))['Год']).tolist()
print("В исходном датасете содержалось", kol_grades, "оценок, из них", kol_grades_pi101, "оценок относятся к группе ПИ101. В датасете находятся оценки", kol_stud, "студентов со следующими личными номерами по ПИ101:", id_stud, "Используемые формы контроля:", form_contr, "Данные представлены по следующим учебным годам:", years)
