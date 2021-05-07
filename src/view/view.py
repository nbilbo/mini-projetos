# coding: utf-8
'''
Camada de visao do projeto.

Recebe os inputs do usuario e passa para a camada de controle.

cores : https://www.design-seeds.com/wander/sea/mental-vacation-45/

'''
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
        
        self._criar_estilo()
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
        
    def _criar_estilo(self):
        '''
        Define o estilo dos widgets.
        '''
        cor_1 = '#C7E0DD'
        cor_2 = '#76B0AC'
        cor_3 = '#6C8BA7'
        cor_4 = '#CBB6B4'
        cor_5 = '#E5D4D0'
        cor_6 = '#EAE8E6'

        estilo = Style()

        # frame
        estilo.configure('TFrame', background=cor_4)

        # botao
        estilo.configure('TButton', background=cor_3, foreground=cor_6,  
                                        font=('Georgia', 14, 'normal'), 
                                                        relief='flat')

        estilo.map('TButton',
                    background=[('active', cor_2)],
                    foreground=[('active', cor_6)])

        # label
        estilo.configure('TLabel', background=cor_4, font=('Gergia', 14, 'normal'))

        # entry
        estilo.configure('TEntry', fieldbackground=cor_6)
        
        #notebook        
        estilo.configure('TNotebook.Tab', background=cor_3, 
                                            foreground=cor_6, 
                                            font=('Arial', 14, 'bold'), 
                                            relief='raised', 
                                            borderwidth=5)

        estilo.map('TNotebook.Tab',
                    background=[('active', cor_2)],
                    foreground=[('active', cor_6)])

        # option menu
        estilo.configure('TMenubutton', background=cor_6, 
                            font=('Georgia', 14, 'normal'), 
                                            relief='flat')

        estilo.map('TMenubutton', 
                    background=[('active', cor_2)])

        # scales
        estilo.configure('TScale', background=cor_3)

        estilo.map('TScale', 
                    background=[('active', cor_2)])

        # spinboxs
        estilo.configure('TSpinbox', arrowsize=20, relief='flat',
                        background=cor_3, fieldbackground=cor_6)

        estilo.map('TSpinbox', 
                    background=[('active', cor_2)])
    
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
        self.title('Ferramentas v.0.3')
        self.maxsize(width=800, height=450)
        self.minsize(width=800, height=450)
        self.mainloop()
        
        