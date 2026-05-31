import re
import json

# =====================================================================
# DEMONSTRAÇÃO PÚBLICA: EXEMPLO DE PARSE DE CONFORMIDADE ÉTICA
# (Versão comercial completa e dicionários forenses são privados)
# =====================================================================

TERMOS_DEMONSTRACAO = {
    "manipulador": "Substituir pela descrição factual do comportamento do paciente.",
    "rebelde": "Termo inadequado e infantilizante para evolução clínica.",
    "muito": "Termo vago. Quantificar a ocorrência dos sintomas com dados objetivos."
}

class ClinicaAuditorPOC:
    def __init__(self):
        self.regras = TERMOS_DEMONSTRACAO

    def auditar_texto(self, texto_prontuario):
        alertas_encontrados = []
        texto_minusculo = texto_prontuario.lower()

        for termo, recomendacao in self.regras.items():
            padrao = rf"\b{termo}\b"
            ocorrencias = len(re.findall(padrao, texto_minusculo))
            if ocorrencias > 0:
                alertas_encontrados.append({
                    "termo_identificado": termo,
                    "categoria": "Indicador de Viés / Subjetividade",
                    "o_que_fazer": recomendacao
                })

        status = "Aprovado" if len(alertas_encontrados) == 0 else "Necessita Revisão"
        return {"status_da_auditoria": status, "alertas": alertas_encontrados}

if __name__ == "__main__":
    auditor = ClinicaAuditorPOC()
    # Um teste simples apenas para demonstrar a execução do script
    exemplo = "O paciente permaneceu muito rebelde durante a sessão."
    resultado = auditor.auditar_texto(exemplo)
    print(json.dumps(resultado, indent=4, ensure_ascii=False))