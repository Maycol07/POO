# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 15:52:20 2022

@author: USUARIO B-V
"""

class Empresa:
    
    def __init__(self):
        print()
        print('-------------------- BIENVENIDO -------------------')
        self.trabajador=input('Ingrese el nombre o usuario del trabajador: ')
        while (True):
            
            self.categoria=input('Categoria: ')
            categoria=self.categoria
            if categoria == 'a' or categoria=='A' or categoria=='B' or categoria=='b' or categoria =='C' or categoria =='c':                              
                break
            else:print('Ingrese correctamente los datos de la Categoria sea:  [ A B C ]')

        if categoria=='A' or categoria=='a':
            self.sueldo=3000                   
        elif categoria=='B' or categoria=='b':
            self.sueldo=2500                    
        elif categoria=='C' or categoria=='c':
            self.sueldo=2000
        elif categoria=="":
            print('Ingresa un dato no dejar en blanco')
            return

        while (True):
            try: 
                self.horas_e=int(input('Horas Extras: '))
            except:
                print('Ingresa correctamente las Horas Extras  ')
            else:break 
 
        while (True):            
            try:
                self.tardanzas=int(input('Tardanzas (minutos) : '))
            except:
                print('Ingresa correctamente las Tardanzas ')
            else:break 

        self.pago_hora_extra=(self.sueldo/240)*self.horas_e
        self.convertir=self.tardanzas/60
        self.descuento=(self.sueldo/240)*self.convertir
    def mostrar(self):
        print()
        print(' _________________FERROTEC SAC__________________')
        print('|                   boleta                     ')
        print('|')
        print('|--- Nombre o Codigo      :',self.trabajador)
        print('|--- Categoria            :',self.categoria)
        print('|--- Sueldo basico        :',self.sueldo)
        print('|--- Descuento Tardanza   : {:.3f}'.format(self.descuento))
        print('|--- Pago por horas extras: {:.3f}'.format(self.pago_hora_extra))
        print('|--- Sueldo Neto          : {:.3f}'.format((self.sueldo-self.descuento)+self.pago_hora_extra))
        print('|')
        print('|_______________________________________________')
        print()
        while (True):

            t=input('Desea continua pagar a otro empleado?  ingrese [SI o NO ] : ')
            if t=='Si' or t=='SI' or t=='si' or t=='sI' :
                r=Empresa()
                r.mostrar()
                return
                
            elif t=='No' or t=='NO' or t=='no' or t=='nO' :
                print('OK chao ')
                break
                          
            else:
                print('Solo ingrese si o no ')
    

objeto=Empresa()
objeto.mostrar()



