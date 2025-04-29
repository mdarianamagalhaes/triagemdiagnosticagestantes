# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 18:36:54 2025

@author: arian
"""
import streamlit as st

# --- CLASSES DE PROTOCOLOS DIAGNÓSTICOS ---
class SindromeCoronarianaAgudaApp:
    def __init__(self):
        self.tipo_dor = None
        self.fatores_agravantes = None
        self.duracao_dor = None
        self.fatores_risco = None
        self.ecg_resultado = None
        self.marcadores_cardiacos = None
        self.protocolo_negativo = False

    def run(self):
        st.title("📍 Protocolo de Infarto Agudo do Miocárdio na Gestação")

        st.subheader("1️⃣ Classificação da dor torácica")
        tipo = st.radio(
            "Classifique o tipo de dor:",
            options=[
                "A - Definitivamente anginosa",
                "B - Provavelmente anginosa",
                "C - Provavelmente não anginosa",
                "D - Definitivamente não anginosa",
            ],
        )
        self.tipo_dor = tipo.split(" - ")[0]

        st.subheader("2️⃣ Fatores agravantes/alívio e duração")
        self.fatores_agravantes = st.radio(
            "A dor piora com esforço ou alivia com repouso ou nitrato?", ["Sim", "Não"]
        )
        self.duracao_dor = st.radio("A dor dura mais de 10 minutos?", ["Sim", "Não"])

        st.subheader("3️⃣ Fatores de risco")
        self.fatores_risco = st.radio(
            "A paciente tem fatores de risco (HAS, idade > 60, dislipidemia, tabagismo, diabetes, aterosclerose)?",
            ["Sim", "Não"],
        )

        st.subheader("4️⃣ ECG")
        ecg = st.radio(
            "O ECG apresenta Supra ST ou Bloqueio de Ramo Novo?", ["Sim", "Não"]
        )
        if ecg == "Sim":
            self.ecg_resultado = "Infarto com Supra ST"
            st.success("✅ Infarto com Supra ST detectado. Iniciar tratamento imediato.")
            self.tratamento_imediato()
        else:
            self.ecg_resultado = "Isquemia ou alterações inespecíficas"
            self.monitoramento_continuo()

    def monitoramento_continuo(self):
        st.subheader("📊 Monitoramento contínuo (9 horas)")
        st.info("Avaliações a cada 3h: exame físico, ECG seriado, marcadores cardíacos.")
        marcadores = st.radio("Marcadores cardíacos realizados?", ["Sim", "Não"])
        self.marcadores_cardiacos = marcadores

        if marcadores == "Sim":
            resultado = st.radio("O protocolo foi positivo?", ["Sim", "Não"])
            if resultado == "Sim":
                st.success("✅ Diagnóstico de SCA confirmado.")
                self.tratamento_imediato()
            else:
                self.protocolo_negativo = True
                st.warning("❌ Protocolo negativo. Avaliar outras causas de dor torácica.")

    def tratamento_imediato(self):
        st.subheader("🚑 Tratamento imediato do IAM na gestação")

        st.markdown("### 🔍 Etiologia orienta conduta:")
        st.markdown(
            """
        - **Lesão aterosclerótica** → Revascularização (ICP ou CRM)  
        - **Dissecção coronária** → Terapia conservadora  
        - **Trombo coronariano** → Aspiração + angioplastia com balão (stent como resgate)
        """
        )

        st.markdown("### 🛑 Medidas gerais:")
        st.markdown(
            """
        - Baixo risco: observação em pronto-socorro ou unidade de dor torácica  
        - Risco intermediário/alto: UCO ou UTI  
        - Monitorização eletrocardiográfica contínua  
        - Acesso venoso periférico  
        - O2 se SpO2 < 90% (cateter 2-4 L/min)  
        - Dor refratária: morfina IV 2-4 mg, repetir cada 5-10 min  
        ⚠️ Evitar morfina se náuseas, vômitos ou hipotensão
        """
        )

        st.markdown("### 💊 Medicamentos:")
        st.markdown(
            """
        - **AAS**: 75-162 mg/dia (seguro após 1º trimestre)  
        - **Clopidogrel**: usar apenas se necessário; suspender 7 dias antes do parto  
        - **Betabloqueadores**: Metoprolol (até 200mg/dia), Atenolol (100mg/dia)  
        - **Nitratos**: com cautela. Evitar se PAS < 100 mmHg  
        - **Nitroglicerina IV**: iniciar com 10 µg/min
        """
        )

        st.markdown("### 🧪 Anticoagulação:")
        st.markdown(
            """
        - **Enoxaparina**: 1 mg/kg SC 12/12h  
        - ClCr < 30 ml/min → dose 1x/dia  
        ⚠️ Contraindicada em sangramento ativo ou plaquetopenia
        """
        )

        st.markdown("### 👶 Monitoramento fetal contínuo")

        st.markdown("### 🗓️ Planejamento do parto:")
        st.markdown(
            """
        - Adiar parto por 2-3 semanas após IAM se estável  
        - **Parto vaginal preferido**  
        - Cesárea apenas se instabilidade materna
        """
        )

        st.markdown("### 🚫 Medicamentos contraindicados:")
        st.markdown(
            """
        - Estatinas, iECA, ARBs, fibrinolíticos  
        - Methergina e prostaglandinas (vasoativas)
        """
        )

# --- PERGUNTAS PADRÃO PARA AVALIAÇÃO INICIAL ---
perguntas_avaliacao = {
    "dor torácica": "Paciente apresenta dor torácica?",
    "irradiação da dor": "A dor irradia para braço, mandíbula ou dorso?",
    "duração da dor >10min": "A dor torácica dura mais de 10 minutos?",
    "fatores de risco (HAS, DM, dislipidemia, tabagismo, idade >60)": "Há fatores de risco cardiovasculares (HAS, DM, dislipidemia, tabagismo, idade >60 anos)?",
    "alívio com nitrato": "A dor alivia com repouso ou uso de nitrato?",
    "náusea": "Paciente relata náusea?",
    "dispneia": "Paciente apresenta dispneia?",
    "pa >140/90": "A pressão arterial está acima de 140/90 mmHg?",
    "cefaleia frontal ou occipital": "Paciente refere cefaleia frontal ou occipital?",
    "visão embaçada": "Paciente apresenta visão embaçada?",
    "edema persistente": "Paciente apresenta inchaço (edema) persistente que não melhora com repouso?",
    "dor epigástrica": "Paciente sente dor epigástrica ou no quadrante superior direito?",
    "náusea e vômito": "Paciente apresenta náuseas e vômitos frequentes?",
    "convulsões": "Paciente apresentou convulsões?",
    "dispneia aos esforços": "Paciente tem falta de ar aos esforços?",
    "ortopneia": "Paciente tem dificuldade de respirar ao deitar (ortopneia)?",
    "dispneia paroxística noturna": "Paciente tem crises de falta de ar durante a noite?",
    "edema de membros inferiores": "Paciente apresenta inchaço nas pernas?",
    "fadiga intensa": "Paciente tem cansaço intenso desproporcional à atividade?",
    "congestão abdominal": "Há sintomas como náusea ou distensão abdominal?",
    "dor torácica lancinante": "A dor torácica é descrita como muito intensa ou lancinante?",
    "dor irradiada para dorso": "A dor se irradia para as costas?",
    "sensação de rasgamento": "Paciente descreve sensação de rasgamento ou dilaceração?",
    "síncope": "Paciente apresentou desmaios (síncope)?",
    "tontura": "Paciente sente tonturas frequentes?",
    "dispneia importante": "Paciente apresenta dispneia intensa, com dificuldade de falar?"
}

# Dicionário de doenças
doencas = {
    "Síndrome Coronariana Aguda": {
        "sintomas": ["dor torácica", "irradiação da dor", "duração da dor >10min", "náusea", "síncope", "dispneia importante"],
        "classe": lambda: SindromeCoronarianaAgudaApp().run()
    },
    "Distúrbio Hipertensivo da Gestação": {
        "sintomas": ["pa >140/90", "cefaleia frontal ou occipital", "visão embaçada", "edema persistente", "convulsões", "dor epigástrica"],
        "classe": lambda: st.write("⚠️ Iniciando protocolo para Distúrbio Hipertensivo da Gestação...")
    },
    "Insuficiência Cardíaca": {
        "sintomas": ["dispneia aos esforços", "ortopneia", "dispneia paroxística noturna", "edema de membros inferiores", "fadiga intensa", "congestão abdominal"],
        "classe": lambda: st.write("🟠 Iniciando protocolo para Insuficiência Cardíaca...")
    },
    "Dissecção de Aorta": {
        "sintomas": ["dor torácica lancinante", "dor irradiada para dorso", "sensação de rasgamento", "síncope", "tontura"],
        "classe": lambda: st.write("🔴 Iniciando protocolo para Dissecção de Aorta...")
    }
}

# Interface
st.set_page_config(page_title="Triagem Clínica Inicial", layout="centered")
st.title("🤰 Triagem Clínica para Gestantes com Sintomas Cardiovasculares")
st.markdown("Responda às perguntas abaixo com base na avaliação clínica inicial da gestante:")

with st.form("form_triagem"):
    respostas = {}
    for chave, pergunta in perguntas_avaliacao.items():
        respostas[chave] = st.radio(pergunta, options=["Sim", "Não"], key=chave)
    enviado = st.form_submit_button("🔍 Avaliar Sintomas")

if enviado:
    st.subheader("📊 Análise dos sintomas informados:")
    sugestoes = []
    for nome_doenca, dados in doencas.items():
        sintomas_presentes = [s for s in dados["sintomas"] if respostas.get(s) == "Sim"]
        if sintomas_presentes:
            sugestoes.append((nome_doenca, len(sintomas_presentes), sintomas_presentes))

    sugestoes.sort(key=lambda x: x[1], reverse=True)

    if not sugestoes:
        st.error("❌ Nenhuma hipótese clínica sugerida com os sintomas fornecidos.")
    else:
        st.success("✅ Hipóteses clínicas sugeridas com base nos sintomas:")

        for i, (nome, score, sintomas_encontrados) in enumerate(sugestoes, 1):
            with st.expander(f"{i}. {nome} ({score} sintomas compatíveis)"):
                st.write(f"**Sinais e sintomas compatíveis:** {', '.join(sintomas_encontrados)}")
                if st.button(f"Iniciar protocolo para {nome}", key=f"btn_{nome}_{i}"):
                    doencas[nome]["classe"]()
