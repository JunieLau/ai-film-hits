"""Build the single-file site: inline src/img/*.jpg as base64 into ../index.html.
Run from anywhere:  python3 src/build.py"""
import re,base64,os
HERE=os.path.dirname(os.path.abspath(__file__))
ROOT=os.path.dirname(HERE)
src=os.path.join(HERE,'index.html'); out=os.path.join(ROOT,'index.html')
s=open(src,encoding='utf-8').read()
used=set(re.findall(r'img/[A-Za-z0-9_.\-]+\.jpg',s))
missing=[u for u in used if not os.path.exists(os.path.join(HERE,u))]
print('used',len(used),'missing',missing)
def rep(m):
    f=os.path.join(HERE,m.group(0))
    if not os.path.exists(f): return m.group(0)
    return 'data:image/jpeg;base64,'+base64.b64encode(open(f,'rb').read()).decode()
s=re.sub(r'img/[A-Za-z0-9_.\-]+\.jpg',rep,s)
open(out,'w',encoding='utf-8').write(s)
print('size',os.path.getsize(out))
