# coding: utf-8
from . import model_backend, model_exceptions

class Model(object):
    def converter_imagens(self, input_dir : str, output_dir : str, 
                                                ext : str='.jpg'):                                   

        model_backend.converter_imagens(input_dir, output_dir, ext)
    
    def redimensionar_imagens(self, input_dir : str, output_dir : str, 
                                            width : int, height : int):         

        model_backend.redimensionar_imagens(input_dir, output_dir, 
                                                    width, height)
    
    @property
    def campos_vazios(self) -> Exception:
        return model_exceptions.CamposVazios

