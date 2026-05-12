# 🗺️ Mapbox 3D Matrix & Route Manager

Este projeto é uma aplicação **Full Stack** profissional desenvolvida para demonstrar a integração avançada com a **Mapbox Standard API**. O sistema permite a criação de rotas dinâmicas em um ambiente 3D, com cálculos de logística e funcionalidades de partilha.

## 🚀 Funcionalidades Principais

- **Visualização 3D de Nova Geração:** Utiliza o estilo *Mapbox Standard* com prédios 3D, iluminação solar dinâmica e sombras em tempo real.
- **Gestão de Múltiplos Pontos:** Permite marcar diversos pontos no mapa de forma sequencial.
- **Identificação de Localização:** Input para dar nomes personalizados a cada marcador (ex: "Sede", "Cliente B", "Ponto de Descarga").
- **Cálculo de Matriz Logística:** Integração com a *Directions Matrix API* para obter tempos de viagem e distâncias exatas entre todos os pontos clicados.
- **Fluxo de Confirmação:** Opções para **Salvar**, **Continuar Editando** ou **Apagar** as marcações antes de registar os dados.
- **Histórico Estruturado (JSON):** Gravação automática de todas as consultas em um banco de dados local `historico_rotas.json`, incluindo carimbo de data/hora e metadados.
- **Link de Partilha Universal:** Geração de uma URL formatada para o **Google Maps**, permitindo enviar a rota completa para amigos ou motoristas.

## 🛠️ Tecnologias Utilizadas

- **Back-end:** Python 3 + Flask
- **Front-end:** JavaScript (Mapbox GL JS v3), HTML5, CSS3
- **Bibliotecas Python:** `requests`, `python-dotenv`

## 🔧 Como Instalar e Rodar

1. **Clone este repositório:**
   ```bash
   git clone [https://github.com/PedroHSN98/Meu_Mapa_Projeto.git](https://github.com/PedroHSN98/Meu_Mapa_Projeto.git)
   cd Meu_Mapa_Projeto

2. **Instale as dependências:**
   ```bash
   pip install flask requests python-dotenv

3. **Configure o seu Token:**
  - Crie um ficheiro .env na raiz do projeto.
  - Adicione a sua chave: MAPBOX_TOKEN=sua_chave_aqui

4. **Execute a aplicação:**
   ```bash
   python app.py

5. **Entre pelo url navegador**:http://127.0.0.1:5000

   
   
