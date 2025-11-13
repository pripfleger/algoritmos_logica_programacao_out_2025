#1 Sistema de Controle de Qualidade Industrial

##1.1 Descrição

Sistema desenvolvido em Python para cadastro, classificação e armazenamento de peças industriais.
O sistema realiza inspeção automatizada baseada em critérios de peso, cor e comprimento, organizando peças aprovadas em caixas de 10 unidades.

##1.2 Funcionalidades

###1.2.1 Menu Principal
1. **Cadastrar nova peça** - Registra peças com suas especificações
2. **Listar peças aprovadas/reprovadas** - Visualiza todas as peças cadastradas
3. **Remover peça cadastrada** - Exclui peças do sistema
4. **Listar caixas** - Mostra caixas abertas e fechadas
5. **Gerar relatório** - Relatórios detalhados de produção
6. **Sair do sistema** - Encerra o programa

###1.2.2 Sistema de Relatórios
1. **Peças aprovadas** - Lista todas as peças que passaram na inspeção
2. **Peças reprovadas** - Lista peças rejeitadas com motivos detalhados
3. **Quantidade total de caixas** - Estatísticas de armazenamento
4. **Voltar** - Retorna ao menu principal

##1.3 Critérios de Aprovação

Uma peça é **APROVADA** quando atende **TODOS** os seguintes critérios:

|    Critério     | Especificação |
|------=======----|---------------|
|    **Peso**     |   95g a 105g  |
|     **Cor**     | Azul ou Verde |
| **Comprimento** |  10cm a 20cm  |

Qualquer desvio desses parâmetros resulta em **REPROVAÇÃO**

##1.4 Sistema de Armazenamento

- Apenas peças **APROVADAS** são armazenadas em caixas
- Cada caixa comporta exatamente **10 peças**
- Caixa fecha automaticamente ao atingir 10 unidades
- Nova caixa é criada automaticamente quando necessário
- Peças reprovadas **NÃO** são armazenadas

##1.5 Como Usar

###1.5.1 Pré-requisitos

```bash
# Python 3.6 ou superior
python --version

# Instalar dependência colorama
pip install colorama
```

###1.5.2 Executando o Sistema

```bash
# Clone ou baixe o arquivo
python trabalhoindustria.py
```

##1.6 Interface

O sistema utiliza cores para melhor visualização:

- **Azul** - Menus e títulos
- **Amarelo** - Informações e listagens
- **Verde** - Operações bem-sucedidas
- **Vermelho** - Erros e reprovações

##1.7 Estrutura de Dados

```python
# Dicionário de Peças
pecas = {
    0: {
        "Nome": "Peça A",
        "Peso": 100.5,
        "Cor": "azul",
        "Comprimento": 15.2,
        "Status": "Aprovado"
    }
}

# Dicionário de Caixas
caixas = {
    1: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],  # Caixa fechada (10 peças)
    2: [10, 11, 12]                      # Caixa aberta (3 peças)
}
```

##1.8 Exemplos de Uso

###1.8.1 Exemplo 1: Peça Aprovada
```
Qual o nome da peça? Engrenagem X
Qual o peso da peça? 100
Qual a cor da peça? azul
Qual o comprimento da peça? 15

Peça armazenada com sucesso na caixa 1!
```

###1.8.2 Exemplo 2: Peça Reprovada
```
Qual o nome da peça? Eixo Y
Qual o peso da peça? 120
Qual a cor da peça? vermelho
Qual o comprimento da peça? 25

Peça reprovada, não entra na caixa!!!

Motivos:
 • Peso fora do padrão
 • Cor fora do padrão
 • Comprimento fora do padrão
```

##1.9 Funcionalidades Técnicas

###1.9.1 Validação Automática
- ✓ Verificação de entrada de dados
- ✓ Tratamento de exceções
- ✓ Conversão automática de tipos
- ✓ Normalização de cores (minúsculas)

###1.9.2 Gerenciamento Inteligente
- ✓ IDs únicos auto-incrementais
- ✓ Rastreamento de peças em caixas
- ✓ Remoção segura (limpa peças e caixas)
- ✓ Relatórios com análise de motivos

###1.9.3 Interface Amigável
- ✓ Limpeza automática de tela
- ✓ Mensagens coloridas contextuais
- ✓ Navegação intuitiva
- ✓ Confirmações de ações

##1.10 Relatórios Disponíveis

###1.10.1 Relatório de Peças Aprovadas
- Lista completa de peças que passaram no controle
- Informações detalhadas de cada peça
- Quantidade total

###1.10.2 Relatório de Peças Reprovadas
- Lista de peças rejeitadas
- **Motivos específicos** de cada reprovação:
  - Peso fora do padrão (95-105g)
  - Cor incorreta (não azul/verde)
  - Comprimento inadequado (10-20cm)

###1.10.3 Relatório de Caixas
- Total de caixas utilizadas
- Status de cada caixa (aberta/fechada)
- IDs das peças em cada caixa

##1.11 Requisitos do Sistema

- **Python:** 3.6+
- **Bibliotecas:**
  - `colorama` - Interface colorida
  - `os` - Manipulação de sistema (built-in)

##1.12 Tratamento de Erros

O sistema possui tratamento robusto de erros para:
- Entrada de dados inválidos
- IDs inexistentes
- Opções de menu inválidas
- Exceções gerais do sistema

##1.13 Licença

Este projeto é de código aberto e pode ser usado livremente para fins educacionais.

---
*Versão 1.0 - 2025*