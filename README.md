# Pipeline de Segurança DevSecOps e Shift-Left

## 1. Sobre o Projeto
Este projeto consiste na automação de uma esteira de segurança CI/CD integrada ao GitHub Actions para uma API desenvolvida em Python. O objetivo principal é implementar práticas de **DevSecOps** e o conceito de **Shift-Left Security**, garantindo que validações de infraestrutura como código (IaC), código-fonte (SAST), dependências (SCA) e aplicação em execução (DAST) ocorram nas fases iniciais do desenvolvimento, bloqueando automações e deploys inseguros.

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
Deploy Simulado (CD)
