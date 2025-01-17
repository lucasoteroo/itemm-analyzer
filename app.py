import os
from datetime import datetime, timedelta
import pandas as pd
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
    
    #------------------- AM01--------------------"

        #EQUALIZAÇÃO

        # Carrega os dados do arquivo CSV para o DataFrame do pandas
    consultaequalizacaoAm01 = pd.read_csv("/workspaces/itemm-analyzer/csv's/equalizacaoAm01.csv", delimiter=';', on_bad_lines='skip', low_memory=False)
        # Substitui vírgula por ponto
    consultaequalizacaoAm01['Voltage'] = consultaequalizacaoAm01['Voltage'].str.replace(',', '.')
    consultaequalizacaoAm01['Current'] = consultaequalizacaoAm01['Current'].str.replace(',', '.')
        # Converte a coluna 'Voltage' para float, pulando os valores de string
    consultaequalizacaoAm01['Voltage'] = pd.to_numeric(consultaequalizacaoAm01['Voltage'], errors='coerce')
    consultaequalizacaoAm01['Current'] = pd.to_numeric(consultaequalizacaoAm01['Current'], errors='coerce').abs()

        # Arredonda a coluna 'Voltage' para duas casas decimais
    consultaequalizacaoAm01['Voltage'] = consultaequalizacaoAm01['Voltage'].round(3)

        # Filtra as linhas que contém o valor desejado, remove as linhas com valores nulos e em que a coluna 'Current' é igual a zero
    linha_especificaequalizacaoAm01 = consultaequalizacaoAm01.loc[(consultaequalizacaoAm01['Voltage'] == 1.750) & (consultaequalizacaoAm01['Step Time'] != 0.000000) & (consultaequalizacaoAm01['Current'] != 0.000)].drop_duplicates(subset=['Current'])

        # Converte o formato de 'Step Time' para horas
    linha_especificaequalizacaoAm01['Step Time'] = pd.to_timedelta(linha_especificaequalizacaoAm01['Step Time'])
    linha_especificaequalizacaoAm01['Step Time'] = linha_especificaequalizacaoAm01['Step Time'].dt.total_seconds() / 3600

    linha_especificaequalizacaoAm01=(linha_especificaequalizacaoAm01[['Step Time', 'Current']])

        #PEUKERT

    consultapeukertAm01 = pd.read_csv("/workspaces/itemm-analyzer/csv's/peukertAm01.csv", delimiter=';', on_bad_lines='skip', low_memory=False)
        # Substitui vírgula por ponto
    consultapeukertAm01['Voltage'] = consultapeukertAm01['Voltage'].str.replace(',', '.')
    consultapeukertAm01['Current'] = consultapeukertAm01['Current'].str.replace(',', '.')
        # Converte a coluna 'Voltage' para float, pulando os valores de string
    consultapeukertAm01['Voltage'] = pd.to_numeric(consultapeukertAm01['Voltage'], errors='coerce')
    consultapeukertAm01['Current'] = pd.to_numeric(consultapeukertAm01['Current'], errors='coerce').abs()

        # Arredonda a coluna 'Voltage' para duas casas decimais
    consultapeukertAm01['Voltage'] = consultapeukertAm01['Voltage'].round(3)

        # Filtra as linhas que contém o valor desejado, remove as linhas com valores nulos e em que a coluna 'Current' é igual a zero
    linha_especificapeukertAm01 = consultapeukertAm01.loc[(consultapeukertAm01['Voltage'] == 1.750) & (consultapeukertAm01['Step Time'] != 0.000000) & (consultapeukertAm01['Current'] != 0.000)].drop_duplicates(subset=['Current'])

        # Converte o formato de 'Step Time' para horas
    linha_especificapeukertAm01['Step Time'] = pd.to_timedelta(linha_especificapeukertAm01['Step Time'])
    linha_especificapeukertAm01['Step Time'] = linha_especificapeukertAm01['Step Time'].dt.total_seconds() / 3600

    linha_especificapeukertAm01=(linha_especificapeukertAm01[['Step Time', 'Current']])


    am01_CBI22076 = pd.concat([linha_especificaequalizacaoAm01, linha_especificapeukertAm01])
    am01_CBI22076['Step Time'] = am01_CBI22076['Step Time'].round(3)
    am01_CBI22076['Current'] = am01_CBI22076['Current'].round(3)
    

    #-----------------------------AM02----------------------------

        #EQUALIZAÇÃO

        # Carrega os dados do arquivo CSV para o DataFrame do pandas
    consultaequalizacaoAm02 = pd.read_csv("/workspaces/itemm-analyzer/csv's/equalizacaoAm02.csv", delimiter=';', on_bad_lines='skip', low_memory=False)
        # Substitui vírgula por ponto
    consultaequalizacaoAm02['Voltage'] = consultaequalizacaoAm02['Voltage'].str.replace(',', '.')
    consultaequalizacaoAm02['Current'] = consultaequalizacaoAm02['Current'].str.replace(',', '.')
        # Converte a coluna 'Voltage' para float, pulando os valores de string
    consultaequalizacaoAm02['Voltage'] = pd.to_numeric(consultaequalizacaoAm02['Voltage'], errors='coerce')
    consultaequalizacaoAm02['Current'] = pd.to_numeric(consultaequalizacaoAm02['Current'], errors='coerce').abs()
        # Arredonda a coluna 'Voltage' para duas casas decimais
    consultaequalizacaoAm02['Voltage'] = consultaequalizacaoAm02['Voltage'].round(3)

        # Filtra as linhas que contém o valor desejado, remove as linhas com valores nulos e em que a coluna 'Current' é igual a zero
    linha_especificaequalizacaoAm02 = consultaequalizacaoAm02.loc[(consultaequalizacaoAm02['Voltage'] == 1.750) & (consultaequalizacaoAm02['Step Time'] != 0.000000) & (consultaequalizacaoAm02['Current'] != 0.000)].drop_duplicates(subset=['Current'])

        # Converte o formato de 'Step Time' para horas
    linha_especificaequalizacaoAm02['Step Time'] = pd.to_timedelta(linha_especificaequalizacaoAm02['Step Time'])
    linha_especificaequalizacaoAm02['Step Time'] = linha_especificaequalizacaoAm02['Step Time'].dt.total_seconds() / 3600

    linha_especificaequalizacaoAm02=(linha_especificaequalizacaoAm02[['Step Time', 'Current']])

        #PEUKERT

    consultapeukertAm02 = pd.read_csv("/workspaces/itemm-analyzer/csv's/peukertAm02.csv", delimiter=';', on_bad_lines='skip', low_memory=False)
        # Substitui vírgula por ponto
    consultapeukertAm02['Voltage'] = consultapeukertAm02['Voltage'].str.replace(',', '.')
    consultapeukertAm02['Current'] = consultapeukertAm02['Current'].str.replace(',', '.')
        # Converte a coluna 'Voltage' para float, pulando os valores de string
    consultapeukertAm02['Voltage'] = pd.to_numeric(consultapeukertAm02['Voltage'], errors='coerce')
    consultapeukertAm02['Current'] = pd.to_numeric(consultapeukertAm02['Current'], errors='coerce').abs()
        # Arredonda a coluna 'Voltage' para duas casas decimais
    consultapeukertAm02['Voltage'] = consultapeukertAm02['Voltage'].round(3)

        # Filtra as linhas que contém o valor desejado, remove as linhas com valores nulos e em que a coluna 'Current' é igual a zero
    linha_especificapeukertAm02 = consultapeukertAm02.loc[(consultapeukertAm02['Voltage'] == 1.750) & (consultapeukertAm02['Step Time'] != 0.000000) & (consultapeukertAm02['Current'] != 0.000)].drop_duplicates(subset=['Current'])


        # Filtra as linhas que não são nulas e não possuem o valor '0' na coluna 'Current'
    linha_especificapeukertAm02 = linha_especificapeukertAm02.dropna(subset=['Current'])


        # Converte o formato de 'Step Time' para horas
    linha_especificapeukertAm02['Step Time'] = pd.to_timedelta(linha_especificapeukertAm02['Step Time'])
    linha_especificapeukertAm02['Step Time'] = linha_especificapeukertAm02['Step Time'].dt.total_seconds() / 3600

    linha_especificapeukertAm02=(linha_especificapeukertAm02[['Step Time', 'Current']])

    am02_CBI22076 = pd.concat([linha_especificaequalizacaoAm02, linha_especificapeukertAm02])
    am02_CBI22076['Step Time'] = am02_CBI22076['Step Time'].round(3)
    am02_CBI22076['Current'] = am02_CBI22076['Current'].round(3)
    

    #-----------------------------AM05----------------------------

        #EQUALIZAÇÃO

        # Carrega os dados do arquivo CSV para o DataFrame do pandas
    consultaequalizacaoAm05 = pd.read_csv("/workspaces/itemm-analyzer/csv's/equalizacaoAm05.csv", delimiter=';', on_bad_lines='skip', low_memory=False)
        # Substitui vírgula por ponto
    consultaequalizacaoAm05['Voltage'] = consultaequalizacaoAm05['Voltage'].str.replace(',', '.')
    consultaequalizacaoAm05['Current'] = consultaequalizacaoAm05['Current'].str.replace(',', '.')

        # Converte a coluna 'Voltage' para float, pulando os valores de string
    consultaequalizacaoAm05['Voltage'] = pd.to_numeric(consultaequalizacaoAm05['Voltage'], errors='coerce')
    consultaequalizacaoAm05['Current'] = pd.to_numeric(consultaequalizacaoAm05['Current'], errors='coerce').abs()
        # Arredonda a coluna 'Voltage' para duas casas decimais
    consultaequalizacaoAm05['Voltage'] = consultaequalizacaoAm05['Voltage'].round(3)

        # Filtra as linhas que contém o valor desejado, remove as linhas com valores nulos e em que a coluna 'Current' é igual a zero
    linha_especificaequalizacaoAm05 = consultaequalizacaoAm05.loc[(consultaequalizacaoAm05['Voltage'] == 1.750) & (consultaequalizacaoAm05['Step Time'] != 0.000000) & (consultaequalizacaoAm05['Current'] != 0.000)].drop_duplicates(subset=['Current'])

        # Converte o formato de 'Step Time' para horas
    linha_especificaequalizacaoAm05['Step Time'] = pd.to_timedelta(linha_especificaequalizacaoAm05['Step Time'])
    linha_especificaequalizacaoAm05['Step Time'] = linha_especificaequalizacaoAm05['Step Time'].dt.total_seconds() / 3600

    linha_especificaequalizacaoAm05=(linha_especificaequalizacaoAm05[['Step Time', 'Current']])

        #PEUKERT

    consultapeukertAm05 = pd.read_csv("/workspaces/itemm-analyzer/csv's/peukertAm05.csv", delimiter=';', on_bad_lines='skip', low_memory=False)
        # Substitui vírgula por ponto
    consultapeukertAm05['Voltage'] = consultapeukertAm05['Voltage'].str.replace(',', '.')
    consultapeukertAm05['Current'] = consultapeukertAm05['Current'].str.replace(',', '.')
        # Converte a coluna 'Voltage' para float, pulando os valores de string
    consultapeukertAm05['Voltage'] = pd.to_numeric(consultapeukertAm05['Voltage'], errors='coerce')
    consultapeukertAm05['Current'] = pd.to_numeric(consultapeukertAm05['Current'], errors='coerce').abs()
        # Arredonda a coluna 'Voltage' para duas casas decimais
    consultapeukertAm05['Voltage'] = consultapeukertAm05['Voltage'].round(3)

        # Filtra as linhas que contém o valor desejado, remove as linhas com valores nulos e em que a coluna 'Current' é igual a zero
    linha_especificapeukertAm05 = consultapeukertAm05.loc[(consultapeukertAm05['Voltage'] == 1.750) & (consultapeukertAm05['Step Time'] != 0.000000) & (consultapeukertAm05['Current'] != 0.000)].drop_duplicates(subset=['Current'])

        # Filtra as linhas que não são nulas e não possuem o valor '0' na coluna 'Current'
    linha_especificapeukertAm05 = linha_especificapeukertAm05.dropna(subset=['Current'])

        # Converte o formato de 'Step Time' para horas
    linha_especificapeukertAm05['Step Time'] = pd.to_timedelta(linha_especificapeukertAm05['Step Time'])
    linha_especificapeukertAm05['Step Time'] = linha_especificapeukertAm05['Step Time'].dt.total_seconds() / 3600

    linha_especificapeukertAm05=(linha_especificapeukertAm05[['Step Time', 'Current']])

    am05_CBI22077 = pd.concat([linha_especificaequalizacaoAm05, linha_especificapeukertAm05])
    am05_CBI22077['Step Time'] = am05_CBI22077['Step Time'].round(3)
    am05_CBI22077['Current'] = am05_CBI22077['Current'].round(3)
    

    #-----------------------------AM06----------------------------

        #EQUALIZAÇÃO

        # Carrega os dados do arquivo CSV para o DataFrame do pandas
    consultaequalizacaoAm06 = pd.read_csv("/workspaces/itemm-analyzer/csv's/equalizacaoAm06.csv", delimiter=';', on_bad_lines='skip', low_memory=False)
        # Substitui vírgula por ponto
    consultaequalizacaoAm06['Voltage'] = consultaequalizacaoAm06['Voltage'].str.replace(',', '.')
    consultaequalizacaoAm06['Current'] = consultaequalizacaoAm06['Current'].str.replace(',', '.')
        # Converte as colunas 'Voltage' e 'Current' para float, pulando os valores de string
    consultaequalizacaoAm06['Voltage'] = pd.to_numeric(consultaequalizacaoAm06['Voltage'], errors='coerce')
    consultaequalizacaoAm06['Current'] = pd.to_numeric(consultaequalizacaoAm06['Current'], errors='coerce').abs()
        # Arredonda a coluna 'Voltage' para duas casas decimais
    consultaequalizacaoAm06['Voltage'] = consultaequalizacaoAm06['Voltage'].round(3)

        # Filtra as linhas que contém o valor desejado, remove as linhas com valores nulos e em que a coluna 'Current' é igual a zero
    linha_especificaequalizacaoAm06 = consultaequalizacaoAm06.loc[(consultaequalizacaoAm06['Voltage'] == 1.750) & (consultaequalizacaoAm06['Step Time'] != 0.000000) & (consultaequalizacaoAm06['Current'] != 0.000)].drop_duplicates(subset=['Current'])

        # Converte o formato de 'Step Time' para horas
    linha_especificaequalizacaoAm06['Step Time'] = pd.to_timedelta(linha_especificaequalizacaoAm06['Step Time'])
    linha_especificaequalizacaoAm06['Step Time'] = linha_especificaequalizacaoAm06['Step Time'].dt.total_seconds() / 3600

    linha_especificaequalizacaoAm06 = linha_especificaequalizacaoAm06[['Step Time', 'Current']]


        #PEUKERT

    consultapeukertAm06 = pd.read_csv("/workspaces/itemm-analyzer/csv's/peukertAm06.csv", delimiter=';', on_bad_lines='skip', low_memory=False)
        # Substitui vírgula por ponto
    consultapeukertAm06['Voltage'] = consultapeukertAm06['Voltage'].str.replace(',', '.')
    consultapeukertAm06['Current'] = consultapeukertAm06['Current'].str.replace(',', '.')
        # Converte a coluna 'Voltage' para float, pulando os valores de string
    consultapeukertAm06['Voltage'] = pd.to_numeric(consultapeukertAm06['Voltage'], errors='coerce')
    consultapeukertAm06['Current'] = pd.to_numeric(consultapeukertAm06['Current'], errors='coerce').abs()
    consultapeukertAm06['Voltage'] = consultapeukertAm06['Voltage'].round(3)


        # Filtra as linhas que contém o valor desejado, remove as linhas com valores nulos e em que a coluna 'Current' é igual a zero
    linha_especificapeukertAm06 = consultapeukertAm06.loc[(consultapeukertAm06['Voltage'] == 1.750) & (consultapeukertAm06['Step Time'] != 0.000000) & (consultapeukertAm06['Current'] != 0.000)].drop_duplicates(subset=['Current'])

        # Filtra as linhas que não são nulas e não possuem o valor '0' na coluna 'Current'
    linha_especificapeukertAm06 = linha_especificapeukertAm06.dropna(subset=['Current'])

        # Converte o formato de 'Step Time' para horas
    linha_especificapeukertAm06['Step Time'] = pd.to_timedelta(linha_especificapeukertAm06['Step Time'])
    linha_especificapeukertAm06['Step Time'] = linha_especificapeukertAm06['Step Time'].dt.total_seconds() / 3600
    linha_especificapeukertAm06 = linha_especificapeukertAm06[['Step Time','Current']]

    am06_CBI22077 = pd.concat([linha_especificaequalizacaoAm06, linha_especificapeukertAm06])
    am06_CBI22077['Step Time'] = am06_CBI22077['Step Time'].round(3)
    
    #url_imagem1 = '/static/Figure_1.png'
    #url_imagem2 = '/static/Figure_2.png'

    return render_template("pekeurt.html",consulta1=am01_CBI22076, 
                consulta2=am02_CBI22076, consulta3=am05_CBI22077,
                consulta4=am06_CBI22077)

