# Jogo Pedra, Papel ou Tesoura

O jogo "Pedra, Papel e Tesoura" é um jogo simples e popular jogado por duas pessoas. O objetivo do jogo é vencer o adversário escolhendo uma das três opções: pedra, papel ou tesoura. As regras são as seguintes:

Pedra vence tesoura (Pedra quebra a tesoura).
Tesoura vence papel (Tesoura corta o papel).
Papel vence pedra (Papel cobre a pedra).
As duas pessoas jogam simultaneamente, escolhendo uma das três opções. Em seguida, o resultado é determinado de acordo com as regras acima

## Pré-requisitos

- Python 3
- Biblioteca Pyro4

## Como Executar

### Passo 1: executar o pyro4-ns

1. Abra o gerenciador de arquivos e busque por "pyro4-ns.exe" e execute-o

### Passo 2: Iniciando o Servidor do jogo

1. Execute o servidor com o seguinte comando:

```bash
python servidor.py
```

### Passo 3: Iniciando o Cliente

1. Abra outro terminal e navegue até o diretório onde o arquivo `cliente.py` está localizado.

2. Execute o cliente de votação com o seguinte comando:

```bash
python cliente.py
```

### Passo 4: Interagindo com o Sistema

O cliente irá exibir um menu com opções para interagir com o sistema. Você pode:

- Escolher nome de jogador 1
- Realizar jogada
- Escolher nome de jogador 2
- Realizar jogada

