import time
from time import sleep
import sys
a = ('100')
b = ('101')
c = ('102')
d = ('103')
e = ('104')
f = ('105')
g = ('106')
h = ('107')
i = ('108')
j = ('109')
k = ('110')
l = ('111')
m = ('112')
n = ('113')
o = ('114') 
p = ('115')
q = ('116')
r = ('117')
s = ('118')
t = ('119')
u = ('120')
v = ('121')
w = ('122')
x = ('123')
y = ('124')
z = ('125')
if sys.version_info[0] !=3: 
	print('''
    ========================
    Harus Menggunakan Python3
    example:
            python3/python worldlist.py
    ================================''')
	sys.exit()
biru = "\033[96;1m" 
hijau = "\033[32;1m" 
putih = "\033[0;1m"  
merah = "\033[31;1m"
netral = "\033[0m"
print(biru+'''
            -----------------------------------------------
            |                                             |
            |           # Worldlist Engine #              |
            |           #Making By:Mr.Teuku #             |
            |     #Contact Me:azhargntl1@gmail.com#       |
            |           # CopyRight (2019) #              |
            |             # Since: (2018) #               |
            |                                             |
            |                                             |
            |                                             |
            |Note:For Exit_K_                             |
            |_____________________________________________|''')
nama = input(biru+'Siapa nama lengkap Target>')
if nama == "K" or nama == "k":
    exit()
nad = input('Nama Depan>')
if nad == 'K' or nad == 'k':
    exit()
nab = input('Nama Belakang>')
if nab == 'K' or nab == 'k':
    exit()
tgl = input('Tanggal Lahir>')
while len(tgl) != 0 and len(tgl) != 8:
    print('\r\n[#]Harus Lebih Dari 0 Dan Kurang Dari 8 Angka!!')
    tgl = input('Tanggal Lahir>')
    if tgl == "K" or tgl == "k":
	exit()
if tgl == 'K' or tgl == 'k':
    exit()
np = input(netral+hijau+'Nama pet>')
if np == 'K' or np == 'k':
    exit()
npt = input('tanggal pet>')
while len(npt) != 0 and len(npt) != 8:
    print('\r\n[#]Harus Lebih Dari 0 Dan Kurang Dari 8 Angka!!')
    npt = input('Tanggal Lahir>')
    if npt == "K" or npt == 'k':
        exit()
if npt == 'K' or npt == 'k':
    exit()
pc = input(netral+merah+'Nama Pacar>')
if pc == 'K' or pc == 'k':
    exit()
dk = input('Nama Adik>')
if dk == 'K' or dk == 'k':
    exit()
sh = input('Nama Sahabat>')
if sh == 'K' or sh == 'k':
    exit()
pg = input('Nama Panggilan>')
if pg == 'K' or pg == 'k':
    exit()
(netral)
azhar1 = True
while azhar1:
    azhar = input(merah+'Continue For Packing[y/t]')
    if azhar == "y" or azhar == "Y":
        azhar1 = False
    else:
        azhar1 = True       
print(biru+'############################')
txt = ('.txt')
w_w = open(nama+txt, 'w')
print('Writing Loading')
sleep(2)
w_w.write(nama)
w_w.write('\n')
w_w.write(nad)
w_w.write('\n')
w_w.write(nab)
w_w.write('\n')
w_w.write(tgl)
w_w.write('\n')
w_w.write(np)
print("Loading 25%")
sleep(3)
w_w.write('\n')
w_w.write(npt)
w_w.write('\n')
w_w.write(pc)
w_w.write('\n')
print('Loading 50%')
sleep(3)
w_w.write(dk)
w_w.write('\n')
w_w.write(sh)
w_w.write('\n')
w_w.write(pg)
w_w.write('\n')
print('Loaing 70%')
sleep(3)
w_w.write(nad+nab)
w_w.write('\n')
sleep(4)
w_w.write(nad+tgl)
w_w.write('\n')
w_w.write(np+npt)
w_w.write('\n')
w_w.write(nab+a)
w_w.write('\n')
w_w.write(nab+b)
w_w.write('\n')
w_w.write(nab+c)
w_w.write('\n')
w_w.write(nab+d)
w_w.write('\n')
w_w.write(nab+e)
w_w.write('\n')
w_w.write(nab+f)
w_w.write('\n')
w_w.write(nab+g)
w_w.write('\n')
w_w.write(nab+h)
w_w.write('\n')
w_w.write(nab+i)
w_w.write('\n')
w_w.write(nab+j)
w_w.write('\n')
w_w.write(nab+k)
w_w.write('\n')
w_w.write(nab+l)
w_w.write('\n')
w_w.write(nab+m)
w_w.write('\n')
w_w.write(nab+n)
w_w.write('\n')
w_w.write(nab+o)
w_w.write('\n')
w_w.write(nab+p)
w_w.write('\n')
w_w.write(nab+q)
w_w.write('\n')
w_w.write(nab+r)
w_w.write('\n')
w_w.write(nab+s)
w_w.write('\n')
w_w.write(nab+t)
w_w.write('\n')
w_w.write(nab+u)
w_w.write('\n')
w_w.write(nab+v)
w_w.write('\n')
w_w.write(nab+w)
w_w.write('\n')
w_w.write(nab+x)
w_w.write('\n')
w_w.write(nab+y)
w_w.write('\n')
w_w.write(nab+z)
w_w.write('\n')
w_w.write(nad+a)
w_w.write('\n')
w_w.write(nad+b)
w_w.write('\n')
w_w.write(nad+c)
w_w.write('\n')
w_w.write(nad+d)
w_w.write('\n')
w_w.write(nad+e)
w_w.write('\n')
w_w.write(nad+f)
w_w.write('\n')
w_w.write(nad+g)
w_w.write('\n')
w_w.write(nad+h)
w_w.write('\n')
w_w.write(nad+i)
w_w.write('\n')
w_w.write(nad+j)
w_w.write('\n')
w_w.write(nad+k)
w_w.write('\n')
w_w.write(nad+l)
w_w.write('\n')
w_w.write(nad+m)
w_w.write('\n')
w_w.write(nad+n)
w_w.write('\n')
w_w.write(nad+o)
w_w.write('\n')
w_w.write(nad+p)
w_w.write('\n')
w_w.write(nad+q)
w_w.write('\n')
w_w.write(nad+r)
w_w.write('\n')
w_w.write(nad+s)
w_w.write('\n')
w_w.write(nad+t)
w_w.write('\n')
w_w.write(nad+u)
w_w.write('\n')
w_w.write(nad+v)
w_w.write('\n')
w_w.write(nad+w)
w_w.write('\n')
w_w.write(nad+x)
w_w.write('\n')
w_w.write(nad+z)
w_w.write('\n')
w_w.write(pg+pc)
w_w.write('\n')
w_w.write(pg+dk)
w_w.write('\n')
w_w.write(pg+sh)
w_w.write('\n')
w_w.write(nama+tgl)
w_w.write('\n')
w_w.write(nad+pc)
print('Loading 100%')
sleep(2)
w_w.write('\n')
w_w.close()
print('</>File Ada di</>'+nama+txt)
