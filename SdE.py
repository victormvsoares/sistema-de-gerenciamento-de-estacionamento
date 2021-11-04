def criar_vaga(vagas,nvagas):

    vaga = []
    vaga.append(nvagas)
    vaga.append(0)
    vagas.append(vaga)

    print(f"\nvagas {nvagas} criada\n")

def visualisar_vagas(vagas,nvagas):

    print("")
    for i in range(0,nvagas):

        if vagas[i][1] == 0:

            print(f"vaga {i} desocupada")

        else:

            print(f"vaga {i} cupada pelo carro {vagas[i][2]}")
    print("")

def entrada_de_carro(vagas,nvagas,historico,ncarro):

    marca = input("\ndigite a marca do carro : ")
    modelo = input("digite o modelo do carro : ")
    cor = input("digite a cor do carro : ")
    placa = input("digite a placa : ")
    hora = input("digite a hora de entrada : ")
    print("")
    visualisar_vagas(vagas,nvagas)
    vaga = int(input("\ndigite em que vaga ele ira estacioner : "))
    print("")

    carro = [marca,modelo,cor,placa,vaga,hora]
    historico.append(carro)
    vagas[vaga].append(ncarro)

    vagas[vaga][1]=1

def saida_de_carro(vagas,nvagas,historico):

    hora = input("\ndigite a hora de saida : ")
    visualisar_vagas(vagas,nvagas)
    carro = int(input("digite qual carro estar saindo : "))
    vaga = int(input("digite de que vaga ele estar saindo : "))
    print("")

    historico[carro].append(hora)

    vagas[vaga][1]=0

def visualisar_historico(historico):

    for i in range(0,len(historico)):

        print(f"\no carro de marca {historico[i][0]} modelo {historico[i][1]} cor {historico[i][2]}\n e placa {historico[i][3]} entrou na vaga {historico[i][4]} as {historico[i][5]} horas e saiu as {historico[i][6]} horas\n")

def main():

    vagas = []
    historico = []
    nvagas = 0
    ncarro = 0

    while True:

        print("criar vaga-----------[0]")
        print("visualisar vagas-----[1]")
        print("entrada de carro-----[2]")
        print("saida de carro-------[3]")
        print("visualisar historico-[4]")
        op = int(input("\ndigite uma opção : "))

        if op == 0:
            
            criar_vaga(vagas,nvagas)
            nvagas+=1
        
        elif op == 1:

            visualisar_vagas(vagas,nvagas)

        elif op == 2:

            entrada_de_carro(vagas,nvagas,historico,ncarro)
            ncarro+=1

        elif op == 3:

            saida_de_carro(vagas,nvagas,historico)

        elif op == 4:

            visualisar_historico(historico)

main()