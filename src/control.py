# coding: utf-8
class Control(object):
    def __init__(self, model, view):
        '''
        parametros
        ----------
        model : classe camada de modelo.
        view : classe camada de visao.
        '''
        self._model = model()
        self._view = view(self)
        
    def converter_imagens(self, input_dir : str, output_dir : str, 
                                                        ext : str):
        try:
            self._model.converter_imagens(input_dir, output_dir, ext)
            self._view.mostrar_msg('Conversao concluida.')
            
        except self._model.campos_vazios:
            self._view.mostrar_aviso(f'Campos obrigatorios vazios.')
            
        except FileNotFoundError:
            self._view.mostrar_aviso(f'Diretorio nao encontrado.')
    
    def redimensionar_imagens(self, input_dir : str, output_dir : str, 
                                            width : str, height : str):
        try:
            self._model.redimensionar_imagens(input_dir, output_dir, width, height)
            self._view.mostrar_msg('Redimensiomanto concluido.')
        
        except self._model.campos_vazios:
            self._view.mostrar_aviso(f'Campos obrigatorios vazios.')
            
        except FileNotFoundError:
            self._view.mostrar_aviso(f'Diretorio nao encontrado.')            
        
    
    def main(self):
        '''
        Iniciar a aplicação.
        '''
        self._view.main()


