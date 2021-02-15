# coding: utf-8
from tkinter import *
from tkinter import filedialog
from tkinter import ttk

from . import common
    

class TelaRedimensionar(Frame):
    PADX = PADY = 10
    
    def __init__(self, master, control, *args, **kwargs):
        '''
        parametros
        ----------
        
        master : tkinter.Widget
        
        control : control.Control
            objeto control
        '''
        super(TelaRedimensionar, self).__init__(master, *args, **kwargs)
        
        self._control = control
        self._input = StringVar()
        self._output = StringVar()
    
        self._criar_estilo_ent()
        self._criar_estilo_btn()
        self._criar_estilo_label()
        
        self._criar_lbl_desc()
        self._criar_input()
        self._criar_output()
        self._criar_larg()
        self._criar_altu()
        self._criar_btn_conf()
    
    def _criar_input(self):
        '''
        Criar campo p/ usuario definir o diretorio de entrada.
        '''
        frame = Frame(self)
        
        entry = ttk.Entry(frame, textvariable=self._input, 
                          font=('Arial', 16, 'normal'),
                          style='Converter.TEntry')
        
        btn_perg_ent = ttk.Button(frame, text='Dir Entrada*', 
                                  style='Converter.TButton',
                                  command=self._perg_dir_ent)
        
        entry.pack(side='left', fill='both', expand=True, 
                                        padx=self.PADX, 
                                        pady=self.PADY)
        
        btn_perg_ent.pack(side='left', padx=self.PADX, pady=self.PADY)
        
        frame.pack(fill='x', padx=self.PADX, pady=self.PADY)
    
    def _criar_output(self):
        '''
        Criar campo p/ usuario definir o diretorio de saida.
        '''        
        frame = Frame(self)
        
        entry = ttk.Entry(frame, textvariable=self._output, 
                            font=('Arial', 16, 'normal'),
                            style='Converter.TEntry')
        
        btn_perg_ent = ttk.Button(frame, text='Dir Saida*', 
                                  style='Converter.TButton',
                                  command=self._perg_dir_sai)
        
        entry.pack(side='left', fill='both', expand=True, 
                                        padx=self.PADX, 
                                        pady=self.PADY)
        
        btn_perg_ent.pack(side='left', padx=self.PADX, pady=self.PADY)
        
        frame.pack(fill='x', padx=self.PADX, pady=self.PADY)
    
    def _criar_larg(self):
        self._larg = common.Slider(self, 'Largura*')
        self._larg.pack(fill='x', padx=self.PADX*2, pady=self.PADY*2)
    
    def _criar_altu(self):
        self._altu = common.Slider(self, 'Altura*')
        self._altu.pack(fill='x', padx=self.PADX*2, pady=self.PADY*2)
        
    def _criar_btn_conf(self):
        '''
        Criar botao p/ usuario confirmar os campos.
        '''        
        btn = ttk.Button(self, text='Confirmar', style='Converter.TButton', 
                                            command=self._cham_redim)
        
        btn.pack(fill='x', expand=True, anchor='s', 
                                        padx=self.PADX, 
                                        pady=self.PADY)
    
    def _criar_lbl_desc(self):
        '''
        Criar label com a descricao da tela.
        '''        
        label = ttk.Label(self, anchor='center', style='Converter.TLabel',
                  text='Redimensionar imagens de um  diretorio.')
        
        label.pack(fill='x', padx=self.PADX, pady=self.PADY)
    
    def _perg_dir_ent(self):
        '''
        Usuario definir o diretorio de entrada.
        '''
        self._input.set(filedialog.askdirectory())
    
    def _perg_dir_sai(self):
        '''
        Usuario definir o diretorio de saida.
        '''        
        self._output.set(filedialog.askdirectory())
    
    def _cham_redim(self):
        '''
        Chama o metodo redimensionar_imagens do objeto control.
        '''
        self._control.redimensionar_imagens(self._input.get(), 
                                            self._output.get(), 
                                            self._larg.atual(), 
                                            self._altu.atual())
        
    
    def _criar_estilo_ent(self):
        estilo = ttk.Style()
        estilo.configure('Converter.TEntry', font=('Arial', 14, 'normal'),                                                               
                                                            borderwidth=3,
                                                            relief='raised')

    def _criar_estilo_btn(self):
        estilo = ttk.Style()
        estilo.configure('Converter.TButton', font=('Arial', 17, 'normal'), 
                                                                width=15,
                                                            borderwidth=3,
                                                            relief='raised')
    
    def _criar_estilo_label(self):
        estilo = ttk.Style()
        estilo.configure('Converter.TLabel', font=('Arial', 18, 'normal'))
