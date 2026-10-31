import re,base64,os
src='/workspace/moodboard/index.html'; out='/workspace/AI_Film_Hits_Moodboard.html'
s=open(src).read()
used=set(re.findall(r'img/[A-Za-z0-9_.\-]+\.jpg',s))
missing=[u for u in used if not os.path.exists('/workspace/moodboard/'+u)]
print('used',len(used),'missing',missing)
def rep(m):
    f='/workspace/moodboard/'+m.group(0)
    if not os.path.exists(f): return m.group(0)
    return 'data:image/jpeg;base64,'+base64.b64encode(open(f,'rb').read()).decode()
s=re.sub(r'img/[A-Za-z0-9_.\-]+\.jpg',rep,s)
open(out,'w').write(s)
print('size',os.path.getsize(out))
