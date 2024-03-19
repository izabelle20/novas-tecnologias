#Escreva um aplicativo que exibe uma caixa, uma oval, uma seta e um losango utilizando asteriscos (*).

# Função para desenhar a forma desejada
def desenhar_forma(forma):
    print(forma)

# Desenhando a caixa
caixa = """
*********
*       *
*       *
*       *
*********
"""
desenhar_forma("Caixa:")
print(caixa)

# Desenhando a oval
oval = """
  ***  
 *   * 
 *   * 
 *   * 
  ***  
"""
desenhar_forma("Oval:")
print(oval)

# Desenhando a seta
seta = """
    *    
   ***   
  *****  
    *    
    *    
    *    
"""
desenhar_forma("Seta:")
print(seta)

# Desenhando o losango
losango = """
   *   
  ***  
 ***** 
*******
 ***** 
  ***  
   *   
"""
desenhar_forma("Losango:")
print(losango)
