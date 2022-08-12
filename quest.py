from math import sqrt

# Coordenadas do ponto 1 (4 1 -1)
(ponto1_x, ponto1_y, ponto1_z) = input(
    'insira as coordenadas do ponto 1: ').split(' ')
(ponto1_x, ponto1_y, ponto1_z) = (int(ponto1_x), int(ponto1_y), int(ponto1_z))

# Coordenadas do ponto 2 (5 2 2)
(ponto2_x, ponto2_y, ponto2_z) = input(
    'insira as coordenadas do ponto 2: ').split(' ')
(ponto2_x, ponto2_y, ponto2_z) = (int(ponto2_x), int(ponto2_y), int(ponto2_z))

# Coordenadas do ponto inicial da reta (0 0 0)
(ponto_reta_x, ponto_reta_y, ponto_reta_z) = input(
    'insira as coordenadas do ponto da reta: ').split(' ')
(ponto_reta_x, ponto_reta_y, ponto_reta_z) = (
    int(ponto_reta_x), int(ponto_reta_y), int(ponto_reta_z))

# Coordenadas do vetor diretor da reta (2 -1 2)
(vetor_dir_x, vetor_dir_y, vetor_dir_z) = input(
    'insira as coordenadas do vetor diretor da reta: ').split(' ')
(vetor_dir_x, vetor_dir_y, vetor_dir_z) = (
    int(vetor_dir_x), int(vetor_dir_y), int(vetor_dir_z))

# Vetor do lado do triângulo
(vetor_lado_1_x, vetor_lado_1_y, vetor_lado_1_z) = (
    ponto2_x-ponto1_x, ponto2_y-ponto1_y, ponto2_z-ponto1_z)

area = 20*sqrt(2)

while True:
    # Gerar um ponto na reta (para a questão, use t = 8.615)
    t = float(input('t= '))
    (ponto_interesse_x, ponto_interesse_y, ponto_interesse_z) = (ponto_reta_x+t*vetor_dir_x, ponto_reta_y +
                                                                 t*vetor_dir_y, ponto_reta_z+t*vetor_dir_z)
    # Gerar o lado do triângulo
    (vetor_lado_2_x, vetor_lado_2_y, vetor_lado_2_z) = (
        ponto_interesse_x-ponto1_x, ponto_interesse_y-ponto1_y, ponto_interesse_z-ponto1_z)

    # Produto vetorial
    cx = vetor_lado_1_y*vetor_lado_2_z - vetor_lado_1_z*vetor_lado_2_y
    cy = vetor_lado_1_z*vetor_lado_2_x - vetor_lado_1_x*vetor_lado_2_z
    cz = vetor_lado_1_x*vetor_lado_2_y - vetor_lado_1_y*vetor_lado_2_x

    # Módulo
    modulo = sqrt(cx**2+cy**2+cz**2)

    # Área do triângulo (que é a metade do módulo produto vetorial)
    area_calculada = modulo/2

    # Comparar com 20 raiz de 2 (quanto mais próximo de 0, mais próximo do resultado)
    print(f'diff = {area - area_calculada}')

    # Coordenadas do ponto na reta
    print(
        f'ponto é ({ponto_interesse_x}, {ponto_interesse_y}, {ponto_interesse_z})')
    # a+b+c
    print(f'soma é {ponto_interesse_x+ponto_interesse_y+ponto_interesse_z}')
