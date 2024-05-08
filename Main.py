import random
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet_v2 import ResNet50V2, preprocess_input, decode_predictions
import streamlit as st
import pandas as pd
import numpy as np
import csv as cv


st.title("Formulário de Inscrição de Gestão de Pacientes")
dados_de_Pacientes=[]
novo_Paciente=[]
Nomes=[]
Moradas=[]
Numeros=[]
Contactos=[]
#numeroPaciente = 1
numeroPaciente= random.randint(1, 1000)
def PesquisaB(numero):

    if numero in Pesquisa:
        st.title("Resultado da Pesquisa")
        st.title('Numero:',numeroPaciente)
        st.title('Nome',Nome)




Pesquisa = st.sidebar.text_input("Pesquisa por numero de Processo")
button = st.sidebar.button("Pesquise Por Nome de Paciente", on_click=PesquisaB, args=(numeroPaciente))

menu = ["Menu", "Pesquisa" ,"Análises Clínicas", "IMAGE - Classifier APP",]
choice = st.selectbox("Selecione uma Opção", menu)

def menu():



    if choice == "Menu":
        st.header("Dados Pessoais")

        col1, col2 = st.columns(2)
        with col1:
            st.header("Número de Paciente")
        with col2:
            #numeroPaciente = int(1) 
            st.header(numeroPaciente)
        Nome = st.text_input("Nome Completo")
        Nomes.append(Nome)
        st.write(Nome)



        Morada = st.text_input("Morada")
        st.text(Morada)
        Contacto = st.text_input("Contacto")
        Contactos.append(Contacto)
        col1, col2 = st.columns(2)
        with col1:
            Especialidade = st.multiselect(label=("Selecione uma Especialidade Médica"),options=["Hemograma","Radiologia","Anatomia Patológica"])
        with col2:
            Idade = st.text_input("Idade")
        #numeroPaciente = st.header(numeroPaciente)
        ###################################
        
        Button = st.button("Adicionar Paciente", key='add')
        if Button == True:
            Numeros.append(numeroPaciente)
            novo_Paciente = ({"Número": Numeros, "Nome": [Nome], "Morada": [Morada], "Contacto": [Contacto]})
            dados_de_Pacientes.append(novo_Paciente)
            df = pd.DataFrame(dados_de_Pacientes)
            #df = pd.DataFrame(dados_de_Pacientes, columns=["Número", "Nome", "Morada"])

            df.to_csv("Lista_de_Pacientes2.csv", sep=",")
            st.success("Paciente Adicionado com Sucesso")
            st.table(dados_de_Pacientes)

        #else:
            #data = [{'Numero': [numero], 'Paciente': [Nomes], 'Morada': [Morada],}]
            #df2 = pd.DataFrame(data={'Numero': [numero], 'Paciente': [Nomes], 'Morada': [Morada],})
            # Alteração de Teste na Criação do CSV

            #df.append(data)
            #df2.to_csv("Lista_de_Pacientes2.csv", sep=";")
            #st.dataframe(df2, width=700)

        #articles = pd.read_csv('Lista_de_Pacientes.csv' ,sep=",")
       # st.dataframe(articles, width=700)

    if choice == "Pesquisa":
        Pesquisa = st.text_input("Pesquisa por numero de Paciente [entre parentisis]", key="submit")
        clicked = st.button("Pesquise Por Nome de Paciente", args=(numeroPaciente), key="Submit2")
        df = pd.read_csv('Lista_de_Pacientes2.csv', sep=",")
        #st.dataframe(articles, width=700)
        if clicked == True:
            ###################################
            #for Pesquisa in Numeros:
                #if numeroPaciente or Nome in df:
            st.title("Resultado da Pesquisa")
    #########################################
            #st.title(Nomes, numeroPaciente, Morada)
            df = pd.read_csv('Lista_de_Pacientes2.csv', sep=",")
            ###################################
            #filtro2 = df[df['Numeros']]
            st.write("DataFrame com filto por numero de paciente: ")
            filter2 = df[df["Número"] == Pesquisa]
            st.table(filter2)
            #st.dataframe(df, width=700)
           
                    



    if choice == "Análise Clínicas":
        soma = 0
        Lista = [11, 16, 19, 18]
        num = 0
        st.header("Análises Clinicas")
        Disciplina1 = st.multiselect(label=("Selecione uma Disciplina"),options=["Ferrantina", "Hemoglobina","Leucócitos","Creatinina","Proteina C-reativa"])
        st.write("Valores de referência")

        Notas = st.number_input("Introduza o valor registado", min_value=5)

        for valores in Lista:
            soma += valores/ len(Lista)

        for valores in Lista:

            st.write(" Dentro dos Valores de Referência ", valores)

        if soma >= 15:
            st.write("Dentro dos Valores", soma)
        else:
            st.write(" Dentro dos Valores ", soma )

    if choice == "IMAGE - Classifier APP":

        #elif choice == 'IMAGE - Classifier APP':
         
        model = ResNet50V2(weights='imagenet')

        # título da página
        st.title('Detecção e classificação de imagens médicas')
        st.write("<a href='https://diagnose-images.streamlit.app/' id='my-link'>Detecção e classificação de imagens diagnóstico</a>", unsafe_allow_html=True)

        # layout da página
        col1, col2 = st.columns(2)
        with col1:
            # uploader de imagem
            st.header('Upload da imagem de diagnóstico')
            uploaded_file = st.file_uploader("Escolha uma imagem...", type=["jpg", "jpeg", "png", 'gif'])
            
        with col2:
            st.header('Imagem de exemplo')
            st.image(uploaded_file)
            st.subheader("O Erro Apresentado é de TESTES - Podem continuar Fazendo o UPload")
        
        if uploaded_file is not None:
            # carregando a imagem
            img = image.load_img(uploaded_file, target_size=(224, 224))

            # exibindo a imagem
            st.image(img, caption='Imagem carregada', use_column_width=True)

            # pré-processamento da imagem
            x = image.img_to_array(img)
            x = np.expand_dims(x, axis=0)
            x = preprocess_input(x)

            # passando a imagem pelo modelo para realizar a classificação
            preds = model.predict(x)

            # decodificando as previsões
            decoded_preds = decode_predictions(preds, top=3)[0]

            # exibindo as previsões
            if len(decoded_preds) > 0:
                st.subheader("Previsões:")
                for result in decoded_preds:
                    label = result[1]
                    prob = result[2]
                    st.subheader(f'{label} : {prob * 100} %')
                with open('results.csv', 'a') as f:
                    with csv.DictWriter(f, fieldnames = [ "Label", "Probabilidades"]):
                        writer.writeheader()
                for r in results:
                    writer.writerow(r)
            else:
                st.write("A imagem n é valida")
            # for label, prob in decoded_preds:
            chart_data = pd.read_csv('results.csv', sep=',')
            # if len(decoded_preds) >=2:
            #  label,_,prob = decoded_preds[0]
            # st.write('%s (%.2f%%)' % (label, prob * 100))
            # label,_,prob = decoded_preds[1]
            # st.write(f'{label}:{prob:2%}')
        st.image("/Users/paulomonteiro/PycharmProjects/Formulário_Pacientes/button2.png")
        st.markdown('<a name="menu"></a>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            # uploader de imagem
            st.header('Upload da imagem')
            uploaded_file = st.file_uploader("Escolha uma imagem...", type=["jpg", "jpeg", "png", "csv", "GIF", "gif"])

        with col2:
            st.header('Fotografia do Paciente')
            st.image(uploaded_file)

        if uploaded_file is True:
                # carregando a imagem
                img = st.image.load_img(uploaded_file, target_size=(125, 125))

                # exibindo a imagem
                st.image(img, caption='Imagem carregada', use_column_width=True)
#def option_menu(choice):

    #if choice == "menu":
            #st.text("Deseja adicionar ao carrinho")
            #st.number_input("Introduza Quantidade")



        if st.button("Adicionar ao carrinho"):
            st.markdown("[ir para secção](#menu)")
        html = f"<a href='{menu}'><img src='data:/Users/paulomonteiro/PycharmProjects/Formulário_Pacientes/button2.png/png;base64,{choice == Menu}'></a>"
        st.markdown(html, unsafe_allow_html=True)

menu()

        # pré-processamento da imagem
        #x = image.img_to_array(img)
        #x = np.expand_dims(x, axis=0)
        #x = preprocess_input(x)
