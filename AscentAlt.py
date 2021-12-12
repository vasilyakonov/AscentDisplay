import random
import requests
import json
import pprint
from random_word import RandomWords

def getDictEntry(n):
    try:
        r = requests.get('https://dictionaryapi.com/api/v3/references/collegiate/json/%s?key=963bf68f-2d24-4142-9ae4-6d4ea286f2fe' % n)
        #print(r.json())
        dic=r.json()
        entry=dic[0]['def'][0]['sseq'][0][0][1]['dt'][0][1]
        sets='{bc}','{sx|','||}','{a_link|','}','{dx_defsee','{dxt|','||1','{/dx_def','{d_link|','|',':1',"'","(",")",'{/dx','{dxcompare','{it','{/it',"  ",
        for char in sets:
            entry=entry.replace(char,'')
        pp.pprint(entry)
    except TypeError:
        print('cannot open')


def fitImage(img,f,leftright=0.5,bottomtop=0.5,fit="short"):
    lr,bt = leftright,bottomtop
    ow, oh = imageSize(img)
    if fit == "short":
        s = f/oh if ow >= oh else f/ow
    elif fit == "long":
        s = f/ow if ow >= oh else f/oh
    w,h = ow*s,oh*s
    x,y = (width()-w)*lr,(height()-h)*bt
    #print(w,x,h,y)
    with savedState():
        scale(s)
        image(img, (x/s, y/s))

def strokeRect(r, g, b, a, n, xr, yr, wr, hr):
    fill(None)
    stroke(r, g, b, a)
    strokeWidth(n)
    rect(xr, yr, wr, hr)

r = RandomWords()
pp=pprint.PrettyPrinter()
frames=100
imgl=random.randrange(1,21)
img1=u'/Users/vasilij/Desktop/Bevel_Texturez/d%s.png' % imgl
w, h = imageSize(img1)
pix=15
color = []
for x in range(0, w, pix):
    # loop of the height of the image
    for y in range(0, h, pix):
        # get the color
        color.append(imagePixelColor(img1, (x, y)))
        
#print(color)
        
area = width()*1.0812
#openTypeFeatures(liga=True)
pos1=r.get_random_word(maxLength=9)
pos2=r.get_random_word(maxLength=9)
getDictEntry(pos1)
getDictEntry(pos2)
x1=830
y1=510
x2=150
y2=210
alpha1=0
alpha2=0
rectColor=random.choice(color)
r, g, b, a=rectColor

for i in range(frames):
    newPage(1920,1080)
    fitImage(img1,area)
    
    if len(pos1) <= 5:
        x1=810
    if len(pos1) > 5:
        x1=530
    if len(pos1) >= 7:
        x1=150
    if len(pos2) <= 5:
        x2=810
    if len(pos2) > 5:
        x2=530
    if len(pos2) >= 7:
        x2=150
    
    #strokeRect(r,g,b,0.8,30,110,110,1700,860)
    #strokeRect(r,g,b,0.8,30,15,15,1890,1050)
    #strokeRect(0,0,0,0.5,65,57.5+5,57.5+5,1795,955)
    
    
    frameDuration(0.05)
    font("/Users/vasilij/Desktop/DrawBot_Ascent-Medium.otf", 330)

    
    
    #y1=y1+(880/600)
    #y2=y2+(880/600)
    #till end of screen distance/time = time til end screen in sec
    #framerate * ttes in sec is alpha fade at end screen
    #don't forget that endscreen is -100 :)
    alpha1=alpha1+(1/100)
    alpha2=alpha2+(1/100)
    
    fill(r=1, g=1, b=1, alpha=alpha1)
    stroke(None)
    tracking(-10)
    # draw text
    #shadow((10, -10), 5, (r, g, b,alpha1))
    
    text(pos1.lower(), (x1, y1))
    
    
    fill(r=1, g=1, b=1, alpha=alpha2)
    stroke(None)
    tracking(-10)
    #shadow((10, -10), 5, (r, g, b,alpha2))
    
    text(pos2.lower(), (x2, y2))
    
    
for i in range(frames):
    newPage(1920,1080)
    fitImage(img1,area)
    
    if len(pos1) <= 5:
        x1=810
    if len(pos1) > 5:
        x1=530
    if len(pos1) >= 7:
        x1=150
    if len(pos2) <= 5:
        x2=810
    if len(pos2) > 5:
        x2=530
    if len(pos2) >= 7:
        x2=150
    
    #strokeRect(r,g,b,0.8,30,110,110,1700,860)
    #strokeRect(r,g,b,0.8,30,15,15,1890,1050)
    #strokeRect(0,0,0,0.5,65,57.5+5,57.5+5,1795,955)
    
    
    frameDuration(0.05)
    font("/Users/vasilij/Desktop/DrawBot_Ascent-Medium.otf", 330)

    
    
    y1=y1+(880/600)
    y2=y2+(880/600)
    #till end of screen distance/time = time til end screen in sec
    #framerate * ttes in sec is alpha fade at end screen
    #don't forget that endscreen is -100 :)
    alpha1=alpha1-(1/155)
    alpha2=alpha2-(1/375)
    
    fill(r=1, g=1, b=1, alpha=alpha1)
    stroke(None)
    tracking(-10)
    # draw text
    #shadow((10, -10), 5, (r, g, b,alpha1))
    
    text(pos1.lower(), (x1, y1))
    
    
    fill(r=1, g=1, b=1, alpha=alpha2)
    stroke(None)
    tracking(-10)
    #shadow((10, -10), 5, (r, g, b,alpha2))
    
    text(pos2.lower(), (x2, y2))
    

for i in range(frames):
    newPage(1920,1080)
    fitImage(img1,area)
    
    if len(pos1) <= 5:
        x1=810
    if len(pos1) > 5:
        x1=530
    if len(pos1) >= 7:
        x1=150
    if len(pos2) <= 5:
        x2=810
    if len(pos2) > 5:
        x2=530
    if len(pos2) >= 7:
        x2=150
    
    #strokeRect(r,g,b,0.8,30,110,110,1700,860)
    #strokeRect(r,g,b,0.8,30,15,15,1890,1050)
    #strokeRect(0,0,0,0.5,65,57.5+5,57.5+5,1795,955)
    
    
    frameDuration(0.05)
    font("/Users/vasilij/Desktop/DrawBot_Ascent-Medium.otf", 330)

    
    
    y1=y1+(880/600)
    y2=y2+(880/600)
    #till end of screen distance/time = time til end screen in sec
    #framerate * ttes in sec is alpha fade at end screen
    #don't forget that endscreen is -100 :)
    alpha1=alpha1-(1/155)
    alpha2=alpha2-(1/375)
    
    fill(r=1, g=1, b=1, alpha=alpha1)
    stroke(None)
    tracking(-10)
    # draw text
    #shadow((10, -10), 5, (r, g, b,alpha1))
    
    text(pos1.lower(), (x1, y1))
    
    
    fill(r=1, g=1, b=1, alpha=alpha2)
    stroke(None)
    tracking(-10)
    #shadow((10, -10), 5, (r, g, b,alpha2))
    
    text(pos2.lower(), (x2, y2))
    
    
for i in range(frames):
    newPage(1920,1080)
    fitImage(img1,area)
    
    if len(pos1) <= 5:
        x1=810
    if len(pos1) > 5:
        x1=530
    if len(pos1) >= 7:
        x1=150
    if len(pos2) <= 5:
        x2=810
    if len(pos2) > 5:
        x2=530
    if len(pos2) >= 7:
        x2=150
    
    #strokeRect(r,g,b,0.8,30,110,110,1700,860)
    #strokeRect(r,g,b,0.8,30,15,15,1890,1050)
    #strokeRect(0,0,0,0.5,65,57.5+5,57.5+5,1795,955)
    
    
    frameDuration(0.05)
    font("/Users/vasilij/Desktop/DrawBot_Ascent-Medium.otf", 330)

    
    
    y1=y1+(880/600)
    y2=y2+(880/600)
    #till end of screen distance/time = time til end screen in sec
    #framerate * ttes in sec is alpha fade at end screen
    #don't forget that endscreen is -100 :)
    alpha1=alpha1-(1/155)
    alpha2=alpha2-(1/375)
    
    fill(r=1, g=1, b=1, alpha=alpha1)
    stroke(None)
    tracking(-10)
    # draw text
    #shadow((10, -10), 5, (r, g, b,alpha1))
    
    text(pos1.lower(), (x1, y1))
    
    
    fill(r=1, g=1, b=1, alpha=alpha2)
    stroke(None)
    tracking(-10)
    #shadow((10, -10), 5, (r, g, b,alpha2))
    
    text(pos2.lower(), (x2, y2))
    

