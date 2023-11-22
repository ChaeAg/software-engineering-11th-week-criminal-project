import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 읽기
data = pd.read_csv('project_criminal.csv')

# age_cat에 따른 재범률 계산
recid_by_age = data.groupby('age_cat')['is_recid'].mean()

# 원하는 순서로 x축 레이블 재배열
new_order = ['Less than 25', '25 - 45', 'Greater than 45']
recid_by_age = recid_by_age.reindex(new_order)

# 그래프 그리기
plt.figure(figsize=(10, 6))
recid_by_age.plot(kind='bar', color='skyblue')
plt.title('Age Category vs Recidivism Rate')
plt.xlabel('Age Category')
plt.ylabel('Recidivism Rate')
plt.xticks(rotation=0)  # x축 레이블 회전 각도 설정
plt.show()