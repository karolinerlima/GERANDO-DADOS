import matplotlib.pyplot as plt
# Bibliotecas============================================
from numpy import square
#========================================================

input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]    # Criei uma lista para armazenar os valores



"""Define o título do grafico e nomeia os eixos"""
# O parâmetro linewidth em u controla a espessura da linha gerada por plot(). 
plt.plot(input_values,squares,linewidth=5) 
 # A função title() em v define um título para o gráfico. Os parâmetros fontsize, que aparecem repetidamente pelo código, controlam o tamanho do texto no gráfico.
plt.title("Square Numbers", fontsize=24)
 #   As funções xlabel() e ylabel() permitem definir um título para cada um dos eixos w, 
plt.xlabel("Value", fontsize=14) 
plt.ylabel("Square of Value", fontsize=14)
# e a função tick_params() estiliza as marcações nos eixos x  
plt.tick_params(axis='both', labelsize=14)



plt.show()                 # Abre o gráfico