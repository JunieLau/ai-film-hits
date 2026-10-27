import re,base64,os
src=os.path.join(os.path.dirname(__file__),'index.html')
out=os.path.join(os.path.dirname(__file__),'..','AI_Film_Hits_Moodboard.html')
s=open(src,encoding='utf-8').read()
imgdir=os.path.join(os.path.dirname(__file__),'img')
used=set(re.findall(r'img/[A-Za-z0-9_.\-]+\.jpg',s))
missing=[u for u in used if not os.path.exists(os.path.join(imgdir,os.path.basename(u)))]
print('used',len(used),'missing',len(missing))
def rep(m):
    f=os.path.join(imgdir,os.path.basename(m.group(0)))
    if not os.path.exists(f): return m.group(0)
    return 'data:image/jpeg;base64,'+base64.b64encode(open(f,'rb').read()).decode()
s=re.sub(r'img/[A-Za-z0-9_.\-]+\.jpg',rep,s)
open(out,'w',encoding='utf-8').write(s)
print('wrote',out,'size',os.path.getsize(out))
