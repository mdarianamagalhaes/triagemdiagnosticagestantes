# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 10:07:11 2025

@author: arian
"""
# --- CLASSES DE PROTOCOLOS DIAGNÓSTICOS (iguais aos anteriores, mantidas para reutilização) ---
class EmergenciaCardiovascular:
    def __init__(self):
        self.tipo_dor = None
        self.fatores_agravantes = None
        self.fatores_risco = None
        self.ecg_resultado = None
        self.marcadores_cardiacos = None
        self.protocolo_negativo = False

    def iniciar(self):
        print("\n📍 Iniciando protocolo: Infarto Agudo do Miocárdio")
        self.classificar_dor()
        self.fatores_agravantes_alivio()
        self.fatores_risco_func()
        self.realizar_ecg()

    def classificar_dor(self):
        print("Classifique o tipo de dor:")
        print("1 - Dor Tipo A (Definitivamente anginosa)")
        print("2 - Dor Tipo B (Provavelmente anginosa)")
        print("3 - Dor Tipo C (Provavelmente não anginosa)")
        print("4 - Dor Tipo D (Definitivamente não anginosa)")
        escolha = input("Escolha o tipo de dor (1-4): ")
        tipos = {"1": "A", "2": "B", "3": "C", "4": "D"}
        self.tipo_dor = tipos.get(escolha)
        if self.tipo_dor is None:
            print("Opção inválida. Tente novamente.")
            self.classificar_dor()

    def fatores_agravantes_alivio(self):
        print("A dor piora com esforço ou alivia com repouso ou nitrato? (sim/não)")
        self.fatores_agravantes = input("Resposta: ").strip().lower()

        print("Duração da dor superior a 10 minutos? (sim/não)")
        resposta = input("Resposta: ").strip().lower()
        if resposta == 'sim':
            self.fatores_agravantes += " | duração > 10 min"

    def fatores_risco_func(self):  # Renomeado para evitar conflito com o atributo
        print("A paciente tem fatores de risco? (HAS, idade > 60 anos, dislipidemia, tabagismo, diabetes mellitus, aterosclerose manifesta) (sim/não)")
        self.fatores_risco = input("Resposta: ").strip().lower()

    def realizar_ecg(self):
        print("Realizar ECG em até 10 minutos.")
        print("O ECG apresenta Supra ST ou Bloqueio de Ramo Novo? (sim/não)")
        resposta = input("Resposta: ").strip().lower()
        if resposta == 'sim':
            self.ecg_resultado = "Infarto com Supra ST"
            print("Infarto com Supra ST. Tratamento imediato para SCA.")
            self.tratamento_imediato()
        else:
            self.ecg_resultado = "Isquemia ou Alterações Inespecíficas"
            self.monitoramento_continuo()

    def monitoramento_continuo(self):
        print("Iniciar monitoramento contínuo por 9 horas.")
        print("Realizar avaliações a cada 3 horas.")
        print("Avaliações necessárias: Exame físico, ECG seriado, Marcadores cardíacos.")
        self.marcadores_cardiacos = input("Exames de marcadores cardíacos realizados? (sim/não): ").strip().lower()
        if self.marcadores_cardiacos == 'sim':
            print("Realizar avaliação final do protocolo.")
            self.protocolo_final()

    def protocolo_final(self):
        print("O protocolo foi positivo? (sim/não): ")
        resposta = input("Resposta: ").strip().lower()
        if resposta == 'sim':
            print("Diagnóstico de SCA confirmado.")
            self.tratamento_imediato()
        else:
            self.protocolo_negativo = True
            print("Descartar SCA e avaliar outras causas de dor torácica.")

    def tratamento_imediato(self):
        print("🔍 Determinar etiologia do IAM na gestante orienta a conduta:")
        print("- Lesão aterosclerótica → Revascularização (ICP ou CRM).")
        print("- Dissecção coronária → Terapia conservadora (salvo complicações graves).")
        print("- Trombo coronariano → Aspiração + angioplastia com balão (stent como resgate).")
        
        print("\n🛑 Tratamento inicial:")
        print("➡️ Medidas gerais:")
        print("- Baixo risco: observação em pronto-socorro ou unidade de dor torácica.")
        print("- Risco intermediário/alto: UCO ou UTI.")
        print("- Monitorização eletrocardiográfica contínua e acesso venoso periférico.")
        print("- O2 se SpO2 < 90% (cateter 2-4 L/min).")
        print("- Dor refratária: morfina IV 2-4 mg, repetir a cada 5-10 min se necessário.")
        print("⚠️ Evitar morfina em casos de náuseas, vômitos ou hipotensão.")
        
        print("\n💊 Medicamentos e terapias:")
        print("- Aspirina: 75-162 mg/dia (segura após 1º trimestre).")
        print("- Clopidogrel: usar apenas se necessário; suspender 7 dias antes do parto.")
        print("  ➤ Dupla antiagregação (AAS + Clopidogrel) por 1 mês após stent; até 3 meses se alto risco isquêmico.")
        print("  ⚠️ Não usar prasugrel, ticagrelor, bivalirudina ou inibidores GP IIb/IIIa.")
        print("- Betabloqueadores: seguros.")
        print("  ➤ Metoprolol (até 200mg/dia, risco C), Atenolol (até 100mg/dia, risco D).")
        print("- Nitratos: usar com cautela. Evitar se PAS < 100 mmHg.")
        print("  ➤ Dinitrato de isossorbida SL: 5 mg, até 3 doses/5 min.")
        print("  ➤ Nitroglicerina IV: iniciar com 10 µg/min, ajustar conforme sintomas/PA.")
        
        print("\n🧪 Anticoagulação:")
        print("- Enoxaparina: 1 mg/kg SC 12/12h; se ClCr < 30 ml/min → 1x/dia.")
        print("  ⚠️ Contraindicada em sangramento ativo, plaquetopenia importante, coagulopatias.")
        print("- Suspender heparina antes do parto para reduzir risco de sangramento.")
        
        print("\n👶 Monitoramento fetal contínuo.")
        
        print("\n🗓️ Planejamento do parto:")
        print("- Adiar parto por 2-3 semanas após IAM, se estável.")
        print("- Parto vaginal preferido; cesárea em casos instáveis.")
        
        print("\n🚫 Medicamentos contraindicados:")
        print("- Estatinas, iECA, ARBs, fibrinolíticos (sem estudos seguros na gravidez).")
        print("- Evitar drogas vasoativas como methergina e prostaglandinas.")

class DisturbioHipertensivoGestacao:
    def __init__(self):
        self.pa_sistolica = None
        self.pa_diastolica = None
        self.proteinuria_24h = None
        self.indice_proteinuria_creatinina = None
        self.ast = None
        self.alt = None
        self.creatinina = None
        self.plaquetas = None
        self.dhl = None
        self.sintomas = []
        self.idade_gestacional = None
        self._diagnostico_final = None  # Armazena o diagnóstico para reuso

    def iniciar(self):
        print("\n📍 Iniciando protocolo: Distúrbios Hipertensivos da Gestação")

        self.pa_sistolica = int(input("Pressão sistólica (mmHg): "))
        self.pa_diastolica = int(input("Pressão diastólica (mmHg): "))
        self.idade_gestacional = int(input("Idade gestacional (semanas): "))

        self.proteinuria_24h = float(input("Proteinúria em 24h (mg): "))
        self.indice_proteinuria_creatinina = float(input("Índice proteinúria/creatinina (mg/dL): "))
        self.ast = float(input("AST (U/L): "))
        self.alt = float(input("ALT (U/L): "))
        self.creatinina = float(input("Creatinina sérica (mg/dL): "))
        self.plaquetas = int(input("Plaquetas (/mm³): "))
        self.dhl = float(input("DHL (U/L): "))

        sintomas = input("Liste os sintomas separados por vírgula (ex: cefaleia intensa, escotomas, dor epigástrica, convulsao): ")
        self.sintomas = [s.strip().lower() for s in sintomas.split(",")]

        self._diagnostico_final = self.diagnostico()
        print(f"\n🔎 Diagnóstico: {self._diagnostico_final}")
        self.conduta()

    def diagnostico(self):
        hipertensao = self.pa_sistolica >= 140 or self.pa_diastolica >= 90
        hipertensao_grave = self.pa_sistolica >= 160 or self.pa_diastolica >= 110
        proteinuria = self.proteinuria_24h > 300 or self.indice_proteinuria_creatinina >= 0.3
        lesao_renal = self.creatinina > 1.1
        trombocitopenia = self.plaquetas < 100000
        enzimas_hepaticas_elevadas = self.ast > 80 or self.alt > 80
        dhl_alto = self.dhl >= 600
        sintomas_graves = any(s in self.sintomas for s in ['cefaleia intensa', 'escotomas', 'dor epigástrica', 'visão turva', 'edema pulmonar', 'convulsao'])

        if hipertensao and self.idade_gestacional < 20:
            return "Hipertensão crônica"

        if hipertensao and self.idade_gestacional >= 20:
            if 'convulsao' in self.sintomas:
                return "Eclâmpsia"

            if hipertensao_grave or sintomas_graves or trombocitopenia or enzimas_hepaticas_elevadas or lesao_renal:
                if trombocitopenia and dhl_alto and enzimas_hepaticas_elevadas:
                    return "Síndrome HELLP"
                return "Pré-eclâmpsia com critérios de gravidade"

            elif proteinuria:
                return "Pré-eclâmpsia"

            return "Hipertensão gestacional"

        return "Sem distúrbio hipertensivo"

    def conduta(self):
        print("\n📋 Conduta sugerida:")

        hipertensao = self.pa_sistolica >= 140 or self.pa_diastolica >= 90
        hipertensao_grave = self.pa_sistolica >= 160 or self.pa_diastolica >= 110
        eclampsia = "convulsao" in self.sintomas
        idade_gestacional = self.idade_gestacional
        diagnostico = self._diagnostico_final or self.diagnostico()

        if eclampsia:
            print("🟣 ECLÂMPSIA – Manejo de crise convulsiva:")
            print("• Sulfato de Magnésio (Esquema de Pritchard):")
            print("  - Ataque: 4g IV lento + 10g IM (5g por nádega).")
            print("  - Manutenção: 5g IM a cada 4h.")
            print("• Alternativa: Esquema de Zuspan: 4g IV + 1g/h em bomba de infusão.")
            print("• Acompanhar diurese, FR e reflexos tendinosos.")
            print("• Antídoto: Gluconato de cálcio 10%, 1 ampola IV.")
            print("• Considerar parto imediato após estabilização.")
            return

        if hipertensao_grave:
            print("🔴 EMERGÊNCIA HIPERTENSIVA:")
            print("• Decúbito lateral esquerdo.")
            print("• Instalar SG 5% EV.")
            print("• Nifedipina 10 mg VO, repetir a cada 30 min até controle (máx 30 mg).")
            print("• Se falha: Hidralazina 5 mg IV (repetir até 20 mg).")
            print("• Alternativa: Labetalol IV (20 mg → 40 mg → até 220 mg).")
            print("• Monitorar PA a cada 5 min e cardiotocografia por 20 min.")
            print("• Objetivo: manter PA <160/110 mmHg e >135/85 mmHg.")

        elif hipertensao:
            print("🟡 HIPERTENSÃO (Crônica ou Gestacional):")
            print("• Monitoramento da PA a cada 1-2 semanas.")
            print("• Medicamentos de 1ª linha:")
            print("  - Metildopa: 250–500 mg VO 2–3x/dia, máx 3000 mg/dia.")
            print("  - Nifedipino LA: iniciar 10 mg VO, ajustar até 120 mg/dia.")
            print("  - Labetalol: 20 mg IV em bolus, máx 220 mg.")
            print("  - Metoprolol: 12,5 mg VO, máx 200 mg/dia.")
            print("• Segunda linha:")
            print("  - Clonidina: 0,2–0,6 mg/dia.")
            print("  - Hidralazina: 25 mg, 4x/dia, máx 200 mg/dia.")
            print("• Objetivo: PA <140/90 mmHg.")
            print("• Acompanhamento fetal regular.")
            print("• Evitar repouso absoluto, dietas hipossódicas ou perda de peso.")
            print("• Contraindicados: IECA, BRA, inibidores diretos da renina, espironolactona, atenolol.")

        # Avaliação de sinais de gravidade
        if any(palavra in sint for sint in self.sintomas for palavra in ["cefaleia", "escotoma", "epigástrica"]):
            print("\n⚠️ Sinais de gravidade detectados: avaliar possibilidade de parto imediato.")

        # Condutas específicas
        if "pré-eclâmpsia com critérios de gravidade" in diagnostico.lower():
            if idade_gestacional < 34:
                print("\n🔴 PRÉ-ECLÂMPSIA GRAVE (<34 semanas):")
                print("• Internação e avaliação materno-fetal por 24h.")
                print("• Sulfato de magnésio e anti-hipertensivos se PAS ≥160 e/ou PAD ≥110.")
                print("• Corticoide para maturação pulmonar.")
                print("• Se complicações maternas ou fetais → parto imediato.")
            else:
                print("\n🔴 PRÉ-ECLÂMPSIA GRAVE (≥34 semanas):")
                print("• Indicar parto pela via apropriada.")
                print("• Terceira etapa do parto vaginal deve ser ativa (prevenção de hemorragia).")

        elif "pré-eclâmpsia" in diagnostico.lower():
            if idade_gestacional < 34:
                print("\n👶 PRÉ-ECLÂMPSIA (<34 semanas):")
                print("• Monitoramento rigoroso.")
                print("• Corticoide para maturação pulmonar:")
                print("  - Betametasona 12 mg IM a cada 24h (2 doses) OU")
                print("  - Dexametasona 6 mg IM a cada 12h (4 doses).")
                print("• Avaliar prolongamento da gestação por até 1–2 semanas.")
            elif idade_gestacional < 40:
                print("\n👶 PRÉ-ECLÂMPSIA (<40 semanas):")
                print("• Monitoramento clínico e laboratorial.")
            else:
                print("\n👶 PRÉ-ECLÂMPSIA (≥40 semanas):")
                print("• Indicar parto após estabilização clínica e hemodinâmica.")

        # Via de parto
        print("\n🚼 Considerações sobre via de parto:")
        print("• Preferência por parto vaginal, exceto indicação obstétrica para cesárea.")
        print("• Indução deve considerar maturidade e condições do colo.")
        print("• Parto cesáreo urgente se instabilidade materna ou sofrimento fetal.")

class InsuficienciaCardiaca:
    def __init__(self):
        self.fatores_risco = 0
        self.sintomas_chave = 0
        self.criterios_maiores = 0
        self.criterios_menores = 0

    def obter_resposta(self, pergunta):
        resposta = input(f"{pergunta} (sim/não): ").strip().lower()
        while resposta not in ["sim", "não"]:
            print("Resposta inválida! Por favor, responda 'sim' ou 'não'.")
            resposta = input(f"{pergunta} (sim/não): ").strip().lower()
        return resposta == "sim"

    def identificar_fatores_risco(self):
        print("\n🔍 Verificando fatores de risco...")
        perguntas = [
            "A paciente tem hipertensão arterial crônica ou pré-eclâmpsia?",
            "A paciente tem doenças valvares ou cardiopatias congênitas preexistentes?",
            "A paciente tem mais de 35 anos ou está na adolescência?",
            "A paciente está com gravidez múltipla?",
            "A paciente tem IMC > 30 kg/m²?",
            "A paciente usa drogas cardiotóxicas (como cocaína ou β-agonistas)?",
            "A paciente tem baixo nível socioeconômico ou desnutrição?",
            "Há histórico familiar de insuficiência cardíaca ou cardiopatias?",
            "A paciente tem doença renal crônica?",
            "A paciente tem diabetes mellitus gestacional ou tipo 2?"
        ]
        self.fatores_risco = sum(self.obter_resposta(p) for p in perguntas)

    def avaliar_sintomas_chave(self):
        print("\n🩺 Verificando sintomas-chave...")
        perguntas = [
            "A paciente apresenta dispneia progressiva (ao esforço ou deitada)?",
            "A paciente apresenta ortopneia?",
            "A paciente apresenta dispneia paroxística noturna?",  # critério maior
            "A paciente apresenta edema generalizado, pior ao longo do dia?",
            "A paciente tem fadiga intensa, desproporcional à atividade diária?",
            "A paciente apresenta dor torácica?",
            "A paciente apresenta sintomas gastrointestinais como náuseas ou distensão abdominal?"
        ]
        self.sintomas_chave = sum(self.obter_resposta(p) for p in perguntas)

    def avaliar_exames(self):
        print("\n🧪 Avaliação dos critérios diagnósticos de Frammingham:")

        if self.obter_resposta("A paciente apresenta dispneia paroxística noturna?"):
            self.criterios_maiores += 1

        if self.obter_resposta("Houve perda de 4,5 kg após 5 dias de tratamento?"):
            self.criterios_maiores += 1

        if self.obter_resposta("Há turgência jugular patológica?"):
            self.criterios_maiores += 1

        if self.obter_resposta("Há estertores crepitantes à ausculta pulmonar?"):
            self.criterios_maiores += 1

        if self.obter_resposta("A paciente teve episódio de edema agudo de pulmão?"):
            self.criterios_maiores += 1

        if self.obter_resposta("A pressão venosa central (PVC) está > 16 cmH2O?"):
            self.criterios_maiores += 1

        if self.obter_resposta("Há refluxo hepatojugular?"):
            self.criterios_maiores += 1

        if self.obter_resposta("Radiografia mostra aumento da silhueta cardíaca (cardiomegalia)?"):
            self.criterios_maiores += 1

        if self.obter_resposta("Há presença da terceira bulha (B3) na ausculta cardíaca?"):
            self.criterios_maiores += 1

        print("\n📉 Verificando critérios menores...")
        perguntas_menores = [
            "A paciente apresenta tosse noturna?",
            "Há edema bilateral de tornozelos?",
            "A paciente apresenta dispneia aos esforços?",
            "Há hepatomegalia?",
            "A capacidade vital está reduzida a 1/3 do normal?",
            "A paciente apresenta taquicardia > 120 bpm?"
        ]
        self.criterios_menores = sum(self.obter_resposta(p) for p in perguntas_menores)

        print("\n🧬 Exames complementares adicionais:")
        if self.obter_resposta("O ecocardiograma mostra fração de ejeção (FE) < 40%?"):
            print("- FE < 40% indica IC. FE < 30% indica IC grave.")
        if self.obter_resposta("Há disfunção diastólica ou regurgitação valvar ao ecocardiograma?"):
            print("- Indício de comprometimento estrutural cardíaco.")
        if self.obter_resposta("Radiografia mostra congestão pulmonar, linhas de Kerley ou derrame pleural?"):
            print("- Sinais sugestivos de IC.")
        if self.obter_resposta("ECG mostra taquicardia sinusal, arritmias ou sinais de sobrecarga ventricular?"):
            print("- ECG alterado.")
        if self.obter_resposta("BNP > 100 pg/mL?"):
            print("- BNP elevado: compatível com IC.")
        if self.obter_resposta("Creatinina ou ureia estão elevadas?"):
            print("- Avaliar possível hipoperfusão renal ou sobrecarga volêmica.")

    def aplicar_criterios_diagnostico(self):
        print("\n📋 Aplicando critérios diagnósticos (Framingham)...")
        if self.criterios_maiores >= 2 or (self.criterios_maiores >= 1 and self.criterios_menores >= 2):
            print("\n🔴 Diagnóstico de Insuficiência Cardíaca Confirmado!")
            return True
        else:
            print("\n🟢 Diagnóstico de IC NÃO confirmado com os critérios atuais.")
            return False

    def recomendar_tratamento(self):
        print("\n💊 Recomendações terapêuticas:")
        if self.obter_resposta("A paciente apresenta congestão pulmonar?"):
            print("- 💧 Furosemida 20–40 mg IV/VO. Evitar excesso para prevenir hipovolemia.")
        if self.obter_resposta("A pressão arterial está elevada e sem controle adequado?"):
            print("- 💊 Hidroclorotiazida 12,5–25 mg VO (adjuvante no controle da PA).")
        if self.obter_resposta("A paciente apresenta disfunção do VE e está estável hemodinamicamente?"):
            print("- 🫀 Metoprolol 25–100 mg/dia. Observar risco de bradicardia fetal e RCIU.")
        if self.obter_resposta("A paciente tem IC grave ou FE < 30%?"):
            print("- 💉 Nitratos + Hidralazina (iniciar hidralazina 10 mg 3–4x/dia).")
            print("- 💉 Enoxaparina 1 mg/kg 12/12h. Reduzir para 1x/dia se ClCr < 30 mL/min.")
        if self.obter_resposta("A contratilidade do VE está reduzida?"):
            print("- 💊 Digoxina 0,25 mg/dia. Monitorar nível sérico e sinais de toxicidade.")

        print("\n🚫 Medicamentos contraindicados na gestação:")
        print("- IECA, BRA, ARNI")
        print("- Espironolactona, Eplerenona")
        print("- Varfarina")
        print("- Ivabradina, Atenolol")

    def monitoramento_e_parto(self):
        print("\n📈 Monitoramento clínico e cuidados com o parto:")
        print("- Acompanhamento da função cardíaca e renal.")
        print("- Avaliação do bem-estar fetal (movimentos, crescimento).")
        tipo_parto = "cesárea" if self.obter_resposta("A paciente está em IC avançada e instável?") else "parto vaginal"
        print(f"- Tipo de parto preferido: {tipo_parto}.")
        print("- Pós-parto: reavaliar função cardíaca e ajustar tratamento convencional.")

    def executar(self):
        print("\n============================")
        print("💗 Avaliação de Insuficiência Cardíaca na Gestação")
        print("============================")
        self.identificar_fatores_risco()
        self.avaliar_sintomas_chave()
        self.avaliar_exames()
        if self.aplicar_criterios_diagnostico():
            self.recomendar_tratamento()
            self.monitoramento_e_parto()
        print("\n✅ Avaliação finalizada.")

    def iniciar(self):
        self.executar()

class DisseccaoAortica:
    def __init__(self):
        self._diagnostico_final = None
        self.tipo_dissecao = None
        self.complicada = False

    def iniciar(self):
        print("\n🚨 TRIAGEM: DISSECÇÃO AÓRTICA 🚨")

        # Coleta de sintomas e sinais
        sintomas = input("👉 Quais sintomas a paciente apresenta? (Separe por vírgulas - Ex: dor torácica, rasgando, dilacerante, iradiando para dorso, dorsal, síncope, desmaio, náuseas): ").lower()
        sinais = input("🩺 Quais sinais clínicos foram observados? (Ex: sudorese, hipertensão): ").lower()
        fatores_risco = input("⚠️ Há fatores de risco como síndrome de Marfan, hipertensão ou valvopatias? (sim/não): ").strip().lower()
        diferenca_pa = input("📏 Há diferença de PA entre os braços (>20 mmHg)? (sim/não): ").strip().lower()
        hipotensao = input("💥 Há hipotensão ou choque? (sim/não): ").strip().lower()
        hipoperfusao = input("🌡️ Há sinais de hipoperfusão (oligúria, confusão mental)? (sim/não): ").strip().lower()

        # Exames individualizados
        print("\n🔬 RESULTADOS DOS EXAMES:")

        ecg_alterado = input("📉 ECG apresenta alterações específicas? (sim/não): ").strip().lower()
        if ecg_alterado == "sim":
            print("   ⚠️ Lembrar: ECG pode mostrar alterações inespecíficas. Se houver supra de ST, considerar IAM como diagnóstico diferencial.")

        ddimero = input("🧪 D-dímero está elevado? (sim/não): ").strip().lower()
        if ddimero == "sim":
            print("   ⚠️ D-dímero elevado aumenta suspeita, mas é inespecífico.")

        raio_x_alterado = input("🩻 RX de tórax alterado? (mediastino alargado, derrame pleural?) (sim/não): ").strip().lower()
        if raio_x_alterado == "sim":
            print("   ⚠️ RX pode mostrar mediastino alargado ou derrame pleural. Avaliar risco-benefício na gestação.")

        angiotc_realizada = input("📸 Angio-TC foi realizada e confirmou dissecção? (sim/não): ").strip().lower()
        if angiotc_realizada == "sim":
            print("   ✅ Dissecção confirmada na angio-TC (padrão ouro).")

        # Processamento
        self.dor_toracica = "dor torácica" in sintomas
        self.sensacao_rasgando = "rasgando" in sintomas or "dilacerante" in sintomas
        self.irradiacao_dorsal = "irradiando para dorso" in sintomas or "dorsal" in sintomas
        self.sincopes = "síncope" in sintomas or "desmaio" in sintomas
        self.hipotensao_choque = (hipotensao == "sim")
        self.hipoperfusao = (hipoperfusao == "sim")
        self.mediastino_alargado = (raio_x_alterado == "sim")
        self.diferenca_pa_significativa = (diferenca_pa == "sim")
        self.antecedente_marfan_ou_valva = (fatores_risco == "sim")
        self.hipertensao_cronica = "hipertensão" in sinais

        # Diagnóstico
        self._diagnostico_final = self.diagnostico()
        print(f"\n🧠 Diagnóstico provável: {self._diagnostico_final}\n")

        # Definição do tipo de dissecção
        self.definir_tipo_dissecao()

        # Conduta
        self.conduta()

    def diagnostico(self):
        pontos = 0

        if self.dor_toracica and self.sensacao_rasgando:
            pontos += 2
        if self.irradiacao_dorsal or self.sincopes:
            pontos += 1
        if self.hipotensao_choque:
            pontos += 2
        if self.hipoperfusao:
            pontos += 2
        if self.diferenca_pa_significativa:
            pontos += 1
        if self.mediastino_alargado:
            pontos += 1
        if self.antecedente_marfan_ou_valva or self.hipertensao_cronica:
            pontos += 1

        if pontos >= 6:
            return "Alta suspeita de Dissecção Aórtica"
        elif pontos >= 3:
            return "Suspeita moderada de Dissecção Aórtica"
        else:
            return "Baixa suspeita de Dissecção Aórtica"

    def definir_tipo_dissecao(self):
        print("\n📌 Agora vamos classificar a dissecção:")
        print("   ➤ Tipo A: envolve a aorta ascendente, independentemente de onde se inicia.")
        print("   ➤ Tipo B: envolve apenas a aorta descendente, distal à artéria subclávia esquerda.")

        tipo = input("🔎 A dissecção envolve a aorta ascendente? (sim/não): ").strip().lower()
        if tipo == "sim":
            self.tipo_dissecao = "A"
        else:
            self.tipo_dissecao = "B"

        print(f"📍 Tipo de dissecção: Tipo {self.tipo_dissecao}")

        if self.tipo_dissecao == "B":
            complicacoes = input("⚠️ Há complicações como isquemia de órgão, dor incontrolável, expansão do falso lúmen ou ruptura iminente? (sim/não): ").strip().lower()
            self.complicada = (complicacoes == "sim")
            if self.complicada:
                print("💢 Dissecção Tipo B complicada identificada.")
            else:
                print("✅ Dissecção Tipo B não complicada.")
        else:
            print("🚨 Toda dissecção Tipo A é considerada grave e de indicação cirúrgica!")

    def conduta(self):
        print("\n📋 PLANO DE CONDUTA CLÍNICA E OBSTÉTRICA\n")

        if self.tipo_dissecao == "A":
            print("🔴 Dissecção Tipo A:")
            print(" - ➤ Indicação de cirurgia de emergência: substituição da aorta ascendente.")
            print(" - ➤ Iniciar tratamento medicamentoso para estabilização até cirurgia:")
        elif self.tipo_dissecao == "B" and self.complicada:
            print("🟠 Dissecção Tipo B COMPLICADA:")
            print(" - ➤ Avaliação para endoprótese endovascular ou cirurgia.")
            print(" - ➤ Iniciar tratamento medicamentoso de suporte.")
        else:
            print("🟢 Dissecção Tipo B NÃO complicada:")
            print(" - ➤ Tratamento clínico é o de escolha.")

        print("\n💊 Suporte medicamentoso:")
        print(" - Monitoramento hemodinâmico rigoroso.")
        print(" - Controle da pressão arterial e força de cisalhamento:")
        print("   • Metoprolol IV 5mg a cada 5min (1ª escolha).")
        print("   • Se PA >120mmHg: Nitroprussiato de Sódio 0,25 mcg/kg/min IV (máximo 4h).")
        print(" - Controle da dor: Morfina IV 2mg a cada 10min conforme necessário.\n")

        print("🤰 Conduta obstétrica:")
        print(" - Gestante estável com dissecção controlada: postergar parto até ≥34 semanas com monitoramento rigoroso.")
        print(" - Dissecção instável: cesariana de emergência antes da cirurgia cardíaca.")
        print(" - ➤ Via de parto:")
        print("   • Cesárea: preferida para Tipo A ou instabilidade materna.")
        print("   • Parto vaginal: pode ser considerado em Tipo B estável com controle rigoroso da PA.\n")

        print("📈 Acompanhamento:")
        print(" - Seguimento cardiológico e obstétrico intensivo.")
        print(" - Controle rigoroso da PA durante e após a gestação.")
        print(" - Avaliação periódica da aorta no pós-parto com TC ou RM seriadas.")

# --- DICIONÁRIO DE DOENÇAS COM SINAIS/SINTOMAS ASSOCIADOS ---
doencas = {
    "Infarto Agudo do Miocárdio": {
        "classe": EmergenciaCardiovascular,
        "sintomas": [
            "dor torácica", "irradiação da dor", "duração da dor >10min",
            "fatores de risco (HAS, DM, dislipidemia, tabagismo, idade >60)",
            "alívio com nitrato", "náusea", "dispneia"
        ]
    },
    "Distúrbios Hipertensivos da Gestação": {
        "classe": DisturbioHipertensivoGestacao,
        "sintomas": [
            "pa >140/90", "cefaleia frontal ou occipital", "visão embaçada",
            "edema persistente", "dor epigástrica", "náusea e vômito", "convulsões"
        ]
    },
    "Insuficiência Cardíaca": {
        "classe": InsuficienciaCardiaca,
        "sintomas": [
            "dispneia aos esforços", "ortopneia", "dispneia paroxística noturna",
            "edema de membros inferiores", "fadiga intensa", "congestão abdominal", "dor torácica"
        ]
    },
    "Dissecção de Aorta": {
        "classe": DisseccaoAortica,
        "sintomas": [
            "dor torácica lancinante", "dor irradiada para dorso", "sensação de rasgamento",
            "síncope", "tontura", "dispneia importante"
        ]
    }
}

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

# --- SISTEMA DE TRIAGEM INICIAL ---

def triagem_clinica():
    print("\n🩺 Bem-vindo ao Assistente de Avaliação Clínica Inicial!")
    print("Responda às perguntas a seguir com 'sim' ou 'não' 👇\n")

    respostas = {}
    for chave, pergunta in perguntas_avaliacao.items():
        resp = input(f"{pergunta} ").strip().lower()
        respostas[chave] = resp

    # --- ANÁLISE DOS SINTOMAS POR DOENÇA ---
    print("\n📊 Analisando possibilidades com base nos sintomas informados...")

    sugestoes = []
    for nome_doenca, dados in doencas.items():
        sintomas_presentes = [s for s in dados["sintomas"] if respostas.get(s, "não") in ["sim", "s"]]
        if sintomas_presentes:
            sugestoes.append((nome_doenca, len(sintomas_presentes), sintomas_presentes))

    sugestoes.sort(key=lambda x: x[1], reverse=True)

    if not sugestoes:
        print("❌ Nenhuma hipótese clínica sugerida com os sintomas fornecidos.")
        return

    print("\n✅ Hipóteses clínicas sugeridas:")
    for i, (nome, score, sintomas_encontrados) in enumerate(sugestoes, 1):
        print(f"{i}. {nome} ({score} sintomas compatíveis)")
        print(f"   - Sinais/sintomas compatíveis: {', '.join(sintomas_encontrados)}")

    while True:
        print("\nDigite o número da hipótese que deseja iniciar o protocolo.")
        print("Ou digite 0 para encerrar o atendimento.")
        escolha = input(">>> ").strip()
        if escolha == "0":
            print("✅ Encerrando triagem. Até logo!")
            break
        elif escolha.isdigit() and 1 <= int(escolha) <= len(sugestoes):
            nome_escolhido = sugestoes[int(escolha) - 1][0]
            classe_protocolo = doencas[nome_escolhido]["classe"]
            classe_protocolo().iniciar()
        else:
            print("Opção inválida. Tente novamente.")

# --- EXECUÇÃO DO SISTEMA ---
triagem_clinica()