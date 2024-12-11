import operator

# Singleton: Logger para registrar operações e resultados
class Logger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def log(self, message):
        print(f"[LOG]: {message}")


# Factory Method: Criação de operações matemáticas
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


# Strategy: Estratégias de exibição de resultados
class BasicDisplay:
    def display(self, result):
        print(f"Resultado: {result}")


class FancyDisplay:
    def display(self, result):
        print(f"==== Resultado ====")
        print(f">> {result}")
        print(f"==================")


# Observer: Notificação de erros ou eventos importantes
class Observer:
    def notify(self, message):
        print(f"[Notificação]: {message}")


# Decorator: Adicionar logs às operações
class LoggedOperation:
    def __init__(self, operation):
        self.operation = operation
        self.logger = Logger()

    def execute(self, a, b):
        result = self.operation(a, b)
        self.logger.log(f"Operação realizada: {a} {self.operation.__name__} {b} = {result}")
        return result


# Sistema principal
def main():
    logger = Logger()
    observer = Observer()

    # Inicializando o modo de exibição padrão
    display_strategy = BasicDisplay()

    logger.log("Calculadora iniciada.")

    while True:
        print("\n--- Calculadora ---")
        print("Selecione uma opção:")
        print("1. Realizar operação matemática")
        print("2. Alterar modo de exibição")
        print("3. Sair")
        choice = input("> ")

        if choice == "1":
            try:
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
                op = input("Digite a operação (+, -, *, /): ")

                operation = OperationFactory.create_operation(op)
                logged_operation = LoggedOperation(operation)
                result = logged_operation.execute(a, b)

                display_strategy.display(result)

            except ValueError as e:
                observer.notify(f"Erro: {e}")
            except ZeroDivisionError:
                observer.notify("Erro: Divisão por zero não permitida!")

        elif choice == "2":
            print("Selecione o modo de exibição:")
            print("1. Básico")
            print("2. Detalhado")
            mode = input("> ")

            if mode == "1":
                display_strategy = BasicDisplay()
                observer.notify("Modo de exibição alterado para Básico.")
            elif mode == "2":
                display_strategy = FancyDisplay()
                observer.notify("Modo de exibição alterado para Detalhado.")
            else:
                observer.notify("Modo inválido!")

        elif choice == "3":
            logger.log("Calculadora encerrada.")
            break
        else:
            observer.notify("Opção inválida!")


if __name__ == "__main__":
    main()
