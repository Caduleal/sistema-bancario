# Sistema Bancário em Python

Este projeto é uma implementação básica de um sistema bancário em Python, que permite aos clientes abrir contas, depositar, sacar dinheiro e visualizar o extrato. Ele também suporta contas correntes e contas poupança com cálculo de juros.

## Estrutura do Código

O código está estruturado em várias classes para representar clientes e contas bancárias:

- `Cliente`: Representa um cliente com nome e CPF, e permite abrir contas.
- `Conta`: Classe base para diferentes tipos de contas bancárias.
- `ContaCorrente`: Subclasse de `Conta`, representa uma conta corrente.
- `ContaPoupanca`: Subclasse de `Conta`, representa uma conta poupança, com cálculo de juros.

### Classes e Métodos

#### Cliente

- `__init__(self, nome, cpf)`: Inicializa um cliente com nome e CPF.
- `abrir_conta(self, tipo_conta, saldo_inicial)`: Abre uma conta do tipo especificado (corrente ou poupança) com saldo inicial.
- `__str__(self)`: Retorna uma string representando o cliente.

#### Conta

- `__init__(self, saldo_inicial=0)`: Inicializa uma conta com saldo inicial.
- `depositar(self, valor)`: Deposita um valor na conta.
- `sacar(self, valor)`: Saca um valor da conta.
- `_registrar_transacao(self, descricao)`: Método privado para registrar transações.
- `extrato(self)`: Exibe o extrato da conta.

#### ContaCorrente

- `__init__(self, saldo_inicial=0)`: Inicializa uma conta corrente com saldo inicial.
- `__str__(self)`: Retorna uma string representando a conta corrente.

#### ContaPoupanca

- `__init__(self, saldo_inicial=0)`: Inicializa uma conta poupança com saldo inicial.
- `calcular_juros(self)`: Calcula e credita juros na conta poupança.
- `__str__(self)`: Retorna uma string representando a conta poupança.

## Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone este repositório.
3. Execute o script principal:

```sh
python SistemaBancario.py