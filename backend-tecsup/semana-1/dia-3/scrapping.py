import  requests
url = requests.get("https://www.sbs.gob.pe/app/pp/sistip_portal/paginas/publicacion/tipocambiopromedio.aspx")

if(url.status_code == 200):
    print(url.text)
else:
    print("error al abrir la pagina" + str(url.status_code))