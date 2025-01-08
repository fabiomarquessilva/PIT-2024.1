import streamlit as st
import pandas as pd

# Configuração inicial
st.set_page_config(
    page_title="Cálculo de Carga Horária Docente",
    layout="wide"
)

# Cabeçalho Institucional
st.markdown('''
<div style='text-align: center; font-family: Arial;'>
    <h2>UNIVERSIDADE FEDERAL DE CAMPINA GRANDE</h2>
    <h3>CENTRO DE FORMAÇÃO DE PROFESSORES</h3>
    <h4>UNIDADE ACADÊMICA DE ENFERMAGEM</h4>
</div>
''', unsafe_allow_html=True)

# Título do aplicativo
st.title("Cálculo de Carga Horária Docente")

# Explicação inicial
st.markdown("""
Este aplicativo permite calcular a carga horária semanal total com base nas atividades descritas no PIT.
Preencha as tabelas abaixo para incluir as horas em cada categoria.
""")

# Definindo categorias e criando tabelas
categories = {
    "Ensino (Graduação e/ou Pós-Graduação)": ["Disciplinas ministradas", "Aulas práticas", "Orientações individuais"],
    "Pesquisa": ["Projetos em andamento", "Publicações científicas"],
    "Extensão": ["Projetos de extensão", "Ações comunitárias"],
    "Administrativas": ["Reuniões", "Atividades de coordenação"],
    "Monitoria": ["Atividades de monitoria"],
    "TCC/Orientação": ["Trabalhos de conclusão orientados"],
    "Produção Intelectual": ["Publicações e apresentações"],
    "Outras Atividades": ["Comissões", "Palestras"],
    "Teletrabalho": ["Atividades pedagógicas remotas"]
}

# Criando tabelas para entrada de dados
data = {}
for category, items in categories.items():
    st.subheader(f"🔢 {category}")
    table = pd.DataFrame({"Atividade": items, "Horas Semanais": [0] * len(items)})
    table["Horas Semanais"] = st.experimental_data_editor(
        table, key=category, num_rows="dynamic"
    )
    data[category] = table

# Cálculo dos totais por categoria
totals = {category: table["Horas Semanais"].sum() for category, table in data.items()}

# Mostrando o resultado final em uma tabela
st.markdown("---")
st.markdown("### Resumo da Carga Horária Semanal")
result_table = pd.DataFrame.from_dict(totals, orient="index", columns=["Horas Totais"])
st.dataframe(result_table.style.format("{:.1f}"), use_container_width=True)

# Cálculo da carga horária total
carga_total = result_table["Horas Totais"].sum()

# Resultado final
st.markdown("---")
st.markdown("<h3 style='text-align: center; color: #007BFF;'>Carga Horária Semanal Total</h3>", unsafe_allow_html=True)
st.markdown(f"<h1 style='text-align: center; color: #28a745;'>{carga_total} horas</h1>", unsafe_allow_html=True)
st.markdown("---")

# Rodapé
st.markdown('''
<div style='text-align: center; font-size: small; color: gray; margin-top: 50px;'>
    Desenvolvido para cálculo de carga horária docente com base no PIT da UAENF
</div>
''', unsafe_allow_html=True)

import streamlit as st

# Configuração inicial
st.set_page_config(
    page_title="Cálculo de Carga Horária Docente",
    layout="centered"
)

# Cabeçalho Institucional
st.markdown('''
<div style='text-align: center; font-family: Arial;'>
    <h2>UNIVERSIDADE FEDERAL DE CAMPINA GRANDE</h2>
    <h3>CENTRO DE FORMAÇÃO DE PROFESSORES</h3>
    <h4>UNIDADE ACADÊMICA DE ENFERMAGEM</h4>
</div>
''', unsafe_allow_html=True)

# Título da página
st.title("Cálculo de Carga Horária Docente")

# Explicação inicial
st.markdown("""
Este aplicativo permite calcular a carga horária semanal total com base nas atividades descritas no PIT.
Edite os valores abaixo para ajustar as horas de acordo com as atividades realizadas.
""")

# Entradas de dados para as atividades
st.subheader("🔢 Insira as Cargas Horárias Semanais")
ensino = st.number_input("Atividades de Ensino (Graduação e/ou Pós-Graduação):", min_value=0, value=22, step=1)
pesquisa = st.number_input("Atividades de Pesquisa:", min_value=0, value=18, step=1)
extensao = st.number_input("Atividades de Extensão:", min_value=0, value=6, step=1)
administrativas = st.number_input("Atividades Administrativas e de Representação:", min_value=0, value=1, step=1)
monitoria = st.number_input("Atividades de Monitoria Acadêmica:", min_value=0, value=18, step=1)
tcc_orientacao = st.number_input("Orientação de Trabalho de Conclusão de Curso (TCC):", min_value=0, value=4, step=1)
producao_intelectual = st.number_input("Atividades de Produção Intelectual:", min_value=0, value=5, step=1)
outras = st.number_input("Outras Atividades (comissões, palestras, etc.):", min_value=0, value=0, step=1)
teletrabalho = st.number_input("Atividades Pedagógicas Remotas por Teletrabalho:", min_value=0, value=0, step=1)

# Cálculo da carga horária total
carga_total = (ensino + pesquisa + extensao + administrativas +
               monitoria + tcc_orientacao + producao_intelectual +
               outras + teletrabalho)

# Resultado final
st.markdown("---")
st.markdown("<h3 style='text-align: center; color: #007BFF;'>Carga Horária Semanal Total</h3>", unsafe_allow_html=True)
st.markdown(f"<h1 style='text-align: center; color: #28a745;'>{carga_total} horas</h1>", unsafe_allow_html=True)
st.markdown("---")

# Rodapé
st.markdown('''
<div style='text-align: center; font-size: small; color: gray; margin-top: 50px;'>
    Desenvolvido para cálculo de carga horária docente com base no PIT da UAENF
</div>
''', unsafe_allow_html=True)
