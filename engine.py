import os,json,urllib.request as U,random as R0
V=(0,100,320,330,500,900,20000)
D=b'\x88\x88\xbd\xedy\xbby\x99h\x89y\x88i\x87\x88\x88\x05HW\xca\x8c\xdd\x89\xbby\x99x\x99f\x88GVxFi\x98z\xba\x88\xab\x89\x9a\x89\x99\x8a\x98gw\xaa\x9c\xaa\xcc\x8a\xaaw\x9agxg\x88G\x88v\x89\x89\xaa\x98\xa8\x99\xa9w\x87\x87\x88\x88\x88x\x98fxiv\x87xy\x87gvWewe\x88u\x8a\x87'
_PM=tuple(tuple(sum(([((D[p*16+r*2+(f>>1)]>>(4*(1-(f&1)))&15)*16-128)for f in range(4)]+[((D[p*16+r*2+(f>>1)]>>(4*(1-(f&1)))&15)*16-128)for f in range(3,-1,-1)]for r in range(8)),[]))for p in range(6))
PM=tuple(tuple(V[p+1]+_PM[p][ix]for ix in range(64))for p in range(6))
PE=tuple(tuple(V[p+1]+(((6-(ix>>3))*25)if p==0 else((30-5*(abs(2*(ix>>3)-7)+abs(2*(ix&7)-7)))if p==5 else _PM[p][ix]//2))for ix in range(64))for p in range(6))
S64=tuple(r*16+f for r in range(8)for f in range(8))
PW=(0,0,1,1,2,4,0)
G=R0.Random(7).getrandbits
Z=tuple(G(64)for _ in range(1808))
ND=(-33,-31,-18,-14,14,18,31,33)
KD=(-17,-16,-15,-1,1,15,16,17)
BD=(-17,-15,15,17)
RD=(-16,-1,1,16)
QD=BD+RD
BK={():"e2e4",("e2e4",):"c7c5",("d2d4",):"d7d5",("c2c4",):"e7e5",("g1f3",):"d7d5",("e2e4","c7c5"):"g1f3",("e2e4","e7e5"):"g1f3",("d2d4","d7d5"):"c2c4",("e2e4","c7c5","g1f3"):"d7d6",("e2e4","e7e5","g1f3"):"b8c6"}
NN=80000
class E:
 def __init__(s):
  b=[0]*128;bk=(4,2,3,5,6,3,2,4)
  for f in range(8):b[f]=-bk[f];b[16+f]=-1;b[96+f]=1;b[112+f]=bk[f]
  s.b=b;s.s=1;s.c=15;s.ep=-1;s.hm=0;s.ks={1:116,-1:4};s.hh={};s.tt={};s.kl=[[0,0]for _ in range(64)];s.hs={};s.nd=0;s.st=0
  h=Z[1679];mg=eg=ph=wb=bb=0;s.wp=[0]*8;s.bp=[0]*8
  for q in S64:
   p=b[q]
   if p:
    h^=Z[(p+6)*128+q];pt=abs(p);sg=1 if p>0 else -1;ph+=PW[pt]
    ix=((7-(q>>4)if sg<0 else(q>>4))<<3)|(q&7)
    mg+=sg*PM[pt-1][ix];eg+=sg*PE[pt-1][ix]
    if pt==3:
     if p>0:wb+=1
     else:bb+=1
    elif pt==1:
     if p>0:s.wp[q&7]+=1
     else:s.bp[q&7]+=1
  s.h=h;s.mg=mg;s.eg=eg;s.ph=ph;s.bc={1:wb,-1:bb}
 def att(s,q,by):
  b=s.b;pd=16*by
  for df in(-1,1):
   p=q+pd+df
   if not p&136 and b[p]==by:return 1
  for ds,tg in((ND,2*by),(KD,6*by)):
   for d in ds:
    p=q+d
    if not p&136 and b[p]==tg:return 1
  for ds,t1 in((BD,3*by),(RD,4*by)):
   for d in ds:
    p=q+d
    while not p&136:
     v=b[p]
     if v:
      if v==t1 or v==5*by:return 1
      break
     p+=d
  return 0
 def gen(s,cp=0):
  b=s.b;sd=s.s;ep=s.ep;mv=[];pd=-16*sd;sr=6 if sd>0 else 1;prr=7-sr
  for q in S64:
   p=b[q]
   if p*sd<=0:continue
   pt=abs(p)
   if pt==1:
    r=q>>4;to=q+pd
    if not to&136 and not b[to]:
     if r==prr:mv+=[(q,to,pr)for pr in(5,4,3,2)]
     elif not cp:
      mv.append((q,to,0))
      if r==sr and not b[to+pd]:mv.append((q,to+pd,0))
    for df in(-1,1):
     to=q+pd+df
     if not to&136:
      c=b[to]
      if c*sd<0:
       if r==prr:mv+=[(q,to,pr)for pr in(5,4,3,2)]
       else:mv.append((q,to,0))
      elif to==ep:mv.append((q,to,0))
   elif pt in(2,6):
    for d in(ND if pt==2 else KD):
     to=q+d
     if not to&136:
      c=b[to]
      if c*sd<=0 and(not cp or c):mv.append((q,to,0))
    if pt==6 and not cp and q==(116 if sd>0 else 4):
     for fl,e1,e2,e3,rk in((1 if sd>0 else 4,q+1,q+2,0,q+3),(2 if sd>0 else 8,q-1,q-2,q-3,q-4)):
      if s.c&fl and b[rk]==4*sd and not b[e1]and not b[e2]and(not e3 or not b[e3])and not s.att(q,-sd)and not s.att(e1,-sd)and not s.att(e2,-sd):mv.append((q,e2,0))
   else:
    for d in(BD if pt==3 else(RD if pt==4 else QD)):
     to=q+d
     while not to&136:
      c=b[to]
      if not c:
       if not cp:mv.append((q,to,0))
      else:
       if c*sd<0:mv.append((q,to,0))
       break
      to+=d
  return mv
 def mk(s,m):
  fr,to,pr=m;b=s.b;sd=s.s;p=b[fr];cp=b[to]
  st=(cp,s.c,s.ep,s.hm,s.h,s.ks[sd],s.mg,s.eg,s.ph,s.bc[1],s.bc[-1])
  h=s.h^Z[1664+s.c]^Z[1807]
  if s.ep>=0:h^=Z[1680+s.ep]
  pt=abs(p);ixf=((7-(fr>>4)if sd<0 else(fr>>4))<<3)|(fr&7);ixt=((7-(to>>4)if sd<0 else(to>>4))<<3)|(to&7)
  s.mg-=sd*PM[pt-1][ixf];s.eg-=sd*PE[pt-1][ixf]
  b[fr]=0;h^=Z[(p+6)*128+fr]
  if pt==1:
   if sd>0:s.wp[fr&7]-=1
   else:s.bp[fr&7]-=1
  if cp:
   cpt=abs(cp);s.ph-=PW[cpt];s.mg+=sd*PM[cpt-1][ixt^56];s.eg+=sd*PE[cpt-1][ixt^56];h^=Z[(cp+6)*128+to]
   if cpt==3:s.bc[-sd]-=1
   elif cpt==1:
    if sd>0:s.bp[to&7]-=1
    else:s.wp[to&7]-=1
  epc=0
  if pt==1 and to==s.ep:
   es=to+16*sd;epc=1;ixe=((7-(es>>4)if -sd<0 else(es>>4))<<3)|(es&7)
   s.mg+=sd*PM[0][ixe];s.eg+=sd*PE[0][ixe];h^=Z[(b[es]+6)*128+es];b[es]=0
   if sd>0:s.bp[es&7]-=1
   else:s.wp[es&7]-=1
  np=pr*sd if pr else p;npt=pr if pr else pt
  if pr:s.ph+=PW[pr]-PW[1]
  elif pt==1:
   if sd>0:s.wp[to&7]+=1
   else:s.bp[to&7]+=1
  s.mg+=sd*PM[npt-1][ixt];s.eg+=sd*PE[npt-1][ixt];b[to]=np;h^=Z[(np+6)*128+to]
  if pt==6:
   s.ks[sd]=to
   if abs(to-fr)==2:
    rf,rt=(fr+3,fr+1)if to==fr+2 else(fr-4,fr-1);rp=b[rf];b[rf]=0;b[rt]=rp;h^=Z[(rp+6)*128+rf]^Z[(rp+6)*128+rt]
    irf=((7-(rf>>4)if sd<0 else(rf>>4))<<3)|(rf&7);irt=((7-(rt>>4)if sd<0 else(rt>>4))<<3)|(rt&7)
    s.mg+=sd*(PM[3][irt]-PM[3][irf]);s.eg+=sd*(PE[3][irt]-PE[3][irf])
  nc=s.c
  cm={116:12,119:14,112:13,4:3,7:11,0:7};nc&=cm.get(fr,15)&cm.get(to,15)
  s.c=nc;h^=Z[1664+nc];nep=(fr+to)>>1 if pt==1 and abs(to-fr)==32 else -1
  if nep>=0:h^=Z[1680+nep]
  s.ep=nep;s.hm=0 if pt==1 or cp or epc else s.hm+1;s.s=-sd;s.h=h;return st
 def umk(s,m,st):
  fr,to,pr=m;cp,c,ep,hm,h,ok,mg,eg,ph,wb,bb=st
  s.s=-s.s;sd=s.s;b=s.b;p=sd if pr else b[to];b[fr]=p;b[to]=cp
  pt=abs(p)
  if pt==1:
   if sd>0:s.wp[fr&7]+=1
   else:s.bp[fr&7]+=1
   if not pr:
    if sd>0:s.wp[to&7]-=1
    else:s.bp[to&7]-=1
  if cp:
   if abs(cp)==1:
    if sd>0:s.bp[to&7]+=1
    else:s.wp[to&7]+=1
  if pt==1 and to==ep:
   es=to+16*sd;b[es]=-sd
   if sd>0:s.bp[es&7]+=1
   else:s.wp[es&7]+=1
  if pt==6:
   s.ks[sd]=ok
   if abs(to-fr)==2:rf,rt=(fr+3,fr+1)if to==fr+2 else(fr-4,fr-1);b[rf]=b[rt];b[rt]=0
  s.c=c;s.ep=ep;s.hm=hm;s.h=h;s.mg=mg;s.eg=eg;s.ph=ph;s.bc[1]=wb;s.bc[-1]=bb
 def ev(s):
  ph=24 if s.ph>24 else s.ph
  mg=s.mg+(35 if s.bc[1]>1 else 0)-(35 if s.bc[-1]>1 else 0)
  eg=s.eg+(50 if s.bc[1]>1 else 0)-(50 if s.bc[-1]>1 else 0)
  # Doubled pawn & isolated pawn penalty + king shield
  wp=s.wp;bp=s.bp;dp=0
  for f in range(8):
   if wp[f]>1:dp-=15*(wp[f]-1)
   if bp[f]>1:dp+=15*(bp[f]-1)
   if wp[f]and(f==0 or not wp[f-1])and(f==7 or not wp[f+1]):dp-=12*wp[f]
   if bp[f]and(f==0 or not bp[f-1])and(f==7 or not bp[f+1]):dp+=12*bp[f]
  mg+=dp;eg+=dp
  sc=(mg*ph+eg*(24-ph))//24
  if ph<8 and abs(sc)>250:
   wk,bk=s.ks[1],s.ks[-1];wr,wf,br,bf=wk>>4,wk&7,bk>>4,bk&7
   md=abs(wr-br)+abs(wf-bf)
   if sc>0:sc+=(14-md)*8+(abs(2*br-7)+abs(2*bf-7))*10
   else:sc-=(14-md)*8+(abs(2*wr-7)+abs(2*wf-7))*10
  return sc*s.s
 def sm(s,m,tm,pl):
  if m==tm:return 10000000
  fr,to,pr=m;c=s.b[to]
  if c:return 1000000+V[abs(c)]*10-V[abs(s.b[fr])]//10
  if pr:return 900000+pr
  if abs(s.b[fr])==1 and to==s.ep:return 1000900
  k=s.kl[pl];return 800000 if m==k[0]else(700000 if m==k[1]else s.hs.get((fr,to),0))
 def qs(s,a,b,pl):
  s.nd+=1
  if s.nd>=NN:s.st=1;return 0
  st=s.ev()
  if st>=b:return b
  if a<st:a=st
  mvs=s.gen(1);mvs.sort(key=lambda m:s.sm(m,None,pl),reverse=1);sd=s.s
  for m in mvs:
   c=s.b[m[1]]
   if c and st+V[abs(c)]+200<a and not m[2]:continue
   u=s.mk(m)
   if s.att(s.ks[sd],-sd):s.umk(m,u);continue
   sc=-s.qs(-b,-a,pl+1);s.umk(m,u)
   if s.st:return 0
   if sc>=b:return b
   if sc>a:a=sc
  return a
 def ab(s,d,a,b,pl,nl=1):
  if s.st or(pl and(s.hm>99 or s.hh.get(s.h,0)>1)):return 0
  if d<1:return s.qs(a,b,pl)
  s.nd+=1
  if s.nd>=NN:s.st=1;return 0
  sd=s.s;ic=s.att(s.ks[sd],-sd)
  if ic and pl<16:d+=1
  oa=a;ent=s.tt.get(s.h);tm=None
  if ent:
   ed,ef,ev,tm=ent
   if ed>=d and pl and(ef==0 or(ef==1 and ev>=b)or(ef==2 and ev<=a)):return ev
  if nl and not ic and d>2 and pl and s.ph>3:
   oe=s.ep
   if oe>=0:s.h^=Z[1680+oe]
   s.ep=-1;s.s=-sd;s.h^=Z[1807];sc=-s.ab(d-3,-b,-b+1,pl+1,0);s.s=sd;s.ep=oe;s.h^=Z[1807]
   if oe>=0:s.h^=Z[1680+oe]
   if s.st:return 0
   if sc>=b:return b
  mvs=s.gen(0);mvs.sort(key=lambda m:s.sm(m,tm,pl),reverse=1);bs=-999999;bm=None;lg=0
  for m in mvs:
   icp=s.b[m[1]]or(abs(s.b[m[0]])==1 and m[1]==s.ep)
   u=s.mk(m)
   if s.att(s.ks[sd],-sd):s.umk(m,u);continue
   lg+=1;s.hh[s.h]=s.hh.get(s.h,0)+1
   if lg==1:sc=-s.ab(d-1,-b,-a,pl+1,1)
   else:
    rd=1+(lg>6)+(lg>14)if d>2 and lg>3 and not ic and not icp and not m[2]else 0
    sc=-s.ab(d-1-rd,-a-1,-a,pl+1,1)
    if not s.st and rd and sc>a:sc=-s.ab(d-1,-a-1,-a,pl+1,1)
    if not s.st and a<sc<b:sc=-s.ab(d-1,-b,-a,pl+1,1)
   s.hh[s.h]-=1;s.umk(m,u)
   if s.st:return 0
   if sc>bs:bs=sc;bm=m
   if sc>a:
    a=sc
    if a>=b:
     if not icp and not m[2]:
      k=s.kl[pl]
      if k[0]!=m:k[1]=k[0];k[0]=m
      s.hs[(m[0],m[1])]=s.hs.get((m[0],m[1]),0)+d*d
     break
  if not lg:return-30000+pl if ic else 0
  if len(s.tt)>250000:s.tt.clear()
  s.tt[s.h]=(d,0 if oa<bs<b else(1 if bs>=b else 2),bs,bm);return bs
 def best(s):
  s.nd=0;s.st=0;bm=None
  for m in s.gen(0):
   u=s.mk(m);ok=not s.att(s.ks[-s.s],s.s);s.umk(m,u)
   if ok:bm=m;break
  if not bm:return None
  val=0
  for d in range(1,32):
   a,b=(-999999,999999)if d<4 else(val-45,val+45);sc=s.ab(d,a,b,0,1)
   if not s.st and(sc<=a or sc>=b):sc=s.ab(d,-999999,999999,0,1)
   if s.st:break
   val=sc;ent=s.tt.get(s.h)
   if ent and ent[3]:bm=ent[3]
   if abs(val)>25000:break
  fr,to,pr=bm;return chr((fr&7)+97)+str(8-(fr>>4))+chr((to&7)+97)+str(8-(to>>4))+({5:"q",4:"r",3:"b",2:"n"}.get(pr,""))
def post(u,p,b):
 with U.urlopen(U.Request(u+p,json.dumps(b).encode(),{"Content-Type":"application/json"}),timeout=30)as f:return json.loads(f.read())
u=os.environ["MAKEFUN_ENV_URL"].rstrip("/")
while 1:
 g=post(u,"/game",{})
 if g.get("status")=="done":break
 gid=g["game"];e=E()
 def ap(m):e.mk((((8-int(m[1]))<<4)|(ord(m[0])-97),((8-int(m[3]))<<4)|(ord(m[2])-97),{"q":5,"r":4,"b":3,"n":2}[m[4]]if len(m)==5 else 0));e.hh[e.h]=e.hh.get(e.h,0)+1
 ms=tuple(g.get("moves",[]))
 for m in ms:ap(m)
 while 1:
  m=BK.get(ms)if len(ms)<4 and ms in BK else e.best();ms=(0,)*9
  if not m:post(u,"/resign",{"game":gid});break
  ap(m);r=post(u,"/move",{"game":gid,"move":m})
  if r.get("status")!="your_move":break
  m=r.get("last_move")
  if m:ap(m)
