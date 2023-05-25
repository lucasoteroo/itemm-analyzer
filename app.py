import os
from datetime import datetime, timedelta
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

from flask import Flask, render_template
from flask_security import (
        Security,
        current_user,
        auth_required,
        hash_password,
        SQLAlchemySessionUserDatastore,
    )
from database import db_session, init_db
from models.auth import User, Role

 # Create app
app = Flask(__name__)
app.config["DEBUG"] = True

    # Generate a nice key using secrets.token_urlsafe()
app.config["SECRET_KEY"] = os.environ.get(
        "SECRET_KEY", "pf9Wkove4IKEAXvy-cQkeDPhv9Cb3Ag-wyJILbq_dFw"
    )
    # Bcrypt is set as default SECURITY_PASSWORD_HASH, which requires a salt
    # Generate a good salt using: secrets.SystemRandom().getrandbits(128)
app.config["SECURITY_PASSWORD_SALT"] = os.environ.get(
        "SECURITY_PASSWORD_SALT", "146585145368132386173505678016728509634"
    )

    # Setup Flask-Security
user_datastore = SQLAlchemySessionUserDatastore(db_session, User, Role)
app.security = Security(app, user_datastore)


    # Views
@app.route("/dac")
@auth_required()
def dac():
        return render_template("dac.html")


@app.route("/polarizacao")
@auth_required()
def polarizacao():
        return render_template("polarizacao.html")


@app.route("/pekeurt")
@auth_required()
def pekeurt():
    
    #------------------AM01--------------------

    #conecta ao banco de dados SQLite
    conn = sqlite3.connect('pet.db')

     # Carrega a tabela do banco de dados em um DataFrame do pandas
    consultaequalizacaoAm01 = pd.read_sql_query('SELECT * FROM equalizacaoAm01', conn)

     # Filtra as linhas que contém o valor desejado, remove as linhas com valores nulos e em que a coluna 'Current' é igual a zero, e remove valores duplicados na coluna 'Current'
    linha_especificaequalizacaoAm01 = consultaequalizacaoAm01.loc[(consultaequalizacaoAm01['Voltage'] == '1,750') & (consultaequalizacaoAm01['Current'] != 0)].dropna().drop_duplicates(subset=['Current'])[['StepTime', 'Current']]
    linha_especificaequalizacaoAm01['Current'] = linha_especificaequalizacaoAm01['Current'].apply(lambda x: abs(float(x.replace(',', '.'))))

     # Converte o formato de hora para número de horas com precisão de 3 casas decimais
    linha_especificaequalizacaoAm01['StepTime'] = pd.to_timedelta(linha_especificaequalizacaoAm01['StepTime']).apply(lambda x: x.total_seconds() / 3600).round(3)


     # Carrega a tabela do banco de dados em um DataFrame do pandas
    consultapeukertAm01 = pd.read_sql_query('SELECT * FROM peukertAm01', conn)

     # Filtra as linhas que contém o valor desejado, remove as linhas com valores nulos e em que a coluna 'Current' é igual a zero, e remove valores duplicados na coluna 'Current'

    linha_especificapeukertAm01 = consultapeukertAm01.loc[(consultapeukertAm01['Voltage'] == '1,75') & (consultapeukertAm01['Current'] != 0)].dropna().drop_duplicates(subset=['Current'])[['StepTime', 'Current']]
    linha_especificapeukertAm01['Current'] = linha_especificapeukertAm01['Current'].apply(lambda x: abs(float(x.replace(',', '.'))))

     # Converte o formato de hora para número de horas com precisão de 3 casas decimais
    linha_especificapeukertAm01['StepTime'] = pd.to_timedelta(linha_especificapeukertAm01['StepTime']).apply(lambda x: x.total_seconds() / 3600).round(3)


    am01_CBI22076 = pd.concat([linha_especificaequalizacaoAm01, linha_especificapeukertAm01])
    print(am01_CBI22076)


    print("-----------------------------AM02----------------------------")

     # Carrega a tabela do banco de dados em um DataFrame do pandas
    consultaequalizacaoAm02 = pd.read_sql_query('SELECT * FROM equalizacaoAm02', conn)

     # Filtra as linhas que contém o valor desejado, remove as linhas com valores nulos e em que a coluna 'Current' é igual a zero, e remove valores duplicados na coluna 'Current'
    linha_especificaequalizacaoAm02 = consultaequalizacaoAm02.loc[(consultaequalizacaoAm02['Voltage'] == '1,750') & (consultaequalizacaoAm02['Current'] != 0)].dropna().drop_duplicates(subset=['Current'])[['StepTime', 'Current']]
    linha_especificaequalizacaoAm02['Current'] = linha_especificaequalizacaoAm02['Current'].apply(lambda x: abs(float(x.replace(',', '.'))))

     # Converte o formato de hora para número de horas com precisão de 3 casas decimais
    linha_especificaequalizacaoAm02['StepTime'] = pd.to_timedelta(linha_especificaequalizacaoAm02['StepTime']).apply(lambda x: x.total_seconds() / 3600).round(3)

     # Carrega a tabela do banco de dados em um DataFrame do pandas
    consultapeukertAm02 = pd.read_sql_query('SELECT * FROM peukertAm02', conn)

     # Filtra as linhas que contém o valor desejado, remove as linhas com valores nulos e em que a coluna 'Current' é igual a zero, e remove valores duplicados na coluna 'Current'
    linha_especificapeukertAm02 = consultapeukertAm02.loc[(consultapeukertAm02['Voltage'] == '1,75') & (consultapeukertAm02['Current'] != 0) & (consultapeukertAm02['Current'] != '0,000')].dropna().drop_duplicates(subset=['Current'])[['StepTime', 'Current']]
    linha_especificapeukertAm02['Current'] = linha_especificapeukertAm02['Current'].apply(lambda x: abs(float(x.replace(',', '.'))))

     # Converte o formato de hora para número de horas com precisão de 3 casas decimais
    linha_especificapeukertAm02['StepTime'] = pd.to_timedelta(linha_especificapeukertAm02['StepTime']).apply(lambda x: x.total_seconds() / 3600).round(3)

    am02_CBI22076 = pd.concat([linha_especificaequalizacaoAm02, linha_especificapeukertAm02])
    print(am02_CBI22076)


    print("---------------AM05--------------------")

    # Carrega a tabela do banco de dados em um DataFrame do pandas
    consultaequalizacaoAm05 = pd.read_sql_query('SELECT * FROM equalizacaoAm05', conn)

     # Filtra as linhas que contém o valor desejado, remove as linhas com valores nulos e em que a coluna 'Current' é igual a zero, e remove valores duplicados na coluna 'Current'
    linha_especificaequalizacaoAm05 = consultaequalizacaoAm05.loc[(consultaequalizacaoAm05['Voltage'] == '1,750') & (consultaequalizacaoAm05['Current'] != 0)].dropna().drop_duplicates(subset=['Current'])[['StepTime', 'Current']]
    linha_especificaequalizacaoAm05['Current'] = linha_especificaequalizacaoAm05['Current'].apply(lambda x: abs(float(x.replace(',', '.'))))

     # Converte o formato de hora para número de horas com precisão de 3 casas decimais
    linha_especificaequalizacaoAm05['StepTime'] = pd.to_timedelta(linha_especificaequalizacaoAm05['StepTime']).apply(lambda x: x.total_seconds() / 3600).round(3)

     # Carrega a tabela do banco de dados em um DataFrame do pandas
    consultapeukertAm05 = pd.read_sql_query('SELECT * FROM peukertAm05', conn)

     # Filtra as linhas que contém o valor desejado, remove as linhas com valores nulos e em que a coluna 'Current' é igual a zero, e remove valores duplicados na coluna 'Current'
    linha_especificapeukertAm05 = consultapeukertAm05.loc[(consultapeukertAm05['Voltage'] == '1,75') & (consultapeukertAm05['Current'] != 0) & (consultapeukertAm05['Current'] != '0,000')].dropna().drop_duplicates(subset=['Current'])[['StepTime', 'Current']]
    linha_especificapeukertAm05['Current'] = linha_especificapeukertAm05['Current'].apply(lambda x: abs(float(x.replace(',', '.'))))

     # Converte o formato de hora para número de horas com precisão de 3 casas decimais
    linha_especificapeukertAm05['StepTime'] = pd.to_timedelta(linha_especificapeukertAm05['StepTime']).apply(lambda x: x.total_seconds() / 3600).round(3)

    am05_CBI22077 = pd.concat([linha_especificaequalizacaoAm05, linha_especificapeukertAm05])
    print(am05_CBI22077)


    print("---------------AM06--------------------")

    # Carrega a tabela do banco de dados em um DataFrame do pandas
    consultaequalizacaoAm06 = pd.read_sql_query('SELECT * FROM equalizacaoAm06', conn)

     # Filtra as linhas que contém o valor desejado, remove as linhas com valores nulos e em que a coluna 'Current' é igual a zero, e remove valores duplicados na coluna 'Current'
    linha_especificaequalizacaoAm06 = consultaequalizacaoAm06.loc[(consultaequalizacaoAm06['Voltage'] == '1,750') & (consultaequalizacaoAm06['Current'] != 0)].dropna().drop_duplicates(subset=['Current'])[['StepTime', 'Current']]
    linha_especificaequalizacaoAm06['Current'] = linha_especificaequalizacaoAm06['Current'].apply(lambda x: abs(float(x.replace(',', '.'))))

     # Converte o formato de hora para número de horas com precisão de 3 casas decimais
    linha_especificaequalizacaoAm06['StepTime'] = pd.to_timedelta(linha_especificaequalizacaoAm06['StepTime']).apply(lambda x: x.total_seconds() / 3600).round(3)


     # Carrega a tabela do banco de dados em um DataFrame do pandas
    consultapeukertAm06 = pd.read_sql_query('SELECT * FROM peukertAm06', conn)

     # Filtra as linhas que contém o valor desejado, remove as linhas com valores nulos e em que a coluna 'Current' é igual a zero, e remove valores duplicados na coluna 'Current'
    linha_especificapeukertAm06 = consultapeukertAm06.loc[(consultapeukertAm06['Voltage'] == '1,75') & (consultapeukertAm06['Current'] != 0) & (consultapeukertAm06['Current'] != '0,000')].dropna().drop_duplicates(subset=['Current'])[['StepTime', 'Current']]
    linha_especificapeukertAm06['Current'] = linha_especificapeukertAm06['Current'].apply(lambda x: abs(float(x.replace(',', '.'))))

     # Converte o formato de hora para número de horas com precisão de 3 casas decimais
    linha_especificapeukertAm06['StepTime'] = pd.to_timedelta(linha_especificapeukertAm06['StepTime']).apply(lambda x: x.total_seconds() / 3600).round(3)

    am06_CBI22077 = pd.concat([linha_especificaequalizacaoAm06, linha_especificapeukertAm06])
    print(am06_CBI22077)


    #----------GRÁFICOS DO AM01 E AM02-------------------

    # Plotar gráfico para linha_especificaequalizacaoAm01
    plt.scatter(range(len(am01_CBI22076)), am01_CBI22076['Current'], label='am01_CBI22076', marker='o',zorder=2, alpha=1)

    # Plotar gráfico para linha_especificapeukertAm01
    plt.scatter(list(range(len(am01_CBI22076), len(am01_CBI22076)+len(am02_CBI22076))), am02_CBI22076['Current'], label='am02_CBI22076', marker='o', zorder=2, alpha=0.5)


    # Configurar rótulos e título do gráfico
    plt.xlabel('StepTime')
    plt.ylabel('Current')
    plt.title('Gráfico de StepTime vs Current')

    # Configurar intervalo dos eixos x e y
    plt.ylim(0, 10)  # Define o intervalo do eixo y de 0 a 10

    #plt.xticks(am01_CBI22076['StepTime'])

    plt.legend('GRÁFICO DO AM01 E AM02')

    # Exibir o gráfico
    plt.show()

    #----------GRÁFICOS DO AM05 E AM06-------------------


    # Plotar gráfico para linha_especificaequalizacaoAm01
    plt.scatter(range(len(am05_CBI22077)), am05_CBI22077['Current'], label='am05_CBI22077', marker='o',zorder=2, alpha=1)

    # Plotar gráfico para linha_especificapeukertAm01
    plt.scatter(list(range(len(am05_CBI22077), len(am05_CBI22077)+len(am06_CBI22077))), am06_CBI22077['Current'], label='am06_CBI22077', marker='o', zorder=2, alpha=0.5)


    # Configurar rótulos e título do gráfico
    plt.xlabel('StepTime')
    plt.ylabel('Current')
    plt.title('Gráfico de StepTime vs Current')

    # Configurar intervalo dos eixos x e y
    plt.ylim(0, 10)  # Define o intervalo do eixo y de 0 a 10

    #plt.xticks(am01_CBI22076['StepTime'])

    plt.legend()

    # Exibir o gráfico
    plt.show()

    conn.close()
    
    return render_template("pekeurt.html", consulta1=am01_CBI22076, 
                                consulta2=am02_CBI22076, consulta3=am05_CBI22077,
                                  consulta4=am06_CBI22077)



@app.route("/consumo")
@auth_required()
def consumo():
    return render_template("consumo.html")


@app.route("/")
@app.route("/home")
@auth_required()
def home():
    return render_template("index.html", name=current_user.email)
    # return render_template_string("Hello {{email}} !", email=current_user.email)


# one time setup
with app.app_context():
    # Create a user to test with
    init_db()
    if not app.security.datastore.find_user(email="test@me.com"):
        app.security.datastore.create_user(
            email="test@me.com", password=hash_password("password")
        )
    db_session.commit()
    db_session.close()

if __name__ == "__main__":
    # run application (can also use flask run)
    app.run()


@app.cli.command("create-user")
def create_user():
    """Criar um usuario."""
    email = input("Coloque o seu email: ")
    password = hash_password(input("Coloque o password: "))
    confirm_password = hash_password(input("Coloque o password novamente: "))
    if password != confirm_password:
        print("Passwords diferentes")
        return 1
    try:
        app.security.datastore.create_user(email=email, password=password)
        db_session.commit()
        print(f"Usuario com email {email} criado com sucesso!")
    except Exception as e:
        print("Nao foi possivel criar o usuario.")
        print(e)
