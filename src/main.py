# coding: utf-8
from view.view import View
from model.model import Model
from control import Control


controle = Control(Model, View)
controle.main()
