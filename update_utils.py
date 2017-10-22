from bs4 import BeautifulSoup
import requests



def getcal():
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
    # print(listCal)
    # listCal = [1 for x in range(14)]
    if listCal is not None:
        mensaList = ['sanfrancesco', 'piovego', 'agripolis', 'acli', 'belzoni', 'forcellini', 'murialdo']
        x = 0
        for mensa in mensaList:
            mensaDict[mensa] = {}
            mensaDict[mensa]["pranzo"] = listCal[x]
            mensaDict[mensa]["cena"] = listCal[x + 1]
            x += 2
    return mensaDict




# a = 0
# if cal is not None:
#     for x in range(7):
#         mensaDict[mensaList[x]]['calendario']['pranzo'] = cal[a]
#         mensaDict[mensaList[x]]['calendario']['cena'] = cal[a + 1]
#         a += 2

# print(mensaDict)