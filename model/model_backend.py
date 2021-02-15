# coding: utf-8
import os
from PIL import Image
from . import model_exceptions


def eh_imagem(nome_arquivo):
    '''
    Verificar se um arquivo e uma imagem.
    
    parametros
    ----------
    nome_arquivo : str
    
    retornos
    --------
    bool
    '''
    if nome_arquivo.endswith('png') or nome_arquivo.endswith('jpg'):
        return True
    else:
        return False

def converter_imagens(input_dir, output_dir, ext='.jpg'):
    '''
    Converter o tipo de todas as imagens em um diretorio.
    
    parametros
    ----------
    input_dir : str
        caminho completo da pasta com as imagens.
    
    output_dir : str
        caminho completo da pasta de saida.
    
    ext : str
        nova extensao da imagem.
    '''
    pref = 'redi_'
    if input_dir.strip() and output_dir.strip():
        lista_de_arquivos = [nome for nome in os.listdir(input_dir) \
                                                if eh_imagem(nome)]
        for nome in lista_de_arquivos:
            imagem = Image.open(os.path.join(input_dir, nome)).convert('RGB')
            nome_sem_ext = os.path.splitext(nome)[0]
            novo_nome = pref + nome_sem_ext
            imagem.save(os.path.join(output_dir, novo_nome + ext))
    else:
        raise model_exceptions.CamposVazios(f'Informe todos os campos.')

def redimensionar_imagens(input_dir, output_dir, width, height):
    '''
    Altera a largura e altura de todas as  imagens em um diretorio.
    
    parametros
    ----------
    input_dir : str
        caminho completo da pasta com as imagens.
    
    output_dir : str
        caminho completo da pasta de saida.
    
    width : int
    
    height : int
    '''    
    pref = 'redu_'
    
    if input_dir.strip() and output_dir.strip():
        lista_de_arquivos = [nome for nome in os.listdir(input_dir) \
                                                if eh_imagem(nome)]
        for nome in lista_de_arquivos:
            imagem = Image.open(os.path.join(input_dir, nome)).convert('RGB')
            redimensionada = imagem.resize((int(width), int(height)))
            novo_nome = pref + nome
            redimensionada.save(os.path.join(output_dir, novo_nome))
    else:
        raise model_exceptions.CamposVazios(f'Informe todos os campos.')
