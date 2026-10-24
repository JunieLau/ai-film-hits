import re,base64,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR=os.path.join(ROOT,'src')
src=os.path.join(SRC_DIR,'index.html')
out=os.path.join(ROOT,'index.html')
s=open(src).read()
used=set(re.findall(r'img/[A-Za-z0-9_.\-]+\.jpg',s))
missing=[u for u in used if not os.path.exists(os.path.join(SRC_DIR,u))]
print('used',len(used),'missing',missing)
def rep(m):
    f=os.path.join(SRC_DIR,m.group(0))
    if not os.path.exists(f): return m.group(0)
    return 'data:image/jpeg;base64,'+base64.b64encode(open(f,'rb').read()).decode()
s=re.sub(r'img/[A-Za-z0-9_.\-]+\.jpg',rep,s)
open(out,'w').write(s)
print('size',os.path.getsize(out))
