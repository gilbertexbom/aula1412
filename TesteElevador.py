# Teste para a classe Elevador

from Elevador import Elevador
import random
# Criação e instância do objeto da classe elevador
e1 = Elevador(0, True, random.random() * 1000)

# Imprimindo o status do elevador
print('\n\t\t\t -- Elevador no Andar Térreo -- ')
print(e1)


# Subir...
e1.subir(5)

# Imprimindo o status do elevador no 5º andar
print('\n\t\t\t -- Elevador no 5º andar -- ')
print(e1)

# Descer...
e1.descer(0)

# Imprimindo o status do elevador no Térreo
print('\n\t\t\t -- Elevador no Térreo -- ')
print(e1)


