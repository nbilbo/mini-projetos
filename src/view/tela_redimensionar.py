# coding: utf-8
import tkinter
import tkinter.ttk
from tkinter import filedialog

from . import slider
    

class TelaRedimensionar(tkinter.ttk.Frame):
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
        self._input = tkinter.StringVar()
        self._output = tkinter.StringVar()
        
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
        frame = tkinter.ttk.Frame(self)
        
        entry = tkinter.ttk.Entry(frame, textvariable=self._input, 
                          font=('Arial', 16, 'normal'),
                          style='Converter.TEntry')
        
        btn_perg_ent = tkinter.ttk.Button(frame, text='Dir Entrada*', 
                                  style='Converter.TButton',
                                  width=15,
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
        frame = tkinter.ttk.Frame(self)
        
        entry = tkinter.ttk.Entry(frame, textvariable=self._output, 
                            font=('Arial', 16, 'normal'),
                            style='Converter.TEntry')
        
        btn_perg_ent = tkinter.ttk.Button(frame, text='Dir Saida*', 
                                  style='Converter.TButton',
                                  width=15,
                                  command=self._perg_dir_sai)
        
        entry.pack(side='left', fill='both', expand=True, 
                                        padx=self.PADX, 
                                        pady=self.PADY)
        
        btn_perg_ent.pack(side='left', padx=self.PADX, pady=self.PADY)
        
        frame.pack(fill='x', padx=self.PADX, pady=self.PADY)
    
    def _criar_larg(self):
        '''
        Criar slider p/ usuario definir a largura da imagem.
        '''
        frame = tkinter.ttk.Frame(self)
        label = tkinter.ttk.Label(frame, text='Largura*', width=10)
        self._larg = slider.Slider(frame, from_=1, to=1920)

        frame.pack(fill='x', padx=self.PADX*2, pady=self.PADY*2)
        self._larg.pack(side='left', fill='x', expand=True)
        label.pack(side='left', fill='x')
    
    def _criar_altu(self):
        '''
        Criar slider p/ usuario definir a altura da imagem.
        '''
        frame = tkinter.ttk.Frame(self)
        label = tkinter.ttk.Label(frame, text='Altura*', width=10)
        self._altu = slider.Slider(frame, from_=1, to=1080)

        frame.pack(fill='x', padx=self.PADX*2, pady=self.PADY*2)
        self._altu.pack(side='left', fill='x', expand=True)
        label.pack(side='left', fill='x')
   
    def _criar_btn_conf(self):
        '''
        Criar botao p/ usuario confirmar os campos.
        '''        
        btn = tkinter.ttk.Button(self, text='Confirmar', style='Converter.TButton', 
                                            command=self._cham_redim)
        
        btn.pack(fill='x', expand=True, anchor='s', 
                                        padx=self.PADX, 
                                        pady=self.PADY)
    
    def _criar_lbl_desc(self):
        '''
        Criar label com a descricao da tela.
        '''        
        label = tkinter.ttk.Label(
            self, 
            anchor='center', 
            style='Converter.TLabel',
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
        Chama o metodo redimensionar_imagens da camada de controle.
        '''
        self._control.redimensionar_imagens(self._input.get(), 
                                            self._output.get(), 
                                            self._larg.valor, 
                                            self._altu.valor)
        
