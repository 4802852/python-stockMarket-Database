import pandas as pd
import requests

code = '005930' # 회사코드
URL = "https://finance.naver.com/item/main.nhn?code=" + code

company = requests.get(URL)
html = company.text

df = pd.read_html(company.text)[3]

df.set_index(('주요재무정보', '주요재무정보', '주요재무정보'), inplace=True)
df.index.rename('주요재무정보', inplace=True)
df.columns = df.columns.droplevel(2)
annual_finance = pd.DataFrame(df).xs('최근 연간 실적', axis=1) 
quarter_finance = pd.DataFrame(df).xs('최근 분기 실적', axis=1)

print(annual_finance)
print(quarter_finance)