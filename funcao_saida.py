def caulcular_pg(qnt_hr,valor_h):
     hr=float(qnt_hr)
     taxa=float(valor_h)
     if hr <= 40:
      salario=hr*taxa
     else:
       h_excd= hr-40
       salario= 40 * taxa +(h_excd*(1,5*taxa))
     print(salario)
caulcular_pg(35,20)
    
        
