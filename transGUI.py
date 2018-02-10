#! /usr/bin/python3
import tkinter as tki
import tkinter.messagebox as tkm
import requests as req
import mw_api_client as mw

DEFAULTWIKI=""
DEFAULTWIKI2=""
DEFAULTUSER=""
DEFAULTPASS=""
DEFAULTFILE=""
DEFAULTFILE2=""

USERAGENT="TransGUI v1.0 by apple502j, using requests"
global w

# Buttons define

def login(ev):
    global w
    un=boxUsername.get()
    sv=boxServer2.get()
    passwd=boxPassword.get()
    w=mw.Wiki("https://"+sv+"/w/api.php",USERAGENT)
    w.login(un,passwd)
    tkm.showinfo('Done','Login done')

def upload(ev):
    global w
    image=boxFilename.get().replace(' ','_')
    sv=boxServer.get()
    imageinfo=req.get("https://"+sv+"/w/api.php?action=query&format=json&prop=imageinfo&redirects=1&iiprop=url&titles="+image).json()
    image_2=list(imageinfo["query"]["pages"].keys())[0]
    image_3=imageinfo["query"]["pages"][image_2]
    imageurl=image_3["imageinfo"][0]["url"]
    imgfile=req.get(imageurl)
    if imgfile.status_code > 400:
        return
    page=boxPage.get()+"<!-- Script upload: if something is wrong, please call "+boxUsername.get()+" -->"
    print(w.upload(imgfile.content,boxFilename2.get().replace("File:",""),comment=page))
    print("done")

# Tkinter shortcut
def box(defv="",size=0,xpos=0,ypos=0,show=""):
    if size != 0:
        x=tki.Entry(width=size,show=show)
    else:
        x=tki.Entry(show=show)
    x.insert(tki.END,defv)
    x.place(x=xpos,y=ypos)
    return x

def label(v="",xpos=0,ypos=0):
    x=tki.Label(text=v)
    x.place(x=xpos,y=ypos)
    return x

def button(func,size=10,v="Button",xpos=0,ypos=0):
    x=tki.Button(text=v,width=size)
    x.bind("<Button-1>",func)
    x.place(x=xpos,y=ypos)
    return x

if True:
    root=tki.Tk()
    root.geometry("480x360")
    root.title("Transport Files")
    
    label("Server",10,10)
    boxServer=box(DEFAULTWIKI,20,80,10)

    label("To Server",10,40)
    boxServer2=box(DEFAULTWIKI2,20,80,40)

    label("Username",10,70)
    boxUsername=box(DEFAULTUSER,20,80,70)

    label("Password",10,100)
    boxPassword=box(DEFAULTPASS,20,80,100,"*")

    btnLogin=button(login,10,"Login",250,10)

    label("Filename",10,130)
    boxFilename=box(DEFAULTFILE,20,80,130)

    label("Filename 2",10,160)
    boxFilename2=box(DEFAULTFILE2,20,80,160)

    label("Page",10,190)
    boxPage=box("",20,80,190)

    btnUpload=button(upload,10,"Upload",250,50)

root.mainloop()
