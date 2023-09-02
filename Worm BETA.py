import os
import msvcrt
import numpy as np
import time as ti
import random as rd
import sys
os.system("")


# ████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
# ███████████████████████████████████████████████████████████████████████████      worm_co_dien     █████████████████████████████████████████████████████████████████████████████
# ████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████

def worm_co_dien():
    global ran
    global moi
    global kinh_thuoc_map
    global scorein
    global timeplayin
    global run0
    key=''
    kinh_thuoc_map=list_size_map[size_map]
    ma_tran_mac_dinh = np.zeros((kinh_thuoc_map,kinh_thuoc_map))
    ma_tran_mac_dinh = np.pad(ma_tran_mac_dinh, ((1, 1), (1, 1)), mode='constant', constant_values=1)
    ma_tran=ma_tran_mac_dinh.copy()
    t=t1=score=timeplay=0
    ran=[[kinh_thuoc_map//2,kinh_thuoc_map//2],[kinh_thuoc_map//2,kinh_thuoc_map//2+1]]
    moi=[]
    time_start1=ti.time()
    for i in range(list_luong_moi[luong_moi]):
        moi.append(rd_moi())
    time_start=ti.time() 
    t=0
    so_tuong=np.count_nonzero(ma_tran_mac_dinh==1)
    while True:
        if msvcrt.kbhit():
            key = str(msvcrt.getch())[2:-1]
            if key==r'\x1b':
                za=tam_dung()
                if za==1:
                    run0=6
                    return
                elif za==2:
                    run0=2
                    return
            elif key not in nut:
                key=''
        if t >= 1/(list_toc_do[toc_do]+6):
            loi=False
            time_start=ti.time()   
            if key!='':
                if key==nut[0] and [ran[0][0]-1,ran[0][1]] != ran[1]:
                    ran.insert(0,[ran[0][0]-1,ran[0][1]])  
                elif  key==nut[1] and [ran[0][0],ran[0][1]+1] != ran[1]:
                    ran.insert(0,[ran[0][0],ran[0][1]+1])
                elif key==nut[2] and [ran[0][0]+1,ran[0][1]] != ran[1]:
                    ran.insert(0,[ran[0][0]+1,ran[0][1]])             
                elif key==nut[3] and [ran[0][0],ran[0][1]-1] != ran[1]:
                    ran.insert(0,[ran[0][0],ran[0][1]-1])
                else:
                    loi=True
            else:
                loi=True
            if loi:
                apl=[ran[0][0]-ran[1][0],ran[0][1]-ran[1][1]]
                if apl[0]>0 :
                    ran.insert(0,[ran[0][0]+1,ran[0][1]])
                elif apl[0]<0 :
                    ran.insert(0,[ran[0][0]-1,ran[0][1]])
                elif apl[1]>0 :
                    ran.insert(0,[ran[0][0],ran[0][1]+1])
                elif apl[1]<0 :
                    ran.insert(0,[ran[0][0],ran[0][1]-1])     
            for i in moi:
                ma_tran[i[0]+1,i[1]+1]=2
            for i in range(1,len(ran)):
                ma_tran[ran[i][0]+1,ran[i][1]+1]=4   
            ma_tran[ran[0][0]+1,ran[0][1]+1]=3
            
            
            if ran[0] in moi:
                moi.remove(ran[0])
                if np.count_nonzero(ma_tran==0)!=0:
                    moi.append(rd_moi())
                score+=1
            else:
                ran.pop(-1)
        for i in moi:
            ma_tran[i[0]+1,i[1]+1]=2
        for i in range(1,len(ran)):
            ma_tran[ran[i][0]+1,ran[i][1]+1]=4   
        ma_tran[ran[0][0]+1,ran[0][1]+1]=3
        quy_doi_co_dien=['  ','\033[0;32m'+'[]'+'\u001b[0m','\033[0;31m'+'▒▒'+'\u001b[0m','\033[0;35m'+'██'+'\u001b[0m','\033[0;36m'+'▓▓'+'\u001b[0m']
        ky_tu='║ '     
        for i in ma_tran:
            for i1 in i:
                ky_tu+=quy_doi_co_dien[int(i1)]
            ky_tu+=' ║\n║ '
        ky_tu=ky_tu.rstrip('║ ')
        scorein=doi_mau_text('do',((str(score)).rjust(3,'0')),tuoi=True)
        timeplay+=t1
        time_start1=ti.time()
        timeplayin=doi_mau_text('xanh',((str(round(timeplay)//60)).rjust(2,'0')+':'+(str(round(timeplay)-60*(round(timeplay)//60))).rjust(2,'0')),tuoi=True)
        cls()
        print('┏━━━━━━━━━━━━━━━━━━━┓'.center(kinh_thuoc_map*2+8)+'\n'+('║ TIME PLAY : '+timeplayin+' ║').center(kinh_thuoc_map*2+18)+'\n'+'┗━━━━━━━━━━━━━━━━━━━┛'.center(kinh_thuoc_map*2+8))
        print('╔'+'═'*(kinh_thuoc_map*2+6)+'╗')
        print(ky_tu,end='')
        print('╚'+'═'*(kinh_thuoc_map*2+6)+'╝')
        print('┏━━━━━━━━━━━━━┓'.center(kinh_thuoc_map*2+4)+'\n'+('║ SCORE : '+scorein+' ║').center(kinh_thuoc_map*2+13)+'\n'+'┗━━━━━━━━━━━━━┛'.center(kinh_thuoc_map*2+4))
        if ran.count(ran[0])>=2 or np.count_nonzero(ma_tran==1)!=so_tuong:
            run0=19
            return
        elif np.count_nonzero(ma_tran==0)==0 and np.count_nonzero(ma_tran==2)==0:
            run0=18
            return
        ma_tran=ma_tran_mac_dinh.copy()
        time_end=ti.time()
        t=time_end-time_start
        t1=time_end-time_start1
  
# ████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
# ███████████████████████████████████████████████████████████████████████████      worm_hai_dau     █████████████████████████████████████████████████████████████████████████████
# ████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████  
  
   
def worm_hai_dau():
    global ran
    global moi
    global kinh_thuoc_map
    global scorein
    global timeplayin
    global run0
    key=''
    kinh_thuoc_map=list_size_map[size_map]
    ma_tran_mac_dinh = np.zeros((kinh_thuoc_map,kinh_thuoc_map))
    ma_tran_mac_dinh = np.pad(ma_tran_mac_dinh, ((1, 1), (1, 1)), mode='constant', constant_values=1)
    ma_tran=ma_tran_mac_dinh.copy()
    t=t1=score=timeplay=0
    ran=[[kinh_thuoc_map//2,kinh_thuoc_map//2],[kinh_thuoc_map//2,kinh_thuoc_map//2+1]]
    moi=[]
    time_start1=ti.time()
    for i in range(list_luong_moi[luong_moi]):
        moi.append(rd_moi())
    time_start=ti.time() 
    t=0
    so_tuong=np.count_nonzero(ma_tran_mac_dinh==1)
    while True:
        if msvcrt.kbhit():
            key = str(msvcrt.getch())[2:-1]
            if key==r'\x1b':
                za=tam_dung()
                if za==1:
                    run0=7
                    return
                elif za==2:
                    run0=2
                    return
            elif key not in nut:
                key=''
        if t >= 1/(list_toc_do[toc_do]+6):
            loi=False
            time_start=ti.time()   
            if key!='':
                if key==nut[0] and [ran[0][0]-1,ran[0][1]] != ran[1]:
                    ran.insert(0,[ran[0][0]-1,ran[0][1]])  
                elif  key==nut[1] and [ran[0][0],ran[0][1]+1] != ran[1]:
                    ran.insert(0,[ran[0][0],ran[0][1]+1])
                elif key==nut[2] and [ran[0][0]+1,ran[0][1]] != ran[1]:
                    ran.insert(0,[ran[0][0]+1,ran[0][1]])             
                elif key==nut[3] and [ran[0][0],ran[0][1]-1] != ran[1]:
                    ran.insert(0,[ran[0][0],ran[0][1]-1])
                else:
                    loi=True
            else:
                loi=True
            if loi:
                apl=[ran[0][0]-ran[1][0],ran[0][1]-ran[1][1]]
                if apl[0]>0 :
                    ran.insert(0,[ran[0][0]+1,ran[0][1]])
                elif apl[0]<0 :
                    ran.insert(0,[ran[0][0]-1,ran[0][1]])
                elif apl[1]>0 :
                    ran.insert(0,[ran[0][0],ran[0][1]+1])
                elif apl[1]<0 :
                    ran.insert(0,[ran[0][0],ran[0][1]-1])     
            for i in moi:
                ma_tran[i[0]+1,i[1]+1]=2
            for i in range(1,len(ran)):
                ma_tran[ran[i][0]+1,ran[i][1]+1]=4   
            ma_tran[ran[0][0]+1,ran[0][1]+1]=3
            
            
            if ran[0] in moi:
                moi.remove(ran[0])
                if np.count_nonzero(ma_tran==0)!=0:
                    moi.append(rd_moi())
                score+=1
                ran=ran[::-1]
                key=''
            else:
                ran.pop(-1)
        for i in moi:
            ma_tran[i[0]+1,i[1]+1]=2
        for i in range(1,len(ran)):
            ma_tran[ran[i][0]+1,ran[i][1]+1]=4   
        ma_tran[ran[0][0]+1,ran[0][1]+1]=3
        quy_doi_co_dien=['  ','\033[0;32m'+'[]'+'\u001b[0m','\033[0;31m'+'O '+'\u001b[0m','\033[0;35m'+'██'+'\u001b[0m','\033[0;36m'+'▓▓'+'\u001b[0m']
        ky_tu='║ '     
        for i in ma_tran:
            for i1 in i:
                ky_tu+=quy_doi_co_dien[int(i1)]
            ky_tu+=' ║\n║ '
        ky_tu=ky_tu.rstrip('║ ')
        scorein=doi_mau_text('luc',((str(score)).rjust(3,'0')),tuoi=True)
        timeplay+=t1
        time_start1=ti.time()
        timeplayin=doi_mau_text('xanh',((str(round(timeplay)//60)).rjust(2,'0')+':'+(str(round(timeplay)-60*(round(timeplay)//60))).rjust(2,'0')),tuoi=True)
        cls()
        print('┏━━━━━━━━━━━━━━━━━━━┓'.center(kinh_thuoc_map*2+8)+'\n'+('║ TIME PLAY : '+timeplayin+' ║').center(kinh_thuoc_map*2+18)+'\n'+'┗━━━━━━━━━━━━━━━━━━━┛'.center(kinh_thuoc_map*2+8))
        print('╔'+'═'*(kinh_thuoc_map*2+6)+'╗')
        print(ky_tu,end='')
        print('╚'+'═'*(kinh_thuoc_map*2+6)+'╝')
        print('┏━━━━━━━━━━━━━┓'.center(kinh_thuoc_map*2+4)+'\n'+('║ SCORE : '+scorein+' ║').center(kinh_thuoc_map*2+13)+'\n'+'┗━━━━━━━━━━━━━┛'.center(kinh_thuoc_map*2+4))
        if ran.count(ran[0])>=2 or np.count_nonzero(ma_tran==1)!=so_tuong:
            run0=19
            return
        elif np.count_nonzero(ma_tran==0)==0 and np.count_nonzero(ma_tran==2)==0:
            run0=18
            return
        ma_tran=ma_tran_mac_dinh.copy()
        time_end=ti.time()
        t=time_end-time_start
        t1=time_end-time_start1
   
# ████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
# ███████████████████████████████████████████████████████████████████████████      worm_song_the     █████████████████████████████████████████████████████████████████████████████
# ████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████  


def worm_song_the():
    global ran
    global moi
    global kinh_thuoc_map
    global scorein
    global timeplayin
    global run0
    key=''
    kinh_thuoc_map=list_size_map[size_map]
    ma_tran_mac_dinh = np.zeros((kinh_thuoc_map,kinh_thuoc_map))
    ma_tran_mac_dinh = np.pad(ma_tran_mac_dinh, ((1, 1), (1, 1)), mode='constant', constant_values=1)
    ma_tran=ma_tran_mac_dinh.copy()
    t=t1=score=timeplay=0
    ran1=[[kinh_thuoc_map//2-1,kinh_thuoc_map-kinh_thuoc_map//3-1],[kinh_thuoc_map//2-1,kinh_thuoc_map-kinh_thuoc_map//3]]
    ran2=[[kinh_thuoc_map//2,kinh_thuoc_map//3],[kinh_thuoc_map//2,kinh_thuoc_map//3-1]]
    ran=ran1+ran2
    moi=[]
    time_start1=ti.time()
    for i in range(list_luong_moi[luong_moi]):
        moi.append(rd_moi())
    time_start=ti.time() 
    t=0
    so_tuong=np.count_nonzero(ma_tran_mac_dinh==1)
    while True:
        if msvcrt.kbhit():
            key = str(msvcrt.getch())[2:-1]
            if key==r'\x1b':
                za=tam_dung()
                if za==1:
                    run0=8
                    return
                elif za==2:
                    run0=2
                    return
            elif key not in nut:
                key=''
        if t >= 1/(list_toc_do[toc_do]+6):
            loi=False
            time_start=ti.time()   
            if key!='':
                if key==nut[0] and [ran1[0][0]-1,ran1[0][1]] != ran1[1]:
                    ran1.insert(0,[ran1[0][0]-1,ran1[0][1]])  
                    ran2.insert(0,[ran2[0][0]+1,ran2[0][1]])  
                elif  key==nut[1] and [ran1[0][0],ran1[0][1]+1] != ran1[1]:
                    ran1.insert(0,[ran1[0][0],ran1[0][1]+1])
                    ran2.insert(0,[ran2[0][0],ran2[0][1]-1])
                elif key==nut[2] and [ran1[0][0]+1,ran1[0][1]] != ran1[1]:
                    ran1.insert(0,[ran1[0][0]+1,ran1[0][1]])  
                    ran2.insert(0,[ran2[0][0]-1,ran2[0][1]])            
                elif key==nut[3] and [ran1[0][0],ran1[0][1]-1] != ran1[1]:
                    ran1.insert(0,[ran1[0][0],ran1[0][1]-1])
                    ran2.insert(0,[ran2[0][0],ran2[0][1]+1])
                else:
                    loi=True
            else:
                loi=True
            if loi:
                apl=[ran1[0][0]-ran1[1][0],ran1[0][1]-ran1[1][1]]
                if apl[0]>0 :
                    ran1.insert(0,[ran1[0][0]+1,ran1[0][1]])
                    ran2.insert(0,[ran2[0][0]-1,ran2[0][1]])
                elif apl[0]<0 :
                    ran1.insert(0,[ran1[0][0]-1,ran1[0][1]])
                    ran2.insert(0,[ran2[0][0]+1,ran2[0][1]])
                elif apl[1]>0 :
                    ran1.insert(0,[ran1[0][0],ran1[0][1]+1])
                    ran2.insert(0,[ran2[0][0],ran2[0][1]-1])
                elif apl[1]<0 :
                    ran1.insert(0,[ran1[0][0],ran1[0][1]-1])   
                    ran2.insert(0,[ran2[0][0],ran2[0][1]+1])     
            ran=ran1+ran2
            for i in moi:
                ma_tran[i[0]+1,i[1]+1]=2
            for i in range(1,len(ran1)):
                ma_tran[ran1[i][0]+1,ran1[i][1]+1]=4  
            for i in range(1,len(ran2)):
                ma_tran[ran2[i][0]+1,ran2[i][1]+1]=6  
            ma_tran[ran1[0][0]+1,ran1[0][1]+1]=3
            ma_tran[ran2[0][0]+1,ran2[0][1]+1]=5
            
            if ran1[0] in moi:
                moi.remove(ran1[0])
                if np.count_nonzero(ma_tran==0)!=0:
                    moi.append(rd_moi())
                score+=1
            elif ran2[0] in moi:
                moi.remove(ran2[0])
                if np.count_nonzero(ma_tran==0)!=0:
                    moi.append(rd_moi())
                score+=1
            else:
                ran1.pop(-1)
                ran2.pop(-1)
        for i in moi:
            ma_tran[i[0]+1,i[1]+1]=2
        for i in range(1,len(ran1)):
            ma_tran[ran1[i][0]+1,ran1[i][1]+1]=4  
        for i in range(1,len(ran2)):
            ma_tran[ran2[i][0]+1,ran2[i][1]+1]=6  
        ma_tran[ran1[0][0]+1,ran1[0][1]+1]=3
        ma_tran[ran2[0][0]+1,ran2[0][1]+1]=5
        quy_doi_co_dien=['  ','\033[0;32m'+'[]'+'\u001b[0m','\033[0;31m'+'O '+'\u001b[0m','\033[0;35m'+'██'+'\u001b[0m','\033[0;36m'+'▓▓'+'\u001b[0m','\033[0;32m'+'██'+'\u001b[0m','\033[0;33m'+'▓▓'+'\u001b[0m']
        ky_tu='║ '     
        for i in ma_tran:
            for i1 in i:
                ky_tu+=quy_doi_co_dien[int(i1)]
            ky_tu+=' ║\n║ '
        ky_tu=ky_tu.rstrip('║ ')
        scorein=doi_mau_text('luc',((str(score)).rjust(3,'0')),tuoi=True)
        timeplay+=t1
        time_start1=ti.time()
        timeplayin=doi_mau_text('xanh',((str(round(timeplay)//60)).rjust(2,'0')+':'+(str(round(timeplay)-60*(round(timeplay)//60))).rjust(2,'0')),tuoi=True)
        cls()
        print('┏━━━━━━━━━━━━━━━━━━━┓'.center(kinh_thuoc_map*2+8)+'\n'+('║ TIME PLAY : '+timeplayin+' ║').center(kinh_thuoc_map*2+18)+'\n'+'┗━━━━━━━━━━━━━━━━━━━┛'.center(kinh_thuoc_map*2+8))
        print('╔'+'═'*(kinh_thuoc_map*2+6)+'╗')
        print(ky_tu,end='')
        print('╚'+'═'*(kinh_thuoc_map*2+6)+'╝')
        print('┏━━━━━━━━━━━━━┓'.center(kinh_thuoc_map*2+4)+'\n'+('║ SCORE : '+scorein+' ║').center(kinh_thuoc_map*2+13)+'\n'+'┗━━━━━━━━━━━━━┛'.center(kinh_thuoc_map*2+4))
        if ran1.count(ran1[0])>=2 or np.count_nonzero(ma_tran==1)!=so_tuong or ran2.count(ran2[0])>=2 or ran2.count(ran1[0])!=0 or ran1.count(ran2[0])!=0:
            run0=19
            return
        elif np.count_nonzero(ma_tran==0)==0 and np.count_nonzero(ma_tran==2)==0:
            run0=18
            return
        ma_tran=ma_tran_mac_dinh.copy()
        time_end=ti.time()
        t=time_end-time_start
        t1=time_end-time_start1

# ████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
# ████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
# ████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████

def tam_dung():
    list_dong=[' ╔══════════════════╗ ', #0
          ' ║                  ║ ', #1
          ' ╚══════════════════╝ ', #2
          ' ║     Tiếp Tục     ║ ', #3
          ' ║     Chơi Lại     ║ ', #4
          ' ║      Thoát       ║ ', #5
          ' ║  [  '+doi_mau_text('do','Tiếp Tục')+'  ]  ║ ', #6
          ' ║  [  '+doi_mau_text('do','Chơi Lại')+'  ]  ║ ', #7
          ' ║   [  '+doi_mau_text('do','Thoát')+'  ]    ║ ',]#8
    chon=0
    vi_tri_bat_dau=[(kinh_thuoc_map//2+2),(kinh_thuoc_map-6)]
    list_in=[0,1,6,1,4,1,5,1,2 ]
    for i in range(9):
        print(f"\x1b[{vi_tri_bat_dau[0]+i};{vi_tri_bat_dau[1]}H"+list_dong[list_in[i]])
    while True:
        if msvcrt.kbhit():
            key = str(msvcrt.getch())[2:-1]
            if key==nut[0]:
                if chon==0:
                    chon=2
                else:
                    chon-=1
            elif key==nut[2]:
                if chon==2:
                    chon=0
                else:
                    chon+=1
            elif key==r'\r':
                if chon==0:
                    return 0
                elif chon==1:
                    return 1
                else:
                    return 2
            if chon==0:
                list_in[2]=6
                list_in[4]=4
                list_in[6]=5
            elif chon==1:
                list_in[2]=3
                list_in[4]=7
                list_in[6]=5
            else:
                list_in[2]=3
                list_in[4]=4
                list_in[6]=8
            for i in range(9):
                print(f"\x1b[{vi_tri_bat_dau[0]+i};{vi_tri_bat_dau[1]}H"+list_dong[list_in[i]])
                
    
       
   
   
   
def doi_mau_text(mau,text,tuoi=False):
    list_ten_mau=['den','do','luc','vang','xanh dam','tim','xanh','trang']
    list_ma_thuong=['\033[0;30m','\033[0;31m','\033[0;32m','\033[0;33m','\033[0;34m','\033[0;35m','\033[0;36m','\033[0;37m']
    list_ma_tuoi=['\033[1;30m','\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m','\033[1;37m']
    z=list_ten_mau.index(mau)
    if tuoi:
        return list_ma_tuoi[z]+text+'\u001b[0m'
    else:
        return list_ma_thuong[z]+text+'\u001b[0m'
    
def cls():
    ESC = "\x1B"
    print(f"{ESC}[999D")
    print(f"{ESC}[999A", end="")

def rd_moi():
    global moi
    while True:
        a=[rd.randint(0,kinh_thuoc_map-1),rd.randint(0,kinh_thuoc_map-1)]
        if a not in ran and a not in moi: 
            return a
   
   
        
def upload_man_hinh13():
    global man_hinh13
    man_hinh13=f'╔══════════════════════════════════════════════════════╗\n║           lên              :            {nut[0]}            ║\n╟──────────────────────────────────────────────────────╢\n║           phải             :            {nut[1]}            ║\n╟──────────────────────────────────────────────────────╢\n║           xuống            :            {nut[2]}            ║\n╟──────────────────────────────────────────────────────╢\n║           trái             :            {nut[3]}            ║\n╟──────────────────────────────────────────────────────╢\n║        về Mặc Định                    Thoát          ║\n╚══════════════════════════════════════════════════════╝'

def upload_man_hinh12():
    global man_hinh12
    man_hinh12=f'╔══════════════════════════════════════════════════════╗\n║                                                      ║\n║                    {list_hien_thi[0]}                  ║\n║                                                      ║\n║                    {list_hien_thi[1]}                  ║\n║                                                      ║\n║                    {list_hien_thi[2]}                  ║\n║                                                      ║\n║                    {list_hien_thi[3]}                  ║\n║                                                      ║\n║                    {list_hien_thi[4]}                  ║\n║                                                      ║\n║                    {list_hien_thi[5]}                  ║\n║                                  nhấn -'+doi_mau_text('do','esc')+'- để thoát ║\n╚══════════════════════════════════════════════════════╝'
    man_hinh12=man_hinh12[0:(57*(2+chon*2)+15)]+f'[   {list_hien_thi[chon]}       ]'+man_hinh12[(57*(2+chon*2)+43):]
    if x==0:
        man_hinh12=man_hinh12[:(57*13+27)]+'˅'+man_hinh12[(57*13+28):]
    elif x==len(list_game)-6:
        man_hinh12=man_hinh12[:(57+27)]+'˄'+man_hinh12[(57+28):]
    else:
        man_hinh12=man_hinh12[:(57*13+27)]+'˅'+man_hinh12[(57*13+28):]
        man_hinh12=man_hinh12[:(57+27)]+'˄'+man_hinh12[(57+28):]
    return man_hinh12
def upload_man_hinh25():
    global man_hinh25
    man_hinh25=f'╔══════════════════════════════════════════════════════╗\n║                 ~ {list_game[game_dc_chon].center(16)} ~                 ║\n║                                                      ║\n║     Tốc độ                :             {list_toc_do[toc_do]}            ║\n║                                                      ║\n║     Số lượng mồi          :             {list_luong_moi[luong_moi]}            ║\n║                                                      ║\n║     Độ lớn map            :           '+f'{list_size_map[size_map]}x{list_size_map[size_map]}'.center(5)+'          ║\n║                                                      ║\n║                  Điểm Cao Trước Đó                   ║\n║                                                      ║\n║       Chơi                            Quay Lại       ║\n╚══════════════════════════════════════════════════════╝'
    cls()
    asok=[doi_mau_text('do',f'{list_toc_do[toc_do]}'),doi_mau_text('do',f'{list_luong_moi[luong_moi]}'),doi_mau_text('do',f'{list_size_map[size_map]}')]
    if chon in [0,1]:
        print(man_hinh25[:(57*(3+chon*2)+39)]+f'<< {asok[chon]} >>'.center(11)+man_hinh25[(57*(3+chon*2)+46):])
    elif chon==2:
        print(man_hinh25[:(57*(3+chon*2)+37)]+f'<< {asok[chon]}x{asok[chon]} >>'.center(13)+man_hinh25[(57*(3+chon*2)+48):])
    elif chon==3:
        print(man_hinh25[:(57*(3+chon*2)+17)]+'[ '+doi_mau_text('do','Điểm Cao Trước Đó')+' ]'+man_hinh25[(57*(3+chon*2)+38):])
    elif chon==4:
        print(man_hinh25[:(57*(3+chon*2)+38)]+'[ '+doi_mau_text('do','Quay Lại')+' ]'+man_hinh25[(57*(3+chon*2)+50):])
    elif chon==5:
        print(man_hinh25[:(57*(3+4*2)+6)]+'[ '+doi_mau_text('do','Chơi')+' ]'+man_hinh25[(57*(3+4*2)+14):])

run0=0 
run=True
nut=['w','d','s','a']
while run:

    match run0:
        case 0:
            os.system('cls')
            print('╔══════════════════════════════════════════════════════╗\n║                                                      ║\n║        ██╗    ██╗ ██████╗ ██████╗ ███╗   ███╗        ║\n║        ██║    ██║██╔═══██╗██╔══██╗████╗ ████║        ║\n║        ██║ █╗ ██║██║   ██║██████╔╝██╔████╔██║        ║\n║        ██║███╗██║██║   ██║██╔══██╗██║╚██╔╝██║        ║\n║        ╚███╔███╔╝╚██████╔╝██║  ██║██║ ╚═╝ ██║        ║\n║         ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝'+doi_mau_text('luc','BETA')+'    ║\n║                                                      ║\n║                                                      ║\n║                                                      ║\n║                                                      ║\n║              nhấn -'+doi_mau_text('do','space')+'- để tiếp tục                ║\n║                                                      ║\n║ '+doi_mau_text('tim','Worm')+' '+doi_mau_text('luc','BETA')+'                                   © '+doi_mau_text('xanh','AURORA')+' ║\n╚══════════════════════════════════════════════════════╝')
            # làm nhấp nháy chứ space (vi_tri_bat_dau (11,14),24 ký tự )
            while True:
                
                if msvcrt.kbhit():
                    key = str(msvcrt.getch())[2:-1]
                    if key==' ':
                        run0=1
                        break
        case 1:
            quy_doi0={0:'[ '+doi_mau_text('do','Chơi')+'     ]',1:'[ '+doi_mau_text('do','Cài Đặt')+'  ]',2:'[ '+doi_mau_text('do','Phản Hồi')+' ]',3:'[ '+doi_mau_text('do','Thoát')+'    ]'}
            opt=0
            man_hinh1='╔══════════════════════════════════════════════════════╗\n║                                                      ║\n║        ██╗    ██╗ ██████╗ ██████╗ ███╗   ███╗        ║\n║        ██║    ██║██╔═══██╗██╔══██╗████╗ ████║        ║\n║        ██║ █╗ ██║██║   ██║██████╔╝██╔████╔██║        ║\n║        ██║███╗██║██║   ██║██╔══██╗██║╚██╔╝██║        ║\n║        ╚███╔███╔╝╚██████╔╝██║  ██║██║ ╚═╝ ██║        ║\n║         ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝'+doi_mau_text('luc','BETA')+'    ║\n║                                                      ║\n║         Chơi                                         ║\n║         Cài Đặt                                      ║\n║         Phản Hồi                                     ║\n║         Thoát                                        ║\n║                                                      ║\n║ '+doi_mau_text('tim','Worm')+' '+doi_mau_text('luc','BETA')+'                                   © '+doi_mau_text('xanh','AURORA')+' ║\n╚══════════════════════════════════════════════════════╝'
            os.system('cls')
            print(man_hinh1[0:(57*(9+opt)+19)]+quy_doi0[opt]+man_hinh1[(57*(9+opt)+31):])
            while True:
                if msvcrt.kbhit():
                    key = str(msvcrt.getch())[2:-1]
                    if key==nut[0]:
                        opt-=1
                        if opt==-1:
                            opt=3
                    elif key==nut[2]:
                        opt+=1
                        if opt==4:
                            opt=0
                    elif key==r'\r':
                        run0=2+opt
                        if run0==5:
                            os.system('cls')
                            sys.exit()
                        break
                    cls()
                    print(man_hinh1[0:(57*(9+opt)+19)]+quy_doi0[opt]+man_hinh1[(57*(9+opt)+31):])
        case 2:# 1:choi
            os.system('cls')
            list_game=['Worm-Cổ Điển',
                       'Worm-Hai Đầu',
                       'Worm-Song Thể',
                       'khóa',                 # 'Worm-Tường'
                       'khóa',                 # 'Worm-Dịch Chuyển',
                       'khóa',                 # 'Worm-Đứng Lại!! ',
                       'khóa',                 # 'Worm-Mở Hòm',
                       'khóa',                 # 'Worm-Đẩy Thùng',
                       'khóa',                 # 'Worm-Chơi Đồ',
                       'khóa',                 # 'Worm-Tàng Hình',
                       'khóa',                 # 'Worm-Hóa Đá',
                       'khóa'                # 'Worm-Tầm Nhìn',
                       ]
            chon=0
            x=0
            # '+doi_mau_text('do',f'')+'
            list_hien_thi=[z.ljust(16) for z in list_game[x:x+6]]     
            man_hinh12=f'╔══════════════════════════════════════════════════════╗\n║                                                      ║\n║                    {list_hien_thi[0]}                  ║\n║                                                      ║\n║                    {list_hien_thi[1]}                  ║\n║                                                      ║\n║                    {list_hien_thi[2]}                  ║\n║                                                      ║\n║                    {list_hien_thi[3]}                  ║\n║                                                      ║\n║                    {list_hien_thi[4]}                  ║\n║                                                      ║\n║                    {list_hien_thi[5]}                  ║\n║                                  nhấn -'+doi_mau_text('do','esc')+'- để thoát ║\n╚══════════════════════════════════════════════════════╝'
            print(man_hinh12[0:(57*(2+chon*2)+15)]+f'[   {list_hien_thi[chon]}       ]'+man_hinh12[(57*(2+chon*2)+43):(57*13+27)]+'˅'+man_hinh12[(57*13+28):])
            while True:
                if msvcrt.kbhit():
                    key = str(msvcrt.getch())[2:-1]
                    if key==nut[2]:
                        if chon!=5:
                            chon+=1
                        else:
                            if x!=len(list_game)-6:
                                x+=1
                                list_hien_thi=[z.ljust(16) for z in list_game[x:x+6]]  
                        cls()
                        print(upload_man_hinh12())
                    elif key==nut[0]:
                        if chon!=0:
                            chon-=1
                        else:
                            if x!=0:
                                x-=1
                                list_hien_thi=[z.ljust  (16) for z in list_game[x:x+6]]  
                        cls()
                        print(upload_man_hinh12())
                    elif key==r'\x1b':
                        run0=1
                        break
                    elif key==r'\r':
                        game_dc_chon=chon+x
                        run0=5
                        break
                        
                    
                    
                    
                    
                    
                    
            
        case 3:# 1:cai_dat
            os.system('cls')
            quy_doi1={}
            man_hinh13=f'╔══════════════════════════════════════════════════════╗\n║           lên              :            {nut[0]}            ║\n╟──────────────────────────────────────────────────────╢\n║           phải             :            {nut[1]}            ║\n╟──────────────────────────────────────────────────────╢\n║           xuống            :            {nut[2]}            ║\n╟──────────────────────────────────────────────────────╢\n║           trái             :            {nut[3]}            ║\n╟──────────────────────────────────────────────────────╢\n║        về Mặc Định                    Thoát          ║\n╚══════════════════════════════════════════════════════╝'
            aur=0
            print(man_hinh13[0:(57*(1+aur*2)+41)]+'['+doi_mau_text('do',f'{nut[aur]}')+']'+man_hinh13[(57*(1+aur*2)+44):])
            while True:
                upload_man_hinh13()
                if msvcrt.kbhit():
                    key = str(msvcrt.getch())[2:-1]
                    if key==nut[2]:#s
                        if aur in [4,5]:
                            aur=0
                        else:
                            aur+=1
                        cls()
                        if aur!=4:
                            print(man_hinh13[0:(57*(1+aur*2)+41)]+'['+doi_mau_text('do',f'{nut[aur]}')+']'+man_hinh13[(57*(1+aur*2)+44):])
                            
                    elif key==nut[0]:#w
                        if aur==0:
                            aur=4
                        elif aur==5:
                            aur=3
                        else:
                            aur-=1
                        cls()
                        if aur!=4:
                            print(man_hinh13[0:(57*(1+aur*2)+41)]+'['+doi_mau_text('do',f'{nut[aur]}')+']'+man_hinh13[(57*(1+aur*2)+44):])
                    elif key==nut[1]:
                        if aur==5:
                            aur=4
                        else:
                            aur=5
                    elif key==nut[3]:
                        if aur==5:
                            aur=4
                        else:
                            aur=5
                    elif key==r'\r':
                        if aur==4:
                            run0=1
                            break
                        elif aur==5:
                            nut=['w','d','s','a']
                            upload_man_hinh13()
                        else:
                            cls()
                            print(man_hinh13[0:(57*(1+aur*2)+32)]+'['+doi_mau_text('do','Nhập 1 Phím Bất Kỳ',tuoi=True)+']'+man_hinh13[(57*(1+aur*2)+52):])
                            while True:
                                if msvcrt.kbhit():
                                    key = str(msvcrt.getch())[2:-1]
                                    if len(key)>1:
                                        cls()
                                        print(man_hinh13[0:(57*(1+aur*2)+41)]+'['+doi_mau_text('do',f'{nut[aur]}')+']'+man_hinh13[(57*(1+aur*2)+44):])
                                        break
                                    else:
                                        if key in nut:
                                            nut[nut.index(key)]=nut[aur]
                                        nut[aur]=key
                                        upload_man_hinh13()
                                        cls()
                                        print(man_hinh13[0:(57*(1+aur*2)+41)]+'['+doi_mau_text('do',f'{nut[aur]}')+']'+man_hinh13[(57*(1+aur*2)+44):])
                                        break
                    cls()
                    if aur==4:
                        print(man_hinh13[0:(57*9+38)]+f'[ '+doi_mau_text('do','Thoát')+' ]'+man_hinh13[(57*9+47):])
                    elif aur==5:
                        print(man_hinh13[0:(57*9+7)]+f'[ '+doi_mau_text('do','Về Mặc Định')+' ]'+man_hinh13[(57*9+22):])

                    
                    
        case 4:# 1:phan_hoi
            cls()
            man_hinh=['╔══════════════════════════════════════════════════════╗\n║                                                      ║\n║                       '+doi_mau_text('xanh','Aurora')+'                         ║\n║                                                      ║\n║       '+doi_mau_text('do','Gmail')+'     :'+doi_mau_text('tim','aurora18327@gmail.com',tuoi=True)+'               ║\n║       '+doi_mau_text('do','Github')+'    :'+doi_mau_text('tim','https://github.com/animeaurora',tuoi=True)+'      ║\n║       '+doi_mau_text('do','Discord')+'   :'+doi_mau_text('tim','animeaurora                  ',tuoi=True)+'       ║\n║       '+doi_mau_text('do','Facebook')+'  :'+doi_mau_text('tim','https://tinyurl.com/Aurora-DNT',tuoi=True)+'      ║\n║                                                      ║\n║              █▀▀▀▀▀█ ▀▀▄▀▄ ▀ ▄ █▀▀▀▀▀█               ║\n║              █ ███ █  ▀██▄█▀ █ █ ███ █               ║\n║              █ ▀▀▀ █  ▄ █▄▀█ █ █ ▀▀▀ █               ║\n║              ▀▀▀▀▀▀▀ █▄▀ ▀▄▀▄█ ▀▀▀▀▀▀▀               ║\n║              ▀█ ▀█▄▀▄ ▀▄ ▀▄▄▄█ ▀▄▄▄▄▄▀               ║\n║               ▄█ ▀ ▀▀▀▀ █ ▀▄▀ ▀▄▄▀█▄▄█               ║\n║              █▀▀█▄▀▀▀ ▀█▄██▄▄█ ▀ ▄  ▄▀               ║\n║              █▀▄▀▀ ▀█▀▀█ ▄▀ ██▀ ▄▀██▀█               ║\n║              ▀ ▀▀  ▀ ▄▄█▀▀▀▄██▀▀▀█ ██                ║\n║              █▀▀▀▀▀█  █▀███ ▄█ ▀ █   ▀               ║\n║              █ ███ █ █ █▄  ▀████▀▀  █▄               ║\n║              █ ▀▀▀ █ ▄▀█▀ ▀▀▄ ▄ ▄█▀███               ║\n║              ▀▀▀▀▀▀▀ ▀ ▀ ▀   ▀ ▀  ▀  ▀               ║\n║                        '+doi_mau_text('xanh','QR:FB')+'                         ║\n║ Nhấn -'+doi_mau_text('do','esc')+'- đề thoát             Nhấn -'+doi_mau_text('do','enter')+'- để next ║\n╚══════════════════════════════════════════════════════╝',
                      '╔══════════════════════════════════════════════════════╗\n║                                                      ║\n║                  '+doi_mau_text('xanh','T.K.H')+doi_mau_text('luc',' (Support)')+'                     ║\n║                                                      ║\n║       '+doi_mau_text('do','Gmail')+'     :'+doi_mau_text('tim','tkhhung123@gmail.com',tuoi=True)+'                ║\n║       '+doi_mau_text('do','Discord')+'   :'+doi_mau_text('tim','HungKz151                    ',tuoi=True)+'       ║\n║       '+doi_mau_text('do','Facebook')+'  :'+doi_mau_text('tim','https://tinyurl.com/TKH-27',tuoi=True)+'          ║\n║       '+doi_mau_text('do','X')+'         :'+doi_mau_text('tim','https://twitter.com/HngTrnh73055681',tuoi=True)+' ║\n║                                                      ║\n║              █▀▀▀▀▀█ █▀▀█ ▄█ ▄ █▀▀▀▀▀█               ║\n║              █ ███ █  ▀ ▄▄█▄ ▀ █ ███ █               ║\n║              █ ▀▀▀ █ █▄▄▀█ █   █ ▀▀▀ █               ║\n║              ▀▀▀▀▀▀▀ █▄▀ ▀ █▄█ ▀▀▀▀▀▀▀               ║\n║              ▀▀▀ ▄█▀ ▀▀ ▀█▄▀▄▀▀██▀▄ ██               ║\n║               ▄▀▀ ▀▀▀▄▀█▄█ ▄▀██ █▀█▀ ▀               ║\n║              ▀▄▀█ █▀▄███ ▀▀▄▄█ █▄   ▄█               ║\n║              ▀▀  ▀ ▀  █▄█▄▀ █▀ ▄▄▄█▀ ▀               ║\n║              ▀▀  ▀▀▀▀▄███ █ ██▀▀▀█  ▀▄               ║\n║              █▀▀▀▀▀█ ▄▄▀█▀ █▄█ ▀ █   █               ║\n║              █ ███ █   ▀█ █ █▀█▀▀█ ▄█                ║\n║              █ ▀▀▀ █ ██▄▀▄▀▀▄█ ▄██▀ ▀▀               ║\n║              ▀▀▀▀▀▀▀ ▀▀▀ ▀ ▀ ▀ ▀  ▀  ▀               ║\n║                        '+doi_mau_text('xanh','QR:FB')+'                         ║\n║ Nhấn -'+doi_mau_text('do','esc')+'- đề thoát             Nhấn -'+doi_mau_text('do','enter')+'- để next ║\n╚══════════════════════════════════════════════════════╝',
                      '╔══════════════════════════════════════════════════════╗\n║                                                      ║\n║                  '+doi_mau_text('xanh','N.T.P')+doi_mau_text('luc',' (Support)')+'                     ║\n║                                                      ║\n║                                                      ║\n║       '+doi_mau_text('do','Discord')+'   :'+doi_mau_text('tim','https://discord.gg/vCgV72b63c',tuoi=True)+'       ║\n║       '+doi_mau_text('do','Facebook')+'  :'+doi_mau_text('tim','https://tinyurl.com/NTP-Thanks',tuoi=True)+'      ║\n║                                                      ║\n║                                                      ║\n║              █▀▀▀▀▀█ ██  ▄▄█ ▄ █▀▀▀▀▀█               ║\n║              █ ███ █  ▀ ▄▀█▄ ▀ █ ███ █               ║\n║              █ ▀▀▀ █ █▄█   █   █ ▀▀▀ █               ║\n║              ▀▀▀▀▀▀▀ █▄▀▄█ █▄█ ▀▀▀▀▀▀▀               ║\n║              █▀▀▄ ▀▀▄█▀ ▄█▄▀▄▀▀██▀▄ ██               ║\n║               █  ▄▀▀▀█▀█▀  ▄▀██ █▀█▀ ▀               ║\n║              ▀ ▀▀█▄▀▄▄▀████ ▄█ █▄   ▄█               ║\n║              ▀▀ ▀▄█▀ ▄ █▀▀  █▀ ▄▄▄█▀ ▀               ║\n║              ▀▀▀▀▀ ▀ ▄▀▄▄█▀▄██▀▀▀█  ▀▄               ║\n║              █▀▀▀▀▀█ ▄▄▀▀█▀ ▄█ ▀ █   █               ║\n║              █ ███ █  ▄█▀▄▀▄█▀█▀▀█ ▄▄                ║\n║              █ ▀▀▀ █ █▄▀▀▄▀▀▄█ ▄██▀ ▀▀               ║\n║              ▀▀▀▀▀▀▀ ▀ ▀ ▀ ▀ ▀ ▀  ▀  ▀               ║\n║                        '+doi_mau_text('xanh','QR:FB')+'                         ║\n║ Nhấn -'+doi_mau_text('do','esc')+'- đề thoát             Nhấn -'+doi_mau_text('do','enter')+'- để next ║\n╚══════════════════════════════════════════════════════╝']
            profile=0
            print(man_hinh[profile])
            while True:
                if msvcrt.kbhit():
                    key = str(msvcrt.getch())[2:-1]
                    if key==r'\x1b':
                        run0=1
                        break
                    if key==r'\r':
                        profile+=1
                        if profile==len(man_hinh):
                            profile=0
                        cls()
                        print(man_hinh[profile])
                        
        case 5:#2
            list_toc_do=[0,1,2,3,4,5,6,7,8,9]
            list_luong_moi=[1,2,3,4,5]
            list_size_map=[10,17,24]
            toc_do=1
            luong_moi=0
            size_map=2
            asok=[doi_mau_text('do',f'{list_toc_do[toc_do]}'),doi_mau_text('do',f'{list_luong_moi[luong_moi]}'),doi_mau_text('do',f'{list_size_map[size_map]}')]
            os.system('cls')
            man_hinh25=f'╔══════════════════════════════════════════════════════╗\n║                 ~ {list_game[game_dc_chon].center(16)} ~                 ║\n║                                                      ║\n║     Tốc độ                :             {list_toc_do[toc_do]}            ║\n║                                                      ║\n║     Số lượng mồi          :             {list_luong_moi[luong_moi]}            ║\n║                                                      ║\n║     Độ lớn map            :           '+f'{list_size_map[size_map]}x{list_size_map[size_map]}'.center(5)+'          ║\n║                                                      ║\n║                  Điểm Cao Trước Đó                   ║\n║                                                      ║\n║       Chơi                            Quay Lại       ║\n╚══════════════════════════════════════════════════════╝'
            chon=0
            print(man_hinh25[:(57*(3+chon*2)+39)]+f'<< {asok[chon]} >>'+man_hinh25[(57*(3+chon*2)+46):])
            while True:
                if msvcrt.kbhit():
                    key = str(msvcrt.getch())[2:-1]
                    if key==nut[2]:
                        if chon in [4,5]:
                            chon=0
                        else:
                            chon+=1
                            
                    elif key==nut[0]:
                        if chon==0:
                            chon=4
                        elif chon in [4,5]:
                            chon=3 
                        else:
                            chon-=1
                            
                    elif key==nut[1]:
                        if chon ==0:
                            toc_do+=1
                            if toc_do==len(list_toc_do):
                                toc_do=0
                        elif chon==1:
                            luong_moi+=1
                            if luong_moi==len(list_luong_moi):
                                luong_moi=0
                        elif chon==2:
                            size_map+=1
                            if size_map==len(list_size_map):
                                size_map=0
                        elif chon in [3,5]:
                            chon=4
                        elif chon==4:
                            chon=5
                    elif key==nut[3]:
                        if chon ==0:
                            toc_do-=1
                            if toc_do==-1:
                                toc_do=len(list_toc_do)-1
                        elif chon==1:
                            luong_moi-=1
                            if luong_moi==-1:
                                luong_moi=len(list_luong_moi)-1
                        elif chon==2:
                            size_map-=1
                            if size_map==-1:
                                size_map=len(list_size_map)-1
                        elif chon in [3,4]:
                            chon=5
                        elif chon==5:
                            chon=4
                    elif key==r'\r':
                        if chon==3:
                            pass
                        elif chon==4:
                            run0=2
                            break
                        elif chon==5:
                            if game_dc_chon==0:
                                run0=6
                                break
                            elif game_dc_chon==1:
                                run0=7
                                break
                            elif game_dc_chon==2:
                                run0=8
                                break
                    upload_man_hinh25()
        case 6:
            os.system('cls')
            worm_co_dien() 
        
        case 7:
            os.system('cls')    
            worm_hai_dau()
        case 8:
            os.system('cls')
            worm_song_the()
        case 18:
            os.system('cls')
            chon1=0
            man_hinh618='╔══════════════════════════════════════════════════════╗\n║                                                      ║\n║               '+doi_mau_text('do','██     ██ ██ ███    ██')+'                 ║\n║               '+doi_mau_text('do','██     ██ ██ ████   ██')+'                 ║\n║               '+doi_mau_text('do','██  █  ██ ██ ██ ██  ██')+'                 ║\n║               '+doi_mau_text('do','██ ███ ██ ██ ██  ██ ██')+'                 ║\n║               '+doi_mau_text('do',' ███ ███  ██ ██   ████')+f'                 ║\n║                                                      ║\n║                 Score     :  {scorein}                     ║\n║                 Time Play :  {timeplayin}                   ║\n║                                                      ║\n║      Chơi Lại                             Thoát      ║\n║                                                      ║\n╚══════════════════════════════════════════════════════╝'
            print(man_hinh618[:704]+'║   [  '+doi_mau_text('xanh','Chơi Lại')+'  ]                          Thoát      ║\n'+man_hinh618[761:])
            while True:
                if msvcrt.kbhit():
                    key = str(msvcrt.getch())[2:-1]
                    if key in [nut[1],nut[3]]:
                        cls()
                        if chon1==1:
                            chon1=0
                            print(man_hinh618[:704]+'║   [  '+doi_mau_text('xanh','Chơi Lại')+'  ]                          Thoát      ║\n'+man_hinh618[761:])
                        else:
                            chon1=1
                            print(man_hinh618[:704]+'║      Chơi Lại                          [  '+doi_mau_text('xanh','Thoát')+'  ]   ║\n'+man_hinh618[761:])
                    elif key=='\r':
                        if chon1==0:
                            run0=game_dc_chon+6
                            break
                        else:
                            run0=2
                            break
        case 19:
            os.system('cls')
            chon1=0
            man_hinh619='╔══════════════════════════════════════════════════════╗\n║                                                      ║\n║           '+doi_mau_text('xanh','██       ██████  ███████ ███████')+'           ║\n║           '+doi_mau_text('xanh','██      ██    ██ ██      ██     ')+'           ║\n║           '+doi_mau_text('xanh','██      ██    ██ ███████ █████  ')+'           ║\n║           '+doi_mau_text('xanh','██      ██    ██      ██ ██     ')+'           ║\n║           '+doi_mau_text('xanh','███████  ██████  ███████ ███████')+f'           ║\n║                                                      ║\n║                 Score     :  {scorein}                     ║\n║                 Time Play :  {timeplayin}                   ║\n║                                                      ║\n║      Chơi Lại                             Thoát      ║\n║                                                      ║\n╚══════════════════════════════════════════════════════╝'
            print(man_hinh619[:704]+'║   [  '+doi_mau_text('do','Chơi Lại')+'  ]                          Thoát      ║\n'+man_hinh619[761:])
            while True:
                if msvcrt.kbhit():
                    key = str(msvcrt.getch())[2:-1]
                    if key in [nut[1],nut[3]]:
                        cls()
                        if chon1==1:
                            chon1=0
                            print(man_hinh619[:704]+'║   [  '+doi_mau_text('do','Chơi Lại')+'  ]                          Thoát      ║\n'+man_hinh619[761:])
                        else:
                            chon1=1
                            print(man_hinh619[:704]+'║      Chơi Lại                          [  '+doi_mau_text('do','Thoát')+'  ]   ║\n'+man_hinh619[761:])
                    elif key==r'\r':
                        if chon1==0:
                            run0=game_dc_chon+6
                            break
                        else:
                            run0=2
                            break