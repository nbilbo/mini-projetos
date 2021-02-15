# coding: utf-8
from . import model_backend

class Model(object):
    def converter_imagens(self, input_dir, output_dir, ext='.jpg'):
        model_backend.converter_imagens(input_dir, output_dir, ext)
    
    def redimensionar_imagens(self, input_dir, output_dir, width, height):
        model_backend.redimensionar_imagens(input_dir, output_dir, width, height)

