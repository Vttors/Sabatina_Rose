import numpy as np
import control as clt
import matplotlib.pyplot as plt

figure = 1

def local_das_raizes(sis):
    global figure
    plt.figure(figure)
    figure += 1
    clt.rlocus(sis)
    plt.title("Local das Raízes Original")
    plt.grid(visible = False)

def margem_de_ganho_e_fase(sis):

    mg, mf, wcg, wcp = clt.margin(sis)

    print("Margem de ganho: " + str(mg))
    print("Margem de fase: " + str(mf))
    if(mf >= 0 and mg >= 0):
        print("O sistema é estável")
    else:
        print("O sistema não é estável")

def resposta_ao_degrau(sis):
    global figure
    sis_fechado = clt.feedback(sis)
    y, x = clt.step_response(sis_fechado)

    plt.figure(figure)
    figure +=1
    plt.title("Resposta ao Degrau")
    degrau = np.ones(len(x))
    plt.plot(y,x,y,degrau)






# Criando a função de trasnferência

G1 = clt.tf([1] , [1, 1])
G2 = clt.tf([1] , [1, 4])
G3 = clt.tf([1] , [1, 7])

G = G1*G2*G3
print("Sistema: " + str(G))


# Questão 1:
print("Questão 1: Figura " + str(figure))
local_das_raizes(G)

print("Para um ξ de 0.62 temos:  k = 43.88 e s = -1.817 + 2.3j")

q = 0.62
k = 43.88
s = -1.87 + 2.3j

# Questão 2:
print("Questão 2:")
margem_de_ganho_e_fase(G*k)
# MG = 10.027
# MF = 107.635 
# Sistema Estável

# Questão 3:
print("Questão 3: Gráfico " + str(figure))
resposta_ao_degrau(G*k)

# Questão 4:

G4 = clt.tf([1,3],[1])
G_ZERO3 = G * G4
print("Questão 4:")
print("Sistema: " + str(G_ZERO3))

# Questão 4.1

print("Questão 4.1: Figura " + str(figure))

local_das_raizes(G_ZERO3)

print("Para um ξ de 0.62 temos:  k = 41.9 e s = -4.609 + 5.832j")

q = 0.62
k = 41.9
s = -4.609 + 5.832j

# Questão 4.2:

print("Questão 4.2: ")
margem_de_ganho_e_fase(G_ZERO3*k)

# Questão 4.3:
print("Questão 4.3: Gráfico " + str(figure))
resposta_ao_degrau(G_ZERO3*k)


plt.show()



