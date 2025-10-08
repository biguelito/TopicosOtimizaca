import numpy as np
import math

# Funcao para gerar entradas aleatorias para testar o codigo
def read_input(size : int):
    hotels = [(f"hotel_{i}", int(np.random.choice(range(1, 5)))) for i in range(size)]
    return hotels

# Possivel otimizacao da escolha do hotel baseado no problema da secretaria
# A otimizacao consiste em utilizar parte inicial das entradas do problema como um grupo controle.
# É salvo a nota da melhor entrada desse grupo controle, porém essa entrada não será usada como resposta.
# Após obter essa informacao, continuamos percorrendo a entrada até antes da ultima entrada.
# Se durante essa observação for encontrado uma entrada com nota melhor que o melhor do grupo controle,
# encontramos nossa solução, não olharemos mais nenhuma outra entrada. Caso até antes da ultima entrada não
# encontremos uma com nota melhor que a melhor entrada do controle, ficamos com a ultima entrada como solução 
# Nessa implementação, o tamanho do grupo controle será aproximamente 37% do tamanho total da entrada. 
# Obtemos esse valor dividindo o tamanho da entrada pela constante e
def secretary_solution(hotels : list):
    # Inicia as variaveis iniciais necessarias
    size = len(hotels)
    control_group_size = math.floor(size / math.e)
    best_control_hotel_score = -1
    best_hotel = None

    # Procura a melhor entrada no grupo controle
    for hotel_number in range(control_group_size):
        actual_hotel = hotels[hotel_number]
        if actual_hotel[1] > best_control_hotel_score:
            best_control_hotel_score = actual_hotel[1]

    # Procura uma melhor entrada até o penultimo dado
    for hotel_number in range(control_group_size, size-1):
        actual_hotel = hotels[hotel_number]
        if actual_hotel[1] > best_control_hotel_score:
            best_hotel = actual_hotel
            break
    
    # Caso não encontre uma entrada melhor que a do melhor controle. A ultima entrada será a solução
    if best_hotel is None:
        best_hotel = hotels[size-1]

    return best_hotel

if __name__ == "__main__":
    hotels = read_input(10)
    print(hotels)
    best_hotel = secretary_solution(hotels)
    print(best_hotel)