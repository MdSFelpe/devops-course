# Pipeline de Segurança DevSecOps e Shift-Left

## 1. Sobre o Projeto
Este projeto consiste na automação de uma esteira de segurança CI/CD integrada ao GitHub Actions para uma API desenvolvida em Python. O objetivo principal é implementar práticas de **DevSecOps** e o conceito de **Shift-Left Security**, garantindo que validações de infraestrutura como código (IaC), código-fonte (SAST), dependências (SCA) e aplicação em execução (DAST) ocorram nas fases iniciais do desenvolvimento, bloqueando entregas e deploys inseguros.

---

## 2. Ferramentas Utilizadas
* **GitHub Actions**: Orquestrador de CI/CD e automação do pipeline.
* **Terraform & Trivy**: Validação de sintaxe e análise de segurança de Infraestrutura como Código (IaC).
* **SonarQube Cloud**: Análise Estática de Segurança de Aplicação (SAST) e qualidade de código.
* **GitHub Dependency Review**: Análise de Segurança de Componentes e Dependências (SCA).
* **OWASP ZAP (ZAProxy)**: Análise Dinâmica de Segurança de Aplicação (DAST).
* **Docker & GitHub Container Registry (GHCR)**: Containerização e armazenamento da imagem do deploy simulado.

---

## 3. Tipo de Análise

| Ferramenta | Tipo de Análise | Descrição |
| :--- | :--- | :--- |
| **Trivy** | IaC Security Scan | Analisa configurações do Terraform buscando regras de segurança permissivas ou falhas de IaC. |
| **SonarQube Cloud** | SAST | Examina o código Python em busca de vulnerabilidades, *code smells* e segredos expostos. |
| **Dependency Review** | SCA | Verifica pacotes e bibliotecas terceirizadas contra bancos de dados de vulnerabilidades conhecidas (CVEs). |
| **OWASP ZAP** | DAST | Interage com a aplicação Python rodando via Docker para identificar vulnerabilidades em tempo de execução. |

---

## 4. Funcionamento da Pipeline

### Fluxo da Solução

```text
Push / Pull Request
       ↓
    Pipeline
       ↓
Terraform (IaC) Scan
       ↓
  SonarQube (SAST)
       ↓
Dependency Review (SCA)
       ↓
  OWASP ZAP (DAST)
       ↓

````


## Detalhes de Execução
## O que dispara a pipeline?

O pipeline é acionado automaticamente em qualquer evento de push ou pull_request direcionado às branches main ou master.

## Em qual etapa ocorre a análise?

As análises executam sequencialmente no ambiente isolado do GitHub Actions:

IaC Scan (Trivy) valida os arquivos .tf.

SAST (SonarQube Cloud) inspeciona o código Python.

SCA (GitHub Dependency Review) roda em Pull Requests para checar dependências vulneráveis.

DAST (OWASP ZAP) executa os testes dinâmicos com a aplicação ativa via container Docker.

## O que acontece quando são encontrados problemas?

A etapa final de Continuous Deployment (CD) possui dependência direta (needs) de todas as etapas de análise anteriores. Se qualquer vulnerabilidade de severidade alta ou crítica for detectada, a esteira é interrompida imediatamente, impedindo a criação/push da imagem Docker e bloqueando o deploy de código inseguro.

## 5. Resultados e Evidências
Execução da Pipeline
Execução automatizada no GitHub Actions demonstrando a aprovação das etapas de segurança e liberação do deploy:
<img width="1519" height="441" alt="Pipeline" src="https://github.com/user-attachments/assets/881462fd-90e4-4678-9f0c-53dcb840b207" />





SAST (SonarQube Cloud)
Resultado da análise estática demonstrando o status de aprovação do Quality Gate:
<img width="1853" height="913" alt="SONAQUBE" src="https://github.com/user-attachments/assets/092a40bc-942c-4420-ae58-9469aedba04a" />
<img width="1507" height="483" alt="Captura de tela 2026-09-12 135030" src="https://github.com/user-attachments/assets/2ff245a0-3e21-46da-8b33-76114af1f4da" />


## 6. Conclusão
A implementação desta esteira aplica o conceito de Shift-Left Security, movendo as verificações de segurança para o início do ciclo de vida de desenvolvimento de software. Em vez de identificar falhas apenas na fase final ou em produção, as análises automatizadas integradas ao DevSecOps atuam como travas de qualidade contínuas, reduzindo custos de correção e mitigando riscos operacionais.







