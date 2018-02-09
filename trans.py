#!/usr/bin/python3
'''
    Copyright (C) 2018 apple502j All rights reserved.
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''
import mw_api_client as mw
import requests as req
import getpass

if True:
    server=input('Server >')
    server2=input('To Server >')
    username=input('Username >')
    password=getpass.getpass('Password >')
    wiki=mw.Wiki('https://' + server2 + '/w/api.php','ImageTransport by Apple502j python3-requests')
    wiki.login(username,password)
    while True:
        imagebase=input('Image >')
        image=imagebase.replace(' ','_')
        imageurl='https://' + server + '/w/images/' + image
        imgfile=req.get(imageurl)
        if imgfile.status_code > 400:
            continue
        toname=input('To Filename >')
        page=input('File Page >')
        page=page+"<!-- Script upload: if something is wrong, please call Apple502j -->"
wiki.upload(imgfile.content,toname,comment=page)
