import numpy as np
import control as clt
import matplotlib.pyplot as plt

# Criando a função de trasnferência

G1 = clt.tf([1] , [1, 1])
G2 = clt.tf([1] , [1, 4])
G3 = clt.tf([1] , [1, 7])

G = G1*G2*G3

# Lugar das raízes
clt.rlocus(G)

# Questão 1:
plt.title("Local das Raízes Original")
plt.grid(visible = False)
#plt.show()

# Para um ξ de 0.62 temos: 
# k = 43.88 e s = -1.817 + 2.3j

Q = 0.62
K = 43.88
S = -1.87 + 2.3j

# Questão 2:

g_or = G*K

mg, mf, wcg, wcp = clt.margin(g_or)

print("Margem de ganho: " + str(mg))
print("Margem de fase: " + str(mf))

# MG = 10.027
# MF = 107.635 
# Sistema Estável

# Questão 3:

x, y = clt.step_response(g_or)

plt.figure(2)
plt.plot(x,y)
plt.show()






