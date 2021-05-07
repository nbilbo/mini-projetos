# coding: utf-8
'''
Um widget para ser usado juntamente com o pacote tkinter.

autor : nbilbo

ultimo update : 05/maio/2021
'''
import tkinter
import tkinter.ttk


class ControleSlider(object):
    '''
    Gerenciar os eventos que ocorrem no slider.
    '''
    def __init__(self, slider):
        self.slider = slider

    def bind_scale(self, *args):
        '''
        Atualiza o valor do spinbox.
        '''
        # print('bind_scale')
        valor_atual = (self.slider.scale_var.get())
        self.slider.spinbox.set(str(valor_atual))

    def bind_spinbox(self, *args):
        '''
        Atualiza o valor do scale.
        '''
        # print('bind_spinbox')
        valor_atual = self.slider.spinbox_var.get()
        
        if valor_atual.isnumeric() and int(valor_atual) <= self.slider.to:
            valor_atual = int(valor_atual)
        else:
            valor_atual = self.slider.scale_var.get()

        self.slider.scale_var.set(valor_atual)
        self.slider.spinbox_var.set(str(valor_atual))


class Slider(tkinter.ttk.Frame):
    '''
    Um frame que contem tanto um spinbox e um scale.
    '''
    def __init__(self, master, from_=0, to=1500, *args, **kwargs):
        '''
        parametros
        ----------
        from_, to : int
            valor minimo e maximo.
        '''
        super(Slider, self).__init__(master, *args, **kwargs)
        self.from_ = from_
        self.to = to
        self.controle_slider = ControleSlider(self)
        self.criar_widgets()
        self.valor = from_
    
    def criar_widgets(self):
        self.criar_scale()
        self.criar_spinbox()

    def criar_scale(self):
        '''
        Instancia um tkinter.ttk.Scale e o posiciona.
        '''
        self.scale_var = tkinter.IntVar()
        self.scale = tkinter.ttk.Scale(self) 
        self.scale['variable'] = self.scale_var
        self.scale['from_'] = self.from_
        self.scale['to'] = self.to
        self.scale['command'] = self.controle_slider.bind_scale
        self.scale.pack(side='left', fill='x', expand=True, padx=5, pady=5)

    def criar_spinbox(self):
        '''
        Instancia um tkinter.ttk.Spinbox e o posiciona.
        '''
        self.spinbox_var = tkinter.StringVar()
        self.spinbox = tkinter.ttk.Spinbox(self)
        self.spinbox['textvariable'] = self.spinbox_var
        self.spinbox['from_'] = self.from_
        self.spinbox['to'] = self.to
        self.spinbox['font'] = ('Arial', 15, 'normal')
        self.spinbox['width'] = 10
        self.spinbox['command'] = self.controle_slider.bind_spinbox
        self.spinbox.bind('<KeyRelease>', lambda event: \
                self.controle_slider.bind_spinbox(event))
        # self.spinbox.pack(side='left', fill='x', expand=True, padx=5, pady=5)
        self.spinbox.pack(side='left', padx=5, pady=5)

    @property
    def valor(self):
        '''
        retorno
        -------
        valor : int
            o valor atual do slider.
        '''
        return self.scale_var.get()

    @valor.setter
    def valor(self, valor):
        '''
        parametro
        ---------
        valor : int
            o novo valor do slider.
        '''
        if valor in range(self.from_, self.to+1):
            self.scale_var.set(valor)
            self.spinbox_var.set(str(valor))

    @property
    def scale(self):
        '''
        retorno
        -------
        tkinter.ttk.Scale
        '''
        return self._scale

    @scale.setter
    def scale(self, scale):
        self._scale = scale

    @property
    def spinbox(self):
        '''
        retorno
        -------
        tkinter.ttk.Spinbox
        '''
        return self._spinbox

    @spinbox.setter
    def spinbox(self, spinbox):
        self._spinbox = spinbox

    @property
    def scale_var(self):
        '''
        retorno
        -------
        tkinter.IntVar
        '''
        return self._scale_var

    @scale_var.setter
    def scale_var(self, scale_var):
        self._scale_var = scale_var

    @property
    def spinbox_var(self):
        '''
        retorno
        -------
        tkinter.StringVar
        '''
        return self._spinbox_var

    @spinbox_var.setter
    def spinbox_var(self, spinbox_var):
        self._spinbox_var = spinbox_var
        

class App(tkinter.Tk):
    '''
    Um aplicação somente para mostrar o widget slider.
    '''
    def __init__(self):
        super(App, self).__init__()
        self.criar_widgets() 
        self.criar_estilos()
    
    def criar_widgets(self):
        self.criar_slider()

    def criar_slider(self):
        self.slider = Slider(self)
        self.slider.pack(fill='x')

    def criar_estilos(self):
        estilo = tkinter.ttk.Style()

        # frames em geral
        estilo.configure('TFrame', background='#fEA')

        # scales
        estilo.configure('TScale', background='purple') 

        estilo.map('TScale', background=[('active', 'yellow')])

        # spinboxs
        estilo.configure('TSpinbox', arrowsize=20, relief='flat',
                    background='purple', fieldbackground='brown', 
                                            foreground='white')

        estilo.map('TSpinbox', 
        background=[('active', 'yellow'),('disabled', 'purple')])


