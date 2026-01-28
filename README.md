# 🎵 Classificador de Gênero Musical

Este projeto é uma aplicação web que utiliza **Machine Learning** para prever o **gênero musical** a partir da letra de uma música. A solução é composta por um **backend em FastAPI** responsável pela inferência do modelo treinado e um **frontend em HTML + JavaScript** para interação com o usuário e visualização de gráficos.

---

## 🚀 Funcionalidades

* Envio de letra de música para análise
* Predição automática do gênero musical
* API REST para consumo do modelo de Machine Learning
* Interface web simples e intuitiva
* Visualização gráfica de dados com Chart.js

---

## 🧠 Tecnologias Utilizadas

### Backend

* **Python**
* **FastAPI**
* **Uvicorn**
* **Scikit-learn**
* **Joblib**
* **Pandas**
* **Pydantic**
* **CORS Middleware**

### Frontend

* **HTML5**
* **CSS3**
* **JavaScript**
* **Chart.js**

---

## 🗂 Estrutura do Projeto

```
├── main.py                  # API FastAPI e inferência do modelo
├── index.html               # Interface web do usuário
├── model_training.py        # Script de treinamento do modelo de ML
├── dataset_genero_musical.xlsx # Dataset de letras e gêneros musicais
├── model.joblib             # Modelo de Machine Learning treinado
├── vectorizer.joblib        # Vetorizador de texto
├── requirements.txt         # Dependências do projeto
├── __pycache__/             # Cache gerado automaticamente pelo Python
```

├── main.py          # API FastAPI e carregamento do modelo
├── index.html       # Interface web do usuário
├── model.joblib     # Modelo de Machine Learning treinado
├── vectorizer.joblib# Vetorizador de texto

````

---

## ⚙️ Backend (FastAPI)

O backend expõe um endpoint `/predict` que recebe uma letra de música em formato JSON e retorna o gênero musical previsto pelo modelo.

### Endpoint

- **POST** `/predict`

#### Exemplo de requisição:
```json
{
  "letra": "Letra da música aqui"
}
````

#### Exemplo de resposta:

```json
{
  "genero": "Sertanejo"
}
```

O servidor roda localmente em:

```
http://localhost:8080
```

---

## 🖥 Frontend

A interface permite ao usuário:

* Inserir a letra da música
* Enviar para o backend
* Visualizar o gênero previsto
* Ver gráficos ilustrativos sobre gêneros musicais e popularidade ao longo dos anos

A comunicação com a API é feita via `fetch` usando JSON.

---

## ▶️ Como Executar o Projeto

### 1️⃣ Backend

Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a API:

```bash
python main.py
```

O backend ficará disponível em:

```
http://localhost:8080
```

### 2️⃣ Frontend

Abra o arquivo `index.html` diretamente no navegador.

> ⚠️ Certifique-se de que o backend esteja rodando antes de enviar a letra da música.

---

## ## 📊 Observações

* O dataset está armazenado em formato Excel (`.xlsx`) e é utilizado apenas no treinamento do modelo.
* A pasta `__pycache__` é gerada automaticamente pelo Python e não deve ser versionada no Git.
* A precisão exibida na interface é ilustrativa.
* Os gráficos apresentados no frontend utilizam dados estáticos para fins de visualização.
* O modelo de Machine Learning é treinado separadamente e carregado na API via arquivos `.joblib`.

---

📌 *Este README será atualizado conforme novos arquivos ou funcionalidades forem adicionados ao projeto.*
