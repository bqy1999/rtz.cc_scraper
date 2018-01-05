import urllib.request
import re
import os
import sys
import getpage

re1='\d{5,5}.htm'
re2='.htm'
re3='\d{2,2}$'

rootpath=sys.argv[1]
p0=int(sys.argv[2])
pt=int(sys.argv[3])+1

getpage.dlpage(rootpath,p0,pt)

for i in range(p0,pt):
    try:
        print('processing: page '+str(i))
        with open(rootpath+'\\pages\\'+str(i)+'.txt') as F:
            time=0
            for num in re.findall(re1,F.read()):
                time=time+1
                num=re.sub(re2,"",num)
                num2=re.sub(re3,"",num)
                if (True):
                    url0="http://tu.darengou.net:8091/pic"+num2+"/"+num+"-"
                    dir0=rootpath+"\\imgs\\"+num+"\\"
                    #print(num)
                    if (time % 2==1):
                        try:
                            os.makedirs(dir0)
                        except:
                            pass
                        for imgtime in range(1,100):
                            url1=url0+str(imgtime)+".jpg"
                            dir1=dir0+str(imgtime)+".jpg"
                            try:
                                urllib.request.urlretrieve(url1,dir1)
                                with open(dir1,'wb') as F2:
                                    F2.write(urllib.request.urlopen(url1,timeout=5).read())
                                print(num+" "+str(imgtime)+" finished")
                            except:
                                print(dir1)
                                print(url1)
                                print(num+" "+str(imgtime)+" error")
                                break
    except:
        print('failed when processing page '+str(i))
                        
                    
            