'''
Created on Aug. 21, 2021

@author: Tao
'''

from flask import Flask, render_template
import webscraper
test = (str(webscraper.lastupdate))

durhamdata = webscraper.durham
durham0 = str(durhamdata[0])
durham0 = durham0.replace(",", "")
durham1 = str(durhamdata[1])
durham1 = durham1.replace(",", "")
durham2 = str(durhamdata[2])
durham2 = durham2.replace(",", "")

durham3 = str(durhamdata[3])
durham3 = durham3.replace(",", "")
durham4 = str(durhamdata[4])
durham4 = durham4.replace(",", "")

haltondata = webscraper.halton
halton0 = str(haltondata[0])
halton0 = halton0.replace(",", "")
halton1 = str(haltondata[1])
halton1 = halton1.replace(",", "")
halton2 = str(haltondata[2])
halton2 = halton2.replace(",", "")
halton3 = str(haltondata[3])
halton3 = halton3.replace(",", "")
halton4 = str(haltondata[4])
halton4 = halton4.replace(",", "")

peeldata = webscraper.peel
peel0 = str(peeldata[0])
peel0 = peel0.replace(",", "")
peel1 = str(peeldata[1])
peel1 = peel1.replace(",", "")
peel2 = str(peeldata[2])
peel2 = peel2.replace(",", "")
peel3 = str(peeldata[3])
peel3 = peel3.replace(",", "")
peel4 = str(peeldata[4])
peel4 = peel4.replace(",", "")

torontodata = webscraper.toronto
toronto0 = str(torontodata[0])
toronto0 = toronto0.replace(",", "")
toronto1 = str(torontodata[1])
toronto1 = toronto1.replace(",", "")
toronto2 = str(torontodata[2])
toronto2 = toronto2.replace(",", "")
toronto3 = str(torontodata[3])
toronto3 = toronto3.replace(",", "")
toronto4 = str(torontodata[4])
toronto4 = toronto4.replace(",", "")

yorkdata = webscraper.york
york0 = str(yorkdata[0])
york0 = york0.replace(",", "")
york1 = str(yorkdata[1])
york1 = york1.replace(",", "")
york2 = str(yorkdata[2])
york2 = york2.replace(",", "")
york3 = str(yorkdata[3])
york3 = york3.replace(",", "")
york4 = str(yorkdata[4])
york4 = york4.replace(",", "")

GTA0 = str(int(durham0) + int(halton0) + int(peel0) + int(toronto0) + int(york0))
if not "-" in GTA0:
    GTA0 = "+" + GTA0
GTA1 = str(int(durham1) + int(halton1) + int(peel1) + int(toronto1) + int(york1))
GTA2 = str(int(durham2) + int(halton2) + int(peel2) + int(toronto2) + int(york2))
GTA3 = str(int(durham3) + int(halton3) + int(peel3) + int(toronto3) + int(york3))
GTA4 = str(int(durham4) + int(halton4) + int(peel4) + int(toronto4) + int(york4))

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def Covid6ix():
    return render_template('Covid6ix.html')

@app.route("/GTA")
def GTA():
    return render_template('GTA.html', test=test, GTA0=GTA0, GTA1=GTA1, GTA2=GTA2, GTA3=GTA3, GTA4=GTA4)

@app.route("/durham")
def durham():
    return render_template('durham.html', test=test, durham0=durham0, durham1=durham1, durham2=durham2, durham3=durham3, durham4=durham4)

@app.route("/halton")
def halton():
    return render_template('halton.html', test=test, halton0=halton0, halton1=halton1, halton2=halton2, halton3=halton3, halton4=halton4)

@app.route("/peel")
def peel():
    return render_template('peel.html', test=test, peel0=peel0, peel1=peel1, peel2=peel2, peel3=peel3, peel4=peel4)

@app.route("/toronto")
def toronto():
    return render_template('toronto.html', test=test, toronto0=toronto0, toronto1=toronto1, toronto2=toronto2, toronto3=toronto3, toronto4=toronto4)

@app.route("/york")
def york():
    return render_template('york.html', test=test, york0=york0, york1=york1, york2=york2, york3=york3, york4=york4)

if __name__ == "__main__":
    app.run()