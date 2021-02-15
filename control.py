# coding: utf-8
from model import model_exceptions


class Control(object):
    def __init__(self, model, view):
        self._model = model()
        self._view = view(self)
        
    def converter_imagens(self, input_dir, output_dir, ext):
        try:
            self._model.converter_imagens(input_dir, output_dir, ext)
            self._view.mostrar_msg('Conversao concluida.')
            
        except model_exceptions.CamposVazios:
            self._view.mostrar_aviso(f'Campos obrigatorios vazios.')
            
        except FileNotFoundError:
            self._view.mostrar_aviso(f'Diretorio nao encontrado.')
    
    def redimensionar_imagens(self, input_dir, output_dir, width, height):
        try:
            self._model.redimensionar_imagens(input_dir, output_dir, width, height)
            self._view.mostrar_msg('Redimensiomanto concluido.')
        
        except model_exceptions.CamposVazios:
            self._view.mostrar_aviso(f'Campos obrigatorios vazios.')
            
        except FileNotFoundError:
            self._view.mostrar_aviso(f'Diretorio nao encontrado.')            
        
    
    def main(self):
        self._view.main()


