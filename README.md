# 002.data-ingestion-lab

## 🎯 Objetivo

Este projeto tem como objetivo desenvolver habilidades práticas em Python para engenharia de dados, simulando um pipeline de dados no modelo Lakehouse (Bronze → Silver → Gold).

---

## 🧱 Estrutura do Projeto

```
002.data-ingestion-lab/
│
├── data/
│   ├── raw/               # Dados brutos (CSV)
│   └── processed/         # Dados tratados (Parquet)
│
├── notebooks/
│   └── 01_data_exploration.ipynb
│
├── src/
│   └── pipeline.py        # Pipeline automatizado
│
├── venv/
├── README.md
└── requirements.txt
```

---

## 🧠 Conceitos Trabalhados

- DataFrame (pandas)
- Data Profiling (`head`, `info`, `describe`)
- Transformação de dados
- Enriquecimento (colunas derivadas)
- Persistência de dados
- Formato Parquet
- Particionamento de dados
- Estrutura Lakehouse
- Pipeline automatizado (ETL)
- Versionamento com Git

---

## 🔄 Pipeline de Dados

### 🔹 Bronze (Raw)

- Fonte: CSV
- Local: `data/raw/transactions.csv`
- Dados imutáveis

---

### 🔹 Silver (Tratado)

Transformações realizadas:

- Conversão de tipos (`data`, `valor`)
- Criação de colunas:
  - `ano`
  - `mes`
  - `tipo_sigla`

---

### 🔹 Gold (Agregado)

- Agregação por tipo de transação
- Uso de `groupby`

---

## 💾 Persistência

### ✔ Parquet particionado

```
data/processed/transactions_partitioned/
  ano=2026/
    mes=1/
      part-xxxx.parquet
```

---

## ⚙️ Execução do Pipeline

```
python src/pipeline.py
```

---

## ⚠️ Problemas enfrentados e soluções

### PyArrow não instala
- Causa: Python 3.14
- Solução: usar Python 3.11

### Engine Parquet não encontrada
- Solução: `pip install pyarrow`

### KeyError (ano, mes)
- Solução: criar colunas antes do particionamento

### FileNotFound
- Solução: corrigir paths ou usar pathlib

### Kernel errado no VSCode
- Solução: selecionar interpreter correto

---

## 🚀 Próximos Passos

- Simular grandes volumes
- Evolução de schema
- Spark / Lakehouse real

---

## 🧑‍💻 Autor

Daniel Skeff
