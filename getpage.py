import urllib.request
import re
import os

def dlpage(rootpath,p0,pt):
    rtz0='http://www.rtz.cc/ji/BeautyLeg%num.html'
    Rtz=[' ','http://www.rtz.cc/ji/BeautyLeg.html']

    for i in range(p0,pt):
        Rtz=Rtz+[re.sub('%num',str(i),rtz0)]
    try:
        os.makedirs(rootpath+"\\pages")
    except:
        pass
    re1='<a href="/html/xinggan'
    for i in range(1,35):
        print('downloading page: '+str(i))
        #page=download(Rtz[i])
        try:
            urllib.request.urlretrieve(Rtz[i],rootpath+'\\pages\\'+str(i)+'.txt')
        except:
            print('page '+str(i)+' failed')