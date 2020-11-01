# coding: utf-8


import os
from PIL import Image
from widgets import UiReduzirImagem


def eh_imagem(nome_arquivo):
    if nome_arquivo.endswith('png') or nome_arquivo.endswith('jpg'):
        return True
    return False

def reduzir_tamanho_imagens(input_dir, output_dir, ext='.jpg', width=1, height=1):
    lista_de_arquivos = [nome for nome in os.listdir(input_dir) if eh_imagem(nome)]
    for nome in lista_de_arquivos:
        imagem = Image.open(os.path.join(input_dir, nome)).convert('RGB')
        #redimensionada = imagem.resize((1280, 720))
        redimensionada = imagem.resize((width, height))
        nome_sem_ext = os.path.splitext(nome)[0]
        redimensionada.save(os.path.join(output_dir, nome_sem_ext + ext))
        #imagem.save(os.path.join(output_dir, nome_sem_ext + ext))

def button_click(tk):
    fields = tk.value()
    input_ = fields["input"]
    outout_ = fields["output"]
    ext = fields["optionmenu"]
    width = fields["width"]
    height = fields["height"]

    if input_ and outout_:
        reduzir_tamanho_imagens(input_, outout_, ext, width, height)

def main():
    try:
        interface_usuario = UiReduzirImagem()
        interface_usuario.button()["command"] = (lambda tk=interface_usuario:
                                                            button_click(tk))
        interface_usuario.execute()

    except Exception as e:
        print(e)
        
if __name__ == "__main__":
    main()

