import streamlit as st
st.title("Proyecto módulo 1 Fundamentals") #title par crer un titulo en un espacio generado#
st.sidebar.title ("Parámetros") #sidebar se usa para crear un adicional#
#ahora crearemos una interfaz insertando imagenes#
st.image("Python_logo.png") #se utiliza image para insertar las imagenes previamente cargadas #
st.sidebar.image ("DMC.png") #ahora estamos insertando la imagen en la ventalla auxiliar#

#se esta creando una sección dentro de la ventana emergente donde se creará una lista con el selectbox y lo combinaremos con el IF que es un condicional
modulo = st.sidebar.selectbox("Elija un módulo", ["Módulo Listas", "Módulo Array", "Módulo Funciones"])

if modulo == "Módulo Listas" : #importante colocar doble = en las condicionales If y Elif#


  # a continuación se genera tres variables que generan una lista numerica que se visualizarán como un desplegable numerico de los rango determinados#
  valor_inicial = st.number_input("ingrese el valor inicial", value = 0)
  valor_final = st.number_input("ingrese el valor final",value = 1)
  lista_numerica = list(range(valor_inicial, valor_final))
  st.write(lista_numerica) #para este espacio se reemplaza el print por el write, es el comando de resultado#
  #usaremos las funciones de ingresar imagenes#

elif modulo == "Módulo Array"
  st.write ("Estas en el módulo de arreglos")

else:
  st.write ("Estas en el módulo de funciones")



