class UIMenu(UIWindow):
    def __init__(self,width=100,height=100,top=0,left=0,right=None,bottom=None,manager=variables.MANAGER):

        GUI.__init__(self,width=width,height=height,manager=manager,
            top=top,left=left,right=right,bottom=bottom)

        
        with PanelLeft(
            width="50%",
            height="100% - 30",
            ) as w1:

            @w1
            def click():
                pass

            @w1
            def render(self):
                """
                Metodo usado para representar elementos hijos
                las modificación de las propiedades hace que se deba
                volver a renderizar el componente, los parametros de init
                son convertidos en propiedades automaticamente
                """
                for elem in self.lista:
                    with Button() as btn:
                        pass

