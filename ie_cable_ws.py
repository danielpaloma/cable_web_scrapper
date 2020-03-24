from bs4 import BeautifulSoup as soup 
from urllib.request import urlopen as uReq
import requests

def isBlank (myString):
    if myString and myString.strip():
        #myString is not None AND myString is not empty or blank
        return False
    #myString is None OR myString is empty or blank
    return True

my_url = 'http://www.interelectricas.com.co/subcatego.php?idcategoria=1&idsubcategoria=72&subcategoria=Cables%20de%20Cobre%20Aislados%20THHN'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")


containers = page_soup.findAll("td",{"class":"info"})
#print(type(containers))
#print(containers[0])

#son en total 40 cables:
del containers[0:2]
del containers[-1]
#print(containers[0])
#print(containers[-1])
print(len(containers))

#container = containers[0]

#verificar que containers solo contiene cables

#print(container.td.a)

#title of product
#print(container.td.a.b.get_text())
#price of product
# price = container.findAll("td",{"width":"160"})
# price_1 = price[0].get_text()
# print(type(price_1))


filename = "cable_CU_THWN.csv"
f = open(filename,"w")

headers = "Nombre,Precio\n"
f.write(headers)


for container in containers:
	nombre_cable = container.td.a.b.get_text()
	precios_cables = container.findAll("td",{"width":"160"})
	precio = precios_cables[0].get_text()

	
	print("Nombre:" + nombre_cable)
	print("Precio:" + precio)

	if isBlank(precio)!=True:

		#Dando formato a las cadenas:
		cable_f = nombre_cable.split(" REF:")
		cable = cable_f[0]

		p_a = precio.split()
		p_b = p_a[1].split("P")
		precio_final = p_b[0].replace(",","")
		

		print(cable + "," + precio_final + "\n")
		f.write(cable + "," + precio_final + "\n")

	else:
		pass

f.close()


