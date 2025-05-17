# os.listdir para navegar em caminhos
# /Users/luizotavio/Desktop/EXEMPLO
# C:\Users\luizotavio\Desktop\EXEMPLO
# caminho = r'C:\\Users\\luizotavio\\Desktop\\EXEMPLO'
# caminho = 'D:\\'

import os
def rastrear_documentos(caminho:str,extensao:str):
    """
    Rastreia arquivos dentro do diretório especificado com a extensão desejada.

    Parâmetros:
    caminho (str): O caminho do diretório onde os arquivos serão pesquisados.
    extensao (str): A extensão dos arquivos a serem rastreados (exemplo: 'pdf', 'jpg', 'docx').

    Retorna:
    None. Exibe na tela os arquivos encontrados e o total de arquivos com a extensão específica.
    """
    contador = 0
    try:
        # print(os.listdir(caminho))
        for i in os.listdir(caminho):
            dividido = os.path.splitext(i)
            exte = '.' + extensao
            
            if exte in dividido:
                contador +=1
                print( ''.join(dividido))
                
            elif exte not in dividido:
                ...
        print(f'\n📂 {contador} aquivos Encontrado com a Extensão "{exte}"')
        
    except FileNotFoundError:
        print(f'O Caminho {caminho} não existe!')
            
def entrada_do_usuario(msg: str) -> str:
    return input(msg )

while True:
    print('➖'*60)
    print('📂 Programa de Rastreamento de arquivos de um tipo de extensão')
    print('➖'*60)
    caminho = entrada_do_usuario('Digite o caminho que desejasmanipular: ')
    extensao = entrada_do_usuario('Digite a extensão que desejas manipular (docx, jpg,pdf...): ')
    rastrear_documentos(caminho,extensao)
    print()
    sair = entrada_do_usuario('deseja sair? 1 para sim: ')
    if sair == '1':
        break
    os.system('cls')