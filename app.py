"""
EthosAudit - Versão Demonstrativa (PoC)
Foco: Análise Crítica e Verificação de Fatos em Prontuários
"""

import re
import json

# Dicionário estritamente limitado para demonstração pública
REGRAS_DEMO = {
    "manipulador": "Substituir pela descrição factual da conduta clínica observada.",
    "rebelde": "Termo inadequado e subjetivo para evolução técnica."
}

class AuditorDemonstrativo:
    def __init__(self):
        self.regras = REGRAS_DEMO

    def analisar(self, texto: str):
        alertas = []
        texto_min = texto.lower()

        for termo, recomendacao in self.regras.items():
            padrao = rf"\b{termo}\b"
            if re.search(padrao, texto_min):
                alertas.append({
                    "termo": termo,
                    "classe": "Julgamento de Valor",
                    "diretriz": recomendacao
                })
        
        return {
            "status_auditoria": "Revisão Requerida" if alertas else "Conforme",
            "alertas_identificados": alertas
        }

if __name__ == "__main__":
    auditor = AuditorDemonstrativo()
    exemplo = "Paciente apresentou-se de forma manipuladora e rebelde."
    print(json.dumps(auditor.analisar(exemplo), indent=4, ensure_ascii=False))