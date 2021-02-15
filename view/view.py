# coding: utf-8
from tkinter import Tk, messagebox
from tkinter.ttk import Notebook, Style
from . import tela_converter, tela_redimensionar


class View(Tk):
    def __init__(self, control, *args, **kwargs):
        '''
        parametros
        ----------
        control : control.Control
            objeto control
        '''
        super(View, self).__init__(*args, **kwargs)
        self._control = control
        
        self._criar_estilo_note()
        self._criar_notebook()
        self._criar_converter()
        self._criar_redimensionar()
        
    def _criar_notebook(self):
        '''
        Criar notebook p/ navegar entre varias telas.
        '''
        self._note = Notebook(self, style='View.TNotebook')
        self._note.pack(fill='both', expand=True)
    
    def _criar_converter(self):
        '''
        Intancia uma nova tela_converter e adiciona ao notebook.
        '''
        converter = tela_converter.TelaConverter(self._note, self._control)
        self._note.add(converter, text='Converter')
    
    def _criar_redimensionar(self):
        redimensionar = tela_redimensionar.TelaRedimensionar(self._note, self._control)
        self._note.add(redimensionar, text='Redimensionar')
        
    def _criar_estilo_note(self):
        estilo = Style()
        estilo.configure('View.TNotebook.Tab', font=('Arial', 14, 'bold'))
    
    def mostrar_msg(self, msg):
        '''
        Abre uma nova janela mostrando uma mensagem.
        '''
        messagebox.showinfo('Mensagem', msg)
    
    def mostrar_aviso(self, aviso):
        '''
        Abreuma nova janela mostrando um aviso de alerta.
        '''
        messagebox.showwarning('Aviso', aviso)
           
    def main(self):
        '''
        Inicializa a gui.
        '''
        self.title('Ferramentas v.0.2')
        self.geometry('900x500')
        self.mainloop()
        