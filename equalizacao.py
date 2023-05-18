import sqlite3
import csv

# Conectar ao banco de dados SQLite Studio
conn = sqlite3.connect('pet.db')
cursor = conn.cursor()

# Criar a tabela para armazenar os dados CSV
cursor.execute('''CREATE TABLE IF NOT EXISTS dados (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  MeasurementID TEXT,
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
  Channel0280101 FLOAT,
  "x1" DATETIME,
  x2 TEXT,
  x3 FLOAT,
  "Peukert1_75V" FLOAT,
  x4 FLOAT
)''')

# Ler o arquivo CSV e inserir os dados na tabela
with open('EQUALIZACAO_4X_C20.csv', 'r') as csvfile:
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
        linha21= linha[20]
        linha22= linha[21]
        linha23= linha[22]
        linha24= linha[23]
        linha25= linha[24]
        linha26= linha[25]
        
        cursor.execute('''INSERT INTO dados ("MeasurementID","Time Stamp", "Step", "Status", "ProgTime", "StepTime",
                Cycle, "CycleLevel", Procedure_2, Voltage, Current, AhCha, AhDch, AhStep,
                AhAccu, WhAccu, WhCha, WhDch, WhStep, Channel0270101, Channel0280101,"x1", x2, x3, "Peukert1_75V",x4)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?,?,?,?)''',
                (linha1, linha2, linha3, linha4, linha5, linha6, linha7, linha8,
                 linha9, linha10, linha11, linha12, linha13, linha14, linha15, linha16,
                 linha17, linha18, linha19, linha20, linha21,linha22,linha23,linha24,linha25,linha26))
conn.commit()
conn.close()