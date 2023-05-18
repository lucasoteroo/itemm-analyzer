import sqlite3
import csv
import pandas as pd



# Conectar ao banco de dados SQLite Studio
conn = sqlite3.connect('pet.db')
cursor = conn.cursor()


# Criar a tabela para armazenar os dados CSV

cursor.execute('''CREATE TABLE IF NOT EXISTS peukert_dados (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  "Time Stamp" DATETIME,
  "Step" INTEGER,
  "Status" TEXT,
  "ProgTime" FLOAT,
  "StepTime" FLOAT,
  Cycle INTEGER,
  "CycleLevel" FLOAT,
  Procedure_2 TEXT,
  Voltage FLOAT,
  Current FLOAT,
  AhCha FLOAT,
  AhDch FLOAT,
  AhStep FLOAT,
  AhAccu FLOAT,
  WhAccu FLOAT,
  WhCha FLOAT,
  WhDch FLOAT,
  WhStep FLOAT,
  Channel0270101 FLOAT,
  Channel0280101 FLOAT
)''')

# Ler o arquivo CSV e inserir os dados na tabela
with open('Peukert.csv', 'r') as csvfile:
    leitor_csv = csv.reader(csvfile, delimiter=';')
    
    next(leitor_csv)
    for linha in leitor_csv:
        linha1= linha[0]
        linha2= linha[1] 
        linha3= linha[2]
        linha4= linha[3] 
        linha5= linha[4]
        linha6= linha[5]
        linha7= linha[6]
        linha8= linha[7]
        linha9= linha[8]
        linha10= linha[9]
        linha11= linha[10]
        linha12= linha[11]
        linha13= linha[12]
        linha14= linha[13]
        linha15= linha[14]
        linha16= linha[15]
        linha17= linha[16]
        linha18= linha[17]
        linha19= linha[18]
        linha20= linha[19]
        

        cursor.execute('''INSERT INTO peukert_dados ("Time Stamp", "Step", "Status", "ProgTime", "StepTime",
                Cycle, "CycleLevel", Procedure_2, Voltage, Current, AhCha, AhDch, AhStep,
                AhAccu, WhAccu, WhCha, WhDch, WhStep, Channel0270101, Channel0280101)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                (linha1, linha2, linha3, linha4, linha5, linha6, linha7, linha8,
                 linha9, linha10, linha11, linha12, linha13, linha14, linha15, linha16,
                 linha17, linha18, linha19, linha20))




query= "SELECT * FROM peukert_dados"
dados=pd.read_sql_query(query,conn)


#coluna_especifica = 'Step'
#print(dados['Step'])

'''
ultimas_linhas_por_id = dados.groupby('2').apply(lambda x: x.iloc[-1])

ultimas_linhas_da_coluna_especifica = ultimas_linhas_por_id[coluna_especifica]

print(ultimas_linhas_por_id)
'''
conn.commit()
conn.close()