'''
            #----------GRÁFICOS DO AM01 E AM02-------------------

            # Plotar gráfico para linha_especificaequalizacaoAm01
            plt.scatter(range(len(am01_CBI22076)), am01_CBI22076['Current'], label='am01_CBI22076', marker='o',zorder=2, alpha=1)

            # Plotar gráfico para linha_especificapeukertAm01
            plt.scatter(list(range(len(am01_CBI22076), len(am01_CBI22076)+len(am02_CBI22076))), am02_CBI22076['Current'], label='am02_CBI22076', marker='o', zorder=2, alpha=0.5)


            # Configurar rótulos e título do gráfico
            plt.xlabel('StepTime')
            plt.ylabel('Current')
            plt.title('Gráfico de StepTime vs Current do am01_CBI22076 e am02_CBI22076')

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
            plt.title('Gráfico de StepTime vs Current do am05_CBI22077 e am06_CBI22077')

            # Configurar intervalo dos eixos x e y
            plt.ylim(0, 10)  # Define o intervalo do eixo y de 0 a 10

            #plt.xticks(am01_CBI22076['StepTime'])

            plt.legend()

            # Exibir o gráfico
            plt.show()

            conn.close()

    #url_imagem1 = '/static/Figure_1.png'
    #url_imagem2 = '/static/Figure_2.png'

'''


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
