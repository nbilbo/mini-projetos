from tkinter import Frame
from tkinter.ttk import Label, Scale, Spinbox, Style


class Slider(Frame):
    MINIMO = 100
    MAXIMO = 2400
    
    def __init__(self, master, label, *args, **kwargs):
        '''
        parametros
        ----------
        master : tkinter.widget
        
        label : str
        
        '''
        super(Slider, self).__init__(master, *args, **kwargs)
        self._criar_estilo_label()
       
        self._criar_scale()
        self._criar_spinbox()
        self._criar_label(label)
        self.set_atual(self.MINIMO)

    def _criar_estilo_label(self):
        estilo = Style()
        estilo.configure('Slider.TLabel', font=('Arial', 14, 'normal'))
          
    def _criar_label(self, label):
        '''
        Criar label.
        '''
        frame = Frame(self, width=150, height=50)
        label = Label(frame, text=label, anchor='center', style='Slider.TLabel')
        
        label.bind('<Double-Button-1>', lambda e: self._spinbox.focus())

        label.pack(fill='both', expand=True, padx=5, pady=5)
        frame.pack(side='left')
        frame.pack_propagate(False)
                                       
    def _criar_spinbox(self):
        '''
        Criar Widget spinbox.
        '''
        self._spinbox = Spinbox(self, from_=self.MINIMO, 
                                         to=self.MAXIMO,
                            font=('Arial', 14, 'normal'),
                            width=10)
        
        self._spinbox['command'] = lambda: \
            self.set_atual(self._spinbox.get(), widget=self._spinbox)
        
        self._spinbox.bind('<Return>', lambda e: \
            self.set_atual(self._spinbox.get()))
        
        self._spinbox.pack(side='left', anchor='center')
    
    def _criar_scale(self):
        '''
        Criar widget Scale.
        '''
        self._scale = Scale(self, from_=self.MINIMO, 
                                    to=self.MAXIMO, 
                                orient='horizontal')
        
        self._scale['command'] = lambda e: \
            self.set_atual(self._scale.get(), widget=self._scale)  
                                        
        self._scale.pack(side='left', fill='x', anchor='center', expand=True, )
        
    def atual(self):
        '''
        Obter o valor atual
        
        retornos
        --------
        int
        '''
        return self._scale.get()
        
    def set_atual(self, atual, **kwargs):
        '''
        Define o valor atual.
        
        parametros
        ----------
        atual : int
        '''
        # caractere númerico é convertido em inteiro.
        if isinstance(atual, str) and atual.isdigit():
            atual = int(atual)
        
        # caractere não númerico convertido em inteiro.
        if not isinstance(atual, int):
            atual = self._scale.get()
        
        # atual fora do range.
        if atual not in range(self.MINIMO, self.MAXIMO):
            atual = self._scale.get()        
        
        widget = kwargs.get('widget')
        if widget:
            if isinstance(widget, Scale):
                self._spinbox.delete(0, 'end')
                self._spinbox.insert(0, str(atual))
            elif isinstance(widget, Spinbox):
                self._scale.set(atual)
        
        else:
            self._spinbox.delete(0, 'end')
            self._spinbox.insert(0, str(atual))
            self._scale.set(atual)

