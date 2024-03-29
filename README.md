# IART 2023/2024

## Projetos e Exercícios das Práticas
Este repositório contém o projeto desenvolvido pelo Grupo A1_29 para a disciplina de Inteligência Artificial (IART) durante o ano letivo 2023/2024 na Faculdade de Engenharia da Universidade do Porto (FEUP).

## Membros do Grupo
| Nome             | Número    | E-mail               |
| ---------------- | --------- | -------------------- |
| Francisco Lopes  | 202108796 | up202108796@up.pt    |
| João Fernandes   | 202108044 | up202108044@up.pt    |
| Rui Silveira     | 202108878 | up202108878@up.pt    |

## Descrição do Projeto
O projeto desenvolvido aborda os conceitos e técnicas estudados na disciplina de Inteligência Artificial, com ênfase em jogos e resolução de problemas. Ele consiste na implementação de um jogo de solitário para um jogador, onde diferentes métodos de busca são aplicados para resolver os níveis do jogo. O objetivo é comparar o desempenho desses métodos em termos de qualidade da solução, eficiência e uso de recursos.
Para obter mais informações sobre o enunciado e os detalhes específicos do projeto, consulte a [página da disciplina IART](https://sigarra.up.pt/feup/pt/UCURR_GERAL.FICHA_UC_VIEW?pv_ocorrencia_id=520334).

## Estrutura do Repositório
- **Exercises:** Exercícios práticos da cadeira.
- **Proj1:** Contém o código-fonte do primeiro projeto.
  - **__pycache__:** Diretório que armazena arquivos cache do Python.
  - **Font:** Diretório com fontes utilizadas no projeto.
  - **Images:** Diretório que contém imagens usadas no jogo.
  - **gitignore:** Arquivo de configuração do Git para ignorar determinados arquivos e diretórios.
  - **algorithms.py:** Implementação de algoritmos relevantes para o projeto.
  - **context.pdf:** Ficheiro com o enunciado do Projeto.
  - **display.py:** Módulo responsável pela exibição na interface gráfica.
  - **draw.py:** Módulo para desenho na interface gráfica.
  - **game.py:** Módulo responsável pela lógica do jogo.
  - **gamelogic.py:** Implementação da lógica do jogo.
  - **levels.py:** Definição dos níveis do jogo.
  - **main.py:** Ponto de entrada principal do programa.
  - **utils.py:** Módulo com utilidades diversas.
- **Proj2:** Contém o código-fonte do segundo projeto.
- **README.md:** Documentação principal do projeto.

## Instruções de Execução
1. Certifique-se de ter o Python e o Pygame instalados em seu sistema.
2. Execute o arquivo `main.py` para iniciar o programa.

## Jogo
O jogo [Cogito] é um jogo de solitário para um jogador. O jogo começa com um tabuleiro baralhado e o objetivo é conseguir formar um quadrado ao centro conforme o pedido.

## Setup
Para executar o jogo é necessario ter algumas livrarias do python instaladas. Para tal basta executar o seguinte comando:
```bash
pip install pygame
pip install numpy
```

## Dar início ao jogo
Para dar início ao jogo basta executar o seguinte comando dentro do dirétorio do "Proj1":
```bash
python3 main.py
```



