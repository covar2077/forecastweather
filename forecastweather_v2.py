import requests
from bs4 import BeautifulSoup
from datetime import date
today = date.today()
d = today.strftime("%B")
months = {"January":"ΙΑΝΟΥΑΡΙΟΥ", "February":"ΦΕΒΡΟΥΑΡΙΟΥ", "March":"ΜΑΡΤΙΟΥ", "April":"ΑΠΡΙΛΙΟΥ", "May":"ΜΑΪΟΥ", "June":"ΙΟΥΝΙΟΥ", "July":"ΙΟΥΛΙΟΥ", "August":"ΑΥΓΟΥΣΤΟΥ", "September":"ΣΕΠΤΕΜΒΡΙΟΥ", "October":"ΟΚΤΩΒΡΙΟΥ", "November":"ΝΟΕΜΒΡΙΟΥ", "December":"ΔΕΚΕΜΒΡΙΟΥ"}
mo = months.get(d)
res = requests.get("https://www.forecastweather.gr/%CF%80%CF%81%CE%BF%CE%B3%CE%BD%CF%89%CF%83%CE%B7/%CE%B5%CE%BB%CE%BB%CE%B1%CE%B4%CE%B1/%CE%BD%CE%B7%CF%83%CE%B9%CE%B1-%CE%B2-%CE%B1-%CE%B1%CE%B9%CE%B3%CE%B1%CE%B9%CE%BF/%CF%87%CE%B9%CE%BF%CF%83.html")
soup = BeautifulSoup(res.content, "html.parser")

table = soup.find("div", class_="prognosis")
prog = table.find_all("div", class_="prognosis-in")
dates = []
for i in prog:
    dat = i.find("div", class_="day").get_text()
    dates.append(dat)
print (len(dates))

nl = "\n"
print(f"ΠΡΟΓΝΩΣΗ ΚΑΙΡΟΥ ΧΙΟΥ ΓΙΑ ΤΙΣ ΕΞΗΣ ΗΜΕΡΕΣ ΤΟΥ ΜΗΝΑ {mo} (ΕΠΙΛΕΞΤΕ ΑΡΙΘΜΟ):")
myls = []
for idx, word in enumerate(dates):
    myls.append(idx)
    print(f"{idx}. {word}")
print(f"{len(dates)}. ΟΛΕΣ ΤΙΣ ΜΕΡΕΣ")


def kairos_all():
    for index, val in enumerate(dates):
        table0 = table.find_all("div", class_="prognosis-in")[index]
        date = table0.find("div", class_="day").get_text()
        sun = table0.find("div", class_="syn").get_text()
        print (date, sun)
        trs = table0.find_all("tr")
        for i in trs:
            hour = i.find_all("td")[0].get_text()
            temp = i.find_all("td")[1].get_text()
            moisture = i.find_all("td")[2].get_text()
            wind = i.find_all("td")[3].get_text()
            clouds = i.find_all("td")[4].get_text()
            print(hour, temp, moisture, wind, clouds)

def kairos(ch):
    table0 = table.find_all("div", class_="prognosis-in")[ch]
    date = table0.find("div", class_="day").get_text()
    sun = table0.find("div", class_="syn").get_text()
    print (date, sun)
    trs = table0.find_all("tr")
    for i in trs:
        hour = i.find_all("td")[0].get_text()
        temp = i.find_all("td")[1].get_text()
        moisture = i.find_all("td")[2].get_text()
        wind = i.find_all("td")[3].get_text()
        clouds = i.find_all("td")[4].get_text()
        print(hour, temp, moisture, wind, clouds)

def check():
    chck = input("ΘΕΛΕΤΕ ΝΑ ΣΥΝΕΧΙΣΕΤΕ? y/n \n")
    if chck == "y":
        choice ()
    elif chck == "n":
        return True
    else: return check()

def choice():
    ch = input("Η ΕΠΙΛΟΓΗ ΣΑΣ ΕΙΝΑΙ: ")
    x = int(ch)
    if x in myls:
        kairos(x), check()
    elif x == len(dates):
        kairos_all(), check()
    else:
        check()


choice()
