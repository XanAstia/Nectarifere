# Nectarifere (latest available version: 2.0)

To use this decorator:

    from nectarifere.nectar import nectar

    @nectar
    def your_function(*args, **kwargs):
      blabla
      
Or:
    
    from nectarifere.falzar import falzar
    
    @falzar
    def your_function(*args, **kwargs):
      blabla

To create your own decorator: 

    from nectarifere.extracteur import ExtracteurDeJus

    class mydecorator(ExtracteurDeJus):

        def __init__(self, function):
            super().__init__(function) #Superclass constructor
            self.myattribute = 42.

    
        def success(self):
            print(self.myattribute)
    
        def failure(self):
            print(1/self.myattribute)

    @mydecorator
    def whateverfunctionyouwant(args):
        ...
    