for i in range(frames):
    newPage(1920,1080)
    fitImage(img1,area)
    
    if len(pos1) <= 5:
        x1=810
    if len(pos1) > 5:
        x1=530
    if len(pos1) >= 7:
        x1=150
    if len(pos2) <= 5:
        x2=810
    if len(pos2) > 5:
        x2=530
    if len(pos2) >= 7:
        x2=150
    
    #strokeRect(r,g,b,0.8,30,110,110,1700,860)
    #strokeRect(r,g,b,0.8,30,15,15,1890,1050)
    #strokeRect(0,0,0,0.5,65,57.5+5,57.5+5,1795,955)
    
    
    frameDuration(0.05)
    font("/Users/vasilij/Desktop/DrawBot_Ascent-Medium.otf", 330)

    
    
    y1=y1+(880/600)
    y2=y2+(880/600)
    #till end of screen distance/time = time til end screen in sec
    #framerate * ttes in sec is alpha fade at end screen
    #don't forget that endscreen is -100 :)
    alpha1=alpha1-(1/155)
    alpha2=alpha2-(1/375)
    
    fill(r=1, g=1, b=1, alpha=alpha1)
    stroke(None)
    tracking(-10)
    # draw text
    #shadow((10, -10), 5, (r, g, b,alpha1))
    
    text(pos1.lower(), (x1, y1))
    
    
    fill(r=1, g=1, b=1, alpha=alpha2)
    stroke(None)
    tracking(-10)
    #shadow((10, -10), 5, (r, g, b,alpha2))
    
    text(pos2.lower(), (x2, y2))
    

for i in range(frames):
    newPage(1920,1080)
    fitImage(img1,area)
    
    if len(pos1) <= 5:
        x1=810
    if len(pos1) > 5:
        x1=530
    if len(pos1) >= 7:
        x1=150
    if len(pos2) <= 5:
        x2=810
    if len(pos2) > 5:
        x2=530
    if len(pos2) >= 7:
        x2=150
    
    #strokeRect(r,g,b,0.8,30,110,110,1700,860)
    #strokeRect(r,g,b,0.8,30,15,15,1890,1050)
    #strokeRect(0,0,0,0.5,65,57.5+5,57.5+5,1795,955)
    
    
    frameDuration(0.05)
    font("/Users/vasilij/Desktop/DrawBot_Ascent-Medium.otf", 330)

    
    
    y1=y1+(880/600)
    y2=y2+(880/600)
    #till end of screen distance/time = time til end screen in sec
    #framerate * ttes in sec is alpha fade at end screen
    #don't forget that endscreen is -100 :)
    alpha1=alpha1-(1/155)
    alpha2=alpha2-(1/375)
    
    fill(r=1, g=1, b=1, alpha=alpha1)
    stroke(None)
    tracking(-10)
    # draw text
    #shadow((10, -10), 5, (r, g, b,alpha1))
    
    text(pos1.lower(), (x1, y1))
    
    
    fill(r=1, g=1, b=1, alpha=alpha2)
    stroke(None)
    tracking(-10)
    #shadow((10, -10), 5, (r, g, b,alpha2))
    
    text(pos2.lower(), (x2, y2))
    


    
 
saveImage("~/Desktop/AscentAlt.mp4")