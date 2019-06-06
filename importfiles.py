#librerias
# pip install pandas
# pip install urllib3
import pandas as pd
import urllib3

#lectura de pandas
alltickers = pd.read_csv('data/WIKI-datasets-codes.csv')

#crea carpeta y archivo en el formato WIKI/nombre hasta 25 lineas
datasets = alltickers.loc[0:25]


#iteracion del data set
for i, row in datasets.values:
	#url para descargar datos de las compañias
	baseurl = "https://www.quandl.com/api/v3/datasets/"
	finalurl = ".csv?api_key=H4obdyWLci4DWFBP-mya&collapse=none"
	tickersample = row

	#urllib3
	http = urllib3.PoolManager(timeout=65)
	#lee y extrae datos a los archivos al directorio WIKI de acuerdo a la iteracion
	mydata = http.request('GET', baseurl+i+finalurl, decode_content=True)
	mydata = mydata.data

	#crea el archivo
	to_write = open(i+".csv","w")

	#decodifica y guarda csv dentro del directorio WIKI
	to_write.write(mydata.decode('UTF-8'))
	to_write.close()
	print("success")
