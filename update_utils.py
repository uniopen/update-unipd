from bs4 import BeautifulSoup
import requests

mensaList = ['sanfrancesco', 'piovego', 'agripolis', 'acli', 'belzoni', 'forcellini', 'murialdo']

def get_cal():
    soup = BeautifulSoup(requests.get("http://www.esupd.gov.it/it").content, "html.parser")
    listFull = []
    listPart = []
    listCal = []
    p = 0
    for i in soup.find_all("td"):
        listFull.append(str(i))
    for x in range(7):
        listPart.append(listFull[p])
        listPart.append(listFull[p + 1])
        p += 4
    for x in range(len(listPart)):
        if 'open' in listPart[x]:
            listCal.append(1)
        else:
            listCal.append(0)
    mensaDict = {}
    if listCal is not None:
        x = 0
        for mensa in mensaList:
            mensaDict[mensa] = {}
            mensaDict[mensa]["pranzo"] = listCal[x]
            mensaDict[mensa]["cena"] = listCal[x + 1]
            x += 2
    return mensaDict


def get_menu():
    rep = '<span style="visibility:hidden">:</span>'
    nomenu = 'Menu non pubblicato su www.esupd.gov.it/'
    errmenu = ['Niente menu, errore su www.esupd.gov.it/']
    mensaMenu = {}
    for x in range(len(mensaList)):
        mensaMenu = {}
        mid = x + 1
        mensaid = '0' + str(mid)
        completo = {"primo": [], "secondo": [], "contorno": [], "dessert": []}
        try:
            url = "http://www.esupd.gov.it/it/Pagine/Menu.aspx?idmenu=ME_%s" % mensaid
            soup = BeautifulSoup(requests.get(url).content, "html.parser")
            menu = []
            for i in soup.find_all("h2"):
                portata = i.text.split()[0].lower()
                for j in i.next_siblings:
                    if j.name == "h2":
                        break
                    if j.name == "ul":
                        a = str(j)
                        menu += (a.split("<li>"))
                        for piatto in range(len(menu)):
                            if "h3" in menu[piatto]:
                                menu[piatto] = menu[piatto].replace(rep, ' ')
                                txt = menu[piatto][4:].split("<")[0]
                                completo[portata].append(txt.replace('*',''))
                    menu = []
            for key in completo:
                if completo[key] == []:
                    completo[key] = [nomenu]
        except:
            for key in completo:
                completo[key] = errmenu
        mensaMenu[mensaList[x]] = completo
    return mensaMenu
