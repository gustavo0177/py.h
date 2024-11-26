class encapsulamento():

           def __init__(self,num1,num2):
                   self.__num1 = num1
                   self.__num2 = num2


           def adicionar(self):
                   return self.__num1+self.__num2
           

calc = encapsulamento (20,10)
print(calc.adicionar())
#"calc.__num1" esse cod gera erro no cod 