import streamlit as st
import pandas as pd
import numpy as np

st.title("Border Freight - Cotizador de Rutas")
st.write("Este cotizador esta diseñado para subir un archivo de rutas y evaluar los precios que contiene")

#We will first define the varaibles we will need to evaluate the routes submitted by the user
cost_per_km = 25.5
avg_monthly_km = 1100000
monthly_kpi = 315000*4
#We will create a dictionary with all the routes and their associated distances
km = {"Aguascalientes - Chihuahua": 1310.18181818182,
"Aguascalientes - Guanajuato": 248,
"Aguascalientes - Jalisco": 234,
"Aguascalientes - Monterrey": 544.4,
"Aguascalientes - Reynosa": 812.866666666667,
"Aguascalientes - Rio Bravo": 819.714285714286,
"Aguascalientes - Saltillo": 498.5,
"Aguascalientes - San Luis Potosi": 204.571428571429,
"Altamira - Monterrey": 506.4,
"Altamira - Reynosa": 525.258064516129,
"Chihuahua - Chihuahua": 360.666666666667,
"Chihuahua - Guanajuato": 1567.77777777778,
"Chihuahua - Jalisco": 1507,
"Chihuahua - Monterrey": 1158.25157232704,
"Chihuahua - Puebla": 1939.76288659794,
"Chihuahua - Reynosa": 1382.4387755102,
"Chihuahua - Rio Bravo": 1434,
"Chihuahua - Saltillo": 845.375,
"Chihuahua - San Luis Potosi": 1109.94736842105,
"CMX - Mexico": 39.25,
"CMX - Monterrey": 914.230769230769,
"CMX - Puebla": 190,
"CMX - Queretaro": 227,
"CMX - Reynosa": 981.39,
"CMX - San Luis Potosi": 392,
"Durango - Reynosa": 656.1,
"Guanajuato - Guanajuato": 40.5771812080537,
"Guanajuato - Jalisco": 170.797570850202,
"Guanajuato - Matamoros": 1007,
"Guanajuato - Mexico": 273.541666666667,
"Guanajuato - Monterrey": 725.521739130435,
"Guanajuato - Puebla": 343.004739336493,
"Guanajuato - Queretaro": 162.919191919192,
"Guanajuato - Reynosa": 952.22015503876,
"Guanajuato - Rio Bravo": 959.2,
"Guanajuato - Saltillo": 624,
"Guanajuato - San Luis Potosi": 185.453409090909,
"Guerrero - Reynosa": 1640,
"Hidalgo - Monterrey": 883,
"Jalisco - Jalisco": 194.405660377358,
"Jalisco - Mexico": 529,
"Jalisco - Monterrey": 802.377777777778,
"Jalisco - Nayarit": 203,
"Jalisco - Puebla": 648.560975609756,
"Jalisco - Queretaro": 240.206896551724,
"Jalisco - Reynosa": 915.161572052402,
"Jalisco - Rio Bravo": 1003.92857142857,
"Jalisco - Saltillo": 586.818181818182,
"Jalisco - San Luis Potosi": 197.677386934673,
"Jalisco - Tlaxcala": 533.918918918919,
"Llera - San Luis Potosi": 363,
"Matamoros - Monterrey": 307.538461538462,
"Matamoros - Morelos": 1082,
"Matamoros - Queretaro": 999,
"Matamoros - Reynosa": 89.36,
"Matamoros - Rio Bravo": 70.8,
"Matamoros - Saltillo": 377,
"Matamoros - San Luis Potosi": 714.15,
"Mexico - Mexico": 104,
"Mexico - Monterrey": 880.436464088398,
"Mexico - Puebla": 159,
"Mexico - Queretaro": 175,
"Mexico - Reynosa": 985.095307917889,
"Mexico - San Luis Potosi": 361.754716981132,
"Mexico - Tolcayuca": 83,
"Monterrey - Monterrey": 25.3292517006803,
"Monterrey - Nuevo Laredo": 234,
"Monterrey - Queretaro": 719.6,
"Monterrey - Reynosa": 231.710693301998,
"Monterrey - Rio Bravo": 250.102040816327,
"Monterrey - Saltillo": 59.6931012250161,
"Monterrey - San Luis Potosi": 519.856304985337,
"Monterrey - Tampico": 499.04347826087,
"Monterrey - Veracruz": 1264,
"Morelos - Reynosa": 1094,
"Morelos - Rio Bravo": 1097,
"Nayarit - Queretaro": 613.711409395973,
"Nayarit - Reynosa": 1251,
"Nuevo Laredo - Reynosa": 255,
"Nuevo Laredo - Rio Bravo": 433,
"Nuevo Laredo - Saltillo": 283.428571428571,
"Nuevo Laredo - San Luis Potosi": 728,
"Puebla - Queretaro": 297,
"Puebla - Reynosa": 1018.59922928709,
"Puebla - Rio Bravo": 806.75,
"Puebla - Saltillo": 986,
"Puebla - San Luis Potosi": 498.796875,
"Puebla - Tlaxcala": 74,
"Queretaro - Queretaro": 33,
"Queretaro - Reynosa": 955.945038167939,
"Queretaro - Rio Bravo": 937.148936170213,
"Queretaro - Saltillo": 630,
"Queretaro - San Luis Potosi": 214.187050359712,
"Reynosa - Reynosa": 111.75,
"Reynosa - Rio Bravo": 800.413793103448,
"Reynosa - Saltillo": 308.511916363959,
"Reynosa - San Luis Potosi": 735.696159833939,
"Reynosa - Tlaxcala": 912.5,
"Reynosa - Victoria": 330,
"Reynosa - Monterrey": 231.710693301998,
"Rio Bravo - San Luis Potosi": 680.255813953488,
"Saltillo - Saltillo": 53.0666666666667,
"Saltillo - San Luis Potosi": 468.566929133858,
"Saltillo - Tampico": 587,
"Saltillo - Reynosa": 308.511916363959,
"Saltillo - Queretaro": 630,
"Saltillo - Monterrey": 59.6931012250161,
"San Luis Potosi - San Luis Potosi": 189.875,
"San Luis Potosi - Tampico": 453,
"San Luis Potosi - Tlaxcala": 510.6}

#We will prompt the user to upload a file
uploaded_file = st.file_uploader("Sube la contrapropuesta del cliente:", type = ["xlsx"], key = "file1")
uploaded_file2 = st.file_uploader("Sube la cotizacion original:", type = ["xlsx"], key = "file2")

#The application will run the program only if the user uploadas a file, otherwise it will display
#an error message.
if uploaded_file is not None and uploaded_file2 is not None:
      route_data = pd.read_excel(uploaded_file, header = 1)
      quote = pd.read_excel(uploaded_file2, header = 1)
      st.write('<h2 style="color:#c4500b;">Archivo cargado:</h2>', unsafe_allow_html=True)
      st.dataframe(route_data)
      #We will format all floats with 1 decimal place and thousands separators
      
      #We will format the price column to a float to perform calculations with it
      route_data["Precio"] = route_data["Precio"].astype(float)
      
      #We will fill any null values in the frequency column with a 1
      route_data["Frequencia (Mensual)"] = route_data["Frequencia (Mensual)"].fillna(1)
    
      #We will create the route column which will join the origin and destination columns 
      route_data["Ruta"] = route_data["Origen"] + " - " + route_data["Destino"]
    
      #We will create a new column named distancia that will return the route distance. If the program
      #can't find it in the route dictionary, it will prompt the user to input the distance manually 
      route_data["Distancia"] = route_data["Ruta"].map(km)
      for i in route_data.index[route_data["Distancia"].isnull()]:
        km_input = float(input(f"Ingresa el kilometraje de la ruta {route_data.loc[i,'Ruta']}:"))
        route_data.loc[i,"Distancia"] = km_input

      #We will create a column named Precio por Km
      route_data["Precio por KM"] = route_data["Precio"] / route_data["Distancia"]
    
      #We will create a column that will tell us the route type and another that tells us the direction of
      #the trip depending on route distance and trip origin respectively.
      route_data["Tipo de Ruta"] = np.where(route_data["Distancia"] <= 400, "Tramo Corto", "Tramo Largo")
      route_data["Sentido"] = np.where(((route_data["Tipo de Ruta"] == "Tramo Largo") & (route_data["Origen"] == "Reynosa")) |
                                     ((route_data["Tipo de Ruta"] == "Tramo Largo") & (route_data["Origen"] == "Monterrey")) |
                                     ((route_data["Tipo de Ruta"] == "Tramo Largo") & (route_data["Origen"] == "Saltillo")) |
                                     ((route_data["Tipo de Ruta"] == "Tramo Largo") & (route_data["Origen"] == "Matamoros")), "Salida",
                                     np.where((route_data["Tipo de Ruta"] == "Tramo Corto") & (route_data["Origen"] == "Reynosa"), "Salida", "Retorno"))
    
      #We will create a column that will calculate the profit margin per route
      route_data["Utilidad (%)"] = ((route_data["Precio"] - (route_data["Distancia"] * cost_per_km))/route_data["Precio"])*100
    
      #We will create a column that will determine route acceptance based on profit theresholds per route type
      #and direction.
      route_data["Evaluacion"] = np.where(((route_data["Tipo de Ruta"] == "Tramo Corto") & (route_data["Sentido"]  == "Retorno") & (route_data["Utilidad (%)"] >= 36)), "Si",
                                        np.where(((route_data["Tipo de Ruta"] == "Tramo Corto") & (route_data["Sentido"] == "Salida") & (route_data["Utilidad (%)"] >= 49)), "Si",
                                                 np.where(((route_data["Tipo de Ruta"] == "Tramo Largo") & (route_data["Sentido"] == "Salida") & (route_data["Utilidad (%)"] >= 15)), "Si",
                                                          np.where(((route_data["Tipo de Ruta"] == "Tramo Largo") & (route_data["Sentido"] == "Retorno") & (route_data["Utilidad (%)"] >= 33)), "Si", "No"))))
    
      #We will create a column called monthly distance that will multiply the monthly frequency by the route distance
      route_data["Distancia Mensual"] = route_data["Distancia"] * route_data["Frequencia (Mensual)"]
      #We will create a column called monthly invoicing 
      route_data["Facturacion Mensual"] = route_data["Precio"] * route_data["Frequencia (Mensual)"]
      #We will create a column called monthly costs
      route_data["Costo Mensual"] = route_data["Distancia Mensual"] * cost_per_km

      #We will create a new data frame to display
      route_data_new = pd.DataFrame(route_data, columns = ["Ruta", "Tipo de Ruta", "Sentido", "Distancia", "Precio", "Precio por KM", "Utilidad (%)", "Evaluacion"])
      
      #We will display the program outputs
      st.write("---")
      st.write('<h2 style="color:#c4500b;">Evaluacion de Rutas:</h2>', unsafe_allow_html=True)
      st.dataframe(route_data_new)

      st.write("---")
      st.write('<h2 style="color:#c4500b;">Evaluacion de Operacion:</h2>', unsafe_allow_html=True)
      km_provided = route_data["Distancia Mensual"].sum()
      revenue = route_data["Facturacion Mensual"].sum()
      total_costs = route_data["Costo Mensual"].sum()
      total_profit = (revenue - total_costs) / revenue
      
      st.write('<b>Kilometros Mensuales de Operacion Cotizada:</b>', f"{km_provided:,.2f}", unsafe_allow_html=True)
      st.write('<b>Facturacion Mensual de Operacion Cotizada:</b>', f"{revenue:,.2f}", unsafe_allow_html=True)
      st.write('<b>Utlidad de Operacion Cotizada:</b>', f"{total_profit:.2%}", unsafe_allow_html=True)
      st.write('<b>Promedio de Kilometros Mensuales:</b>', f"{avg_monthly_km:,.2f}", unsafe_allow_html=True)
      
      km_mensual_new = km_provided + avg_monthly_km
      st.write('<b>Kilometros Mensuales + Nueva Operacion:</b>', f"{km_mensual_new:,.2f}", unsafe_allow_html=True)
      per_increase = ((km_provided + avg_monthly_km) - avg_monthly_km) / avg_monthly_km
      st.write('<b>Porcentaje de Incremento:</b>', f"{per_increase:.2%}", unsafe_allow_html=True)
      
      st.write('<b>KPI Mensual:</b>', f"{monthly_kpi:,.2f}", unsafe_allow_html=True)
      
      difference = km_mensual_new - monthly_kpi
      st.write('<b>Diferencia:</b>', f"{difference:,.2f}", unsafe_allow_html=True)

      st.write("---")
      st.write('<h2 style="color:#c4500b;">Comparativa con Cotizacion Original:</h2>', unsafe_allow_html=True)
      #We will create a column named route that will merge the origin and destination columns with a dash
      quote["Ruta"] = quote["Origen"] + " - " + quote["Destino"]
      
      #We will merge the route_data and quote data frames on the route column
      compare = pd.merge(route_data, quote, on = "Ruta")

      #We will create two columns to see the difference between the price we quoted initally and the 
      #client's response
      compare["Diferencia"] = compare["Precio_x"] - compare["Precio_y"]
      compare["Diferencia %"] = ((compare["Precio_x"] - compare["Precio_y"])/compare["Precio_y"])*100
      compare["Diferencia %"] = compare["Diferencia %"].round(2)

      #We will create a new data frame to display the comparisson 
      compare_new = pd.DataFrame(compare, columns = ["Ruta", "Precio_x", "Precio_y", "Diferencia", "Diferencia %"])
      compare_new.rename(columns={"Precio_x": "Precio Cliente", "Precio_y": "Precio Cotizacion"}, inplace=True)
      st.dataframe(compare_new)
else:
      st.warning("Por favor sube un archivo de Excel para continuar")
      
      

      
    
      
      
      
      
      
    
    
    
    

















