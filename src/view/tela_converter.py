# coding: utf-8
import tkinter
import tkinter.ttk
from tkinter import filedialog


class TelaConverter(tkinter.ttk.Frame):
    PADX = PADY = 10
    
    def __init__(self, master, control, *args, **kwargs):
        '''
        parametros
        ----------
        
        master : tkinter.Widget
        
        control : control.Control
            objeto control
        '''
        super(TelaConverter, self).__init__(master, *args, **kwargs)
        
        self._control = control
        self._input = tkinter.StringVar()
        self._output = tkinter.StringVar()
        self._ext = tkinter.StringVar()
        
        self._criar_lbl_desc()
        self._criar_input()
        self._criar_output()
        self._criar_dropdown()
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
    
    def _criar_dropdown(self):
        '''
        Criar campo p/ usuario definir a nova extesao da imagem.
        '''        
        opcoes = ['.png', '.jpg']
        
        
        frame = tkinter.ttk.Frame(self)
        dropdown = tkinter.ttk.OptionMenu(frame, self._ext, opcoes[0], *opcoes, 
                                         style='Converter.TMenubutton')
        
        dropdown.pack(fill='x', padx=self.PADX, pady=self.PADY)
        frame.pack(fill='x',padx=self.PADX, pady=self.PADY)
    
    def _criar_btn_conf(self):
        '''
        Criar botao p/ usuario confirmar os campos.
        '''        
        btn = tkinter.ttk.Button(self, text='Confirmar', style='Converter.TButton', 
                                            command=self._cham_conv)
        
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
            text='Converter imagens de um diretorio alterando sua extensao.')
        
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
    
    def _cham_conv(self):
        '''
        Chama o metodo converter_imagens da camada de controle.
        '''
        self._control.converter_imagens(self._input.get(), 
                                        self._output.get(), 
                                        self._ext.get())
