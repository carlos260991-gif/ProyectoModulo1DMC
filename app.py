import streamlit as st
st.title("Proyecto módulo 1 Fundamentals") #title par crer un titulo en un espacio generado#
st.sidebar.title ("Parámetros") #sidebar se usa para crear un adicional#
#ahora crearemos una interfaz insertando imagenes#
st.image(Python logo.png)

# a continuación se genera tres variables que generan una lista numerica que se visualizarán como un desplegable numerico de los rango determinados#
valor_inicial = st.number_input("ingrese el valor inicial", value = 0)
valor_final = st.number_input("ingrese el valor final",value = 1)

lista_numerica = list(range(valor_inicial, valor_final))

st.write(lista_numerica) #para este espacio se reemplaza el print por el write, es el comando de resultado#
#usaremos las funciones de ingresar imagenes#
