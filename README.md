# Design Petterns

# Calculadora em Python com Design Patterns

Este projeto é uma calculadora de linha de comando (CMD) criada em Python para demonstrar a aplicação de **5 tipos de Design Patterns**. Ele é simples, funcional e ideal para quem está estudando padrões de projeto e quer ver exemplos práticos em um contexto real.

## 🎯 Objetivo

O objetivo deste projeto é mostrar como implementar padrões de design amplamente utilizados na engenharia de software, aplicando-os a uma calculadora. Cada padrão foi usado para resolver problemas específicos no design do programa, melhorando a organização, reutilização de código e escalabilidade.

---

### 1. **Singleton (Logger)**
- **Classe:** `Logger`
- **Descrição:** O padrão Singleton garante que a classe `Logger` tenha apenas uma única instância em todo o programa. Isso é útil para centralizar o registro de mensagens no sistema.
- **Localização no código:**
  ```python
  class Logger:
      _instance = None

      def __new__(cls, *args, **kwargs):
          if not cls._instance:
              cls._instance = super(Logger, cls).__new__(cls)
          return cls._instance
  ```
- **Uso:** Em `Logger.log`, todas as mensagens de log são centralizadas, evitando a criação de múltiplas instâncias desnecessárias.

---

### 2. **Factory Method (OperationFactory)**
- **Classe:** `OperationFactory`
- **Descrição:** O Factory Method é usado para criar objetos de diferentes operações matemáticas (`+`, `-`, `*`, `/`). Ele encapsula a lógica de criação de objetos, retornando a função de operação correspondente.
- **Localização no código:**
  ```python
  class OperationFactory:
      @staticmethod
      def create_operation(op):
          operations = {
              "+": operator.add,
              "-": operator.sub,
              "*": operator.mul,
              "/": operator.truediv,
          }
          if op in operations:
              return operations[op]
          else:
              raise ValueError("Operação inválida!")
  ```
- **Uso:** Em `main`, ele cria a operação correspondente com base na entrada do usuário:
  ```python
  operation = OperationFactory.create_operation(op)
  ```

---

### 3. **Strategy (Exibição de resultados)**
- **Classes:** `BasicDisplay`, `FancyDisplay`
- **Descrição:** O padrão Strategy define diferentes maneiras de exibir os resultados da calculadora. O comportamento pode ser alterado dinamicamente durante a execução.
- **Localização no código:**
  ```python
  class BasicDisplay:
      def display(self, result):
          print(f"Resultado: {result}")

  class FancyDisplay:
      def display(self, result):
          print(f"==== Resultado ====")
          print(f">> {result}")
          print(f"==================")
  ```
- **Uso:** O usuário pode alternar entre modos de exibição:
  ```python
  display_strategy = BasicDisplay()  # Modo padrão
  display_strategy = FancyDisplay()  # Alterado pelo usuário
  ```

---

### 4. **Observer (Notificação de eventos)**
- **Classe:** `Observer`
- **Descrição:** O padrão Observer é usado para notificar eventos importantes ou erros no programa. Ele separa a lógica de notificação do restante do sistema.
- **Localização no código:**
  ```python
  class Observer:
      def notify(self, message):
          print(f"[Notificação]: {message}")
  ```
- **Uso:** É usado para exibir mensagens de erro ou notificações:
  ```python
  observer.notify("Erro: Divisão por zero não permitida!")
  observer.notify("Modo de exibição alterado para Detalhado.")
  ```

---

### 5. **Decorator (LoggedOperation)**
- **Classe:** `LoggedOperation`
- **Descrição:** O padrão Decorator é usado para adicionar funcionalidades extras (neste caso, logs) à execução das operações matemáticas, sem modificar diretamente as funções de operação.
- **Localização no código:**
  ```python
  class LoggedOperation:
      def __init__(self, operation):
          self.operation = operation
          self.logger = Logger()

      def execute(self, a, b):
          result = self.operation(a, b)
          self.logger.log(f"Operação realizada: {a} {self.operation.__name__} {b} = {result}")
          return result
  ```
- **Uso:** Envolve as operações para registrar automaticamente as informações de cada cálculo:
  ```python
  logged_operation = LoggedOperation(operation)
  result = logged_operation.execute(a, b)
  ```

---
