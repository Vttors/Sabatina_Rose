import numpy as np
import control as clt
import matplotlib.pyplot as plt

figure = 1

def local_das_raizes(sis,questao):
    global figure
    plt.figure(figure)
    figure += 1
    clt.rlocus(sis)
    plt.title("Local das Raízes - Questão " + str(questao))
    plt.grid(visible = False)

def margem_de_ganho_e_fase(sis):

    mg, mf, wcg, wcp = clt.margin(sis)

    print("Margem de ganho: " + str(mg))
    print("Margem de fase: " + str(mf))
    if(mf >= 0 and mg >= 0):
        print("O sistema é estável")
    else:
        print("O sistema não é estável")

def resposta_ao_degrau(sis, questao):
    global figure
    sis_fechado = clt.feedback(sis)
    y, x = clt.step_response(sis_fechado)

    plt.figure(figure)
    figure +=1
    plt.title("Resposta ao Degrau - Questão " + str(questao))
    degrau = np.ones(len(x))
    plt.plot(y,x,y,degrau)

# Criando a função de trasnferência

G1 = clt.tf([1] , [1, 1])
G2 = clt.tf([1] , [1, 4])
G3 = clt.tf([1] , [1, 7])

G = G1*G2*G3
print("Sistema: " + str(G))

def Questao(questao,zero,k,s):
    # Adicionando o zero
    Z1 = clt.tf([1,zero],[1])
    SISTEMA = G * Z1

    print("Questão "+ str(questao) + ":")
    print("Sistema: " + str(SISTEMA))
    print("Questão " + str(questao) + ".1: Figura " + str(figure))
    local_das_raizes(SISTEMA,questao)
    print("Para um ξ de 0.62 temos:  k = " + str(k) + " e s = " + str(s))
    print("Questão " + str(questao) + ".2: ")
    margem_de_ganho_e_fase(SISTEMA*k)
    print("Questão " + str(questao) + ".3: Gráfico " + str(figure))
    resposta_ao_degrau(SISTEMA*k,questao)



# Questão 1:
print("Questão 1: Figura " + str(figure))
local_das_raizes(G,1)

print("Para um ξ de 0.62 temos:  k = 43.88 e s = -1.817 + 2.3j")

k = 43.88

# Questão 2:
print("Questão 2:")
margem_de_ganho_e_fase(G*k)

# Questão 3:
print("Questão 3: Gráfico " + str(figure))
resposta_ao_degrau(G*k,3)

# Questão 4:
Questao(4,3,41.9, -4.609 + 5.832j)
# Questão 5:
Questao(5, 15, 3.765, -2.02 +2.556j)
# Questão 6:
Questao(6, 30, 1.644, -1.905 + 2.411j)
# Questão 7:
Questao(7, 40, 1.196, -1.881 + 2.381j)


plt.show()
