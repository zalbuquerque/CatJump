# 😺 Cat Jump 😺

Projeto de jogo 2D desenvolvido em **Python** com **Pygame**, criado e executado no **PyCharm**.

O **Cat Jump** é um jogo no estilo **endless runner**, em que o jogador controla um gatinho que precisa **pular obstáculos** e **coletar moedas** para alcançar a maior pontuação possível. O projeto também possui **menu inicial**, **tela de game over** e **ranking Top 10** salvo localmente.

---

## Sobre o projeto

Este projeto foi desenvolvido com foco em praticar conceitos de:

- programação orientada a objetos;
- organização de projeto em múltiplos arquivos;
- manipulação de imagens, sons e eventos com Pygame;
- lógica de movimentação e colisão;
- persistência de dados com SQLite;
- estruturação de um jogo 2D simples, mas funcional.

Além da parte técnica, o projeto também explora elementos visuais e sonoros para tornar a experiência mais completa, como **cenário com múltiplas camadas**, **músicas para menu e gameplay** e **tela de pontuação**.

---

## Funcionalidades

- Menu inicial com opções de:
  - **Jogar**
  - **Score**
  - **Sair**
<img width="450" height="250" alt="image" src="https://github.com/user-attachments/assets/24226efa-649f-4db6-9e69-cc6feb87bda5" />

- Personagem principal com sistema de pulo
- Obstáculos gerados dinamicamente
- Moedas colecionáveis
- Sistema de pontuação por:
  - distância percorrida
  - moedas coletadas
<img width="450" height="250" alt="image" src="https://github.com/user-attachments/assets/311eaf25-005e-4893-b946-d8a44f4bab80" />

- Tela de fim de jogo
<img width="450" height="250" alt="image" src="https://github.com/user-attachments/assets/97cd2ddf-924a-4c4b-adbc-508668df3d44" />

- Salvamento local de score com nome do jogador
- Exibição do **Top 10 scores**

- Música e imagens para diferentes telas do jogo
<img width="450" height="250" alt="image" src="https://github.com/user-attachments/assets/90936677-217e-40b4-8038-ebf3efd8f901" />

---

## Tecnologias utilizadas

- **Python**
- **Pygame**
- **SQLite**
- **PyCharm** como IDE de desenvolvimento

---
## Requisitos

Antes de executar o projeto, você precisa ter instalado:

- Python 3
- Pygame

As dependências estão no arquivo ```requirements.txt```.

# Instalação
## 1. Clonar o repositório

```git clone https://github.com/zalbuquerque/CatJump.git```

## 2. Acessar a pasta do projeto

```cd CatJump```

## 3. Instalar as dependências

```pip install -r requirements.txt```

## Como gerar o executável do projeto

Para transformar o jogo em um executável `.exe` no Windows, uma opção prática é usar o **PyInstaller**. Ele empacota o script principal junto com o interpretador Python e os arquivos necessários para rodar a aplicação.

### 1. Instalar o PyInstaller

```
pip install pyinstaller
```
### 2. Gerar o executável
No terminal, dentro da pasta do projeto, execute:

```
pyinstaller --noconfirm --windowed --onedir --name CatJump --add-data "asset;asset" --add-data "DBScore;." main.py
```
O que esse comando faz

```--windowed``` -> gera uma aplicação gráfica sem abrir o terminal junto no Windows.

```--onedir``` -> cria uma pasta com o executável e todos os arquivos necessários. Essa abordagem costuma ser mais adequada para jogos com imagens, sons e outros assets. O PyInstaller também suporta empacotar em arquivo único, mas a própria documentação alerta que combinar --onefile com --windowed pode ser ineficiente.

--name CatJump
define o nome final do executável.

```--add-data "asset;asset"``` -> inclui a pasta de imagens e sons dentro da build.

```--add-data "DBScore;."``` -> inclui o arquivo de banco de dados usado para armazenar os scores.

## 3. Onde o executável será criado

Após o processo, o PyInstaller gera principalmente estas pastas e arquivos:

```build/```

```dist/```

```CatJump.spec```


O executável ficará em:

```dist/CatJump/CatJump.exe```

O PyInstaller cria a pasta dist para o aplicativo final e também gera um arquivo .spec, que pode ser reutilizado para builds futuras.

## Gerando executável com ícone

Se você tiver um arquivo ```.ico```, pode usar:

```pyinstaller --noconfirm --windowed --onedir --name CatJump --icon icon.ico --add-data "asset;asset" --add-data "DBScore;." main.py```

O parâmetro ```--icon``` aplica um ícone personalizado ao executável no Windows.
