import time
n_c=[3979,6592,1980,4902,6050,4980,5593,5513,8203,9053,10282,10974,12973,19045,23734,22900]#цена норникеля с 2006 по 2021
n_d=[109.49,228,112,0,210,180,196,621.53,1010.82,1297.06,674.39,670.3,1384,2280.54,1180.55,2544.39]#дивы норникеля
G_c=[287,342,190,189,193,173,144,140,132,137,154,132,254,255,212,342]#цена Газпрома
G_d=[1.5,2.54,2.66,0.36,0.36,2.39,3.85,8.97,5.99,7.2,7.2,7.89,8.04,16.61,15.24,12.55]#дивы Газпрома
C_c=[76,70,9,69,75,60,67,80,38,76,128,190,168,230,242,2]#цена сбербанка
C_d=[0.295,0.465,0.65,0.63,0.45,1.15,2.59,3.2,3.2,0.45,1.97,6,12,16,18.7,18.7]#дивы Сбера
L_c=[2325,2100,995,1701,1753,1718,2013,1996,2239,2378,2453,3332,4980,6160,5154,6573]#цена лукойла
L_d=[33,38,42,50,52,59,115,100,120,159,187,205,225,347,396,553]#Дивы лукойла
O_c=[1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000]#цена облигаций
O_d=[80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80]#купоны
M_c=[227,377,144,223,263,184,246,328,171,211,261,277,238,320,331,299]#цена мтс
M_d=[7.6,9.67,14.84,20.15,15.4,14.54,14.71,19.82,28.8,25.17,26,26,26,28.66,29.5,37.06]#дивы мтс
R_c=[244,232,251,250,219,218,299,250,198,254,402,202,234,448,441,599]#цена роснефть
R_d=[0,1.33,1.6,1.92,2.3,2.76,4.08,8.05,12.85,8.21,11.75,9.81,21.23,26.67,18.07,24.97]
F_c=[739.59,1246.9,949.6,1655,2821,2599,2494,2546,2408,3136,5863]
F_d=[25,95.5,35.35,64.3,120,255,96,156,225,252,558]
A_c=[30,35,63,55.94,97.43,76.9,98.62,84.32,99,122.34]
A_d=[1.01,1.11,1.47,1.47,2.09,8.93,11.17,7.95,2.63,18.33]
FCK_c=[0.37,0.28,0.2,0.0902,0.046,0.059,0.2,0.16,0.15,0.2,0.22,0.16]
FCK_d=[0,0.0020524,0,0,0.0003427,0.0006648,0.0133,0.0154,0.0148,0.0249,0.0094943,0.0161]
print('Год создания портфеля')
a = int(input())
print('Год закрытия портфеля')
b = int(input())
print('Стартовый капитал')
startsum = int(input())
print('Соотношение Норникеля в портфеле.','оставшиеся для распределения доли в портфеле',1)
procentraspredeleniyGMKN = float(input())
print('Соотношение Сбербанка привеллигированного в портфеле.','оставшиеся для распределения доли в портфеле',1-procentraspredeleniyGMKN)
procentraspredeleniySBERP = float(input())
print('Соотношение Газпрома в портфеле.','оставшиеся для распределения доли в портфеле',1-procentraspredeleniyGMKN-procentraspredeleniySBERP)
procentraspredeleniyGAZP = float(input())
print('Соотношение Лукойла в портфеле.','оставшиеся для распределения доли в портфеле',round(1-procentraspredeleniyGMKN-procentraspredeleniySBERP-procentraspredeleniyGAZP,3))
procentraspredeleniyLKOH = float(input())
print('Соотношение Облигаций в портфеле.','оставшиеся для распределения доли в портфеле',round(1-procentraspredeleniyGMKN-procentraspredeleniySBERP-procentraspredeleniyGAZP-procentraspredeleniyLKOH,3))
procentraspredeleniyOFZ = float(input())
print('Соотношение МТС в портфеле.','оставшиеся для распределения доли в портфеле',round(1-procentraspredeleniyGMKN-procentraspredeleniySBERP-procentraspredeleniyGAZP-procentraspredeleniyLKOH-procentraspredeleniyOFZ,3))
procentraspredeleniyMTC = float(input())
print('Соотношение Роснефти в портфеле.','оставшиеся для распределения доли в портфеле',round(1-procentraspredeleniyGMKN-procentraspredeleniySBERP-procentraspredeleniyGAZP-procentraspredeleniyLKOH-procentraspredeleniyOFZ-procentraspredeleniyMTC,3))
procentraspredeleniyPOCH = float(input())
print('Соотшение Фосагро в портфеле. На рынке с 2011 года.','оставшиеся для распределения доли в портфеле',round(1-procentraspredeleniyGMKN-procentraspredeleniySBERP-procentraspredeleniyGAZP-procentraspredeleniyLKOH-procentraspredeleniyOFZ-procentraspredeleniyMTC-procentraspredeleniyPOCH,3))
procentraspredeleniyFOCA=float(input())
print('Соотношение Алросы в портфеле. На рынке с 2012 года.','оставшиеся для распределения доли в портфеле',round(1-procentraspredeleniyGMKN-procentraspredeleniySBERP-procentraspredeleniyGAZP-procentraspredeleniyLKOH-procentraspredeleniyOFZ-procentraspredeleniyMTC-procentraspredeleniyPOCH-procentraspredeleniyFOCA,3))
procentraspredeleniyALPO = float(input())
print('Соотношение ФСК ЕЭС в портфеле. На рынке с 2010 года.','оставшиеся для распределения доли в портфеле',round(1-procentraspredeleniyGMKN-procentraspredeleniySBERP-procentraspredeleniyGAZP-procentraspredeleniyLKOH-procentraspredeleniyOFZ-procentraspredeleniyMTC-procentraspredeleniyPOCH-procentraspredeleniyFOCA-procentraspredeleniyALPO,3))
procentraspredeleniyFCK = float(input())
for c in range(2006, 2022):
    if a == c:
        number = c - 2005
    if b == c:
        number1 = c - 2005
if (procentraspredeleniyGMKN+procentraspredeleniySBERP+procentraspredeleniyGAZP+procentraspredeleniyLKOH+procentraspredeleniyOFZ+procentraspredeleniyMTC+procentraspredeleniyPOCH+procentraspredeleniyFOCA+procentraspredeleniyALPO+procentraspredeleniyFCK)!=1.0:
    print('Ошибка при введении распределения в портфеле, портфель расчитан на сумму', startsum*round((procentraspredeleniyGMKN+procentraspredeleniySBERP+procentraspredeleniyGAZP+procentraspredeleniyLKOH+procentraspredeleniyOFZ+procentraspredeleniyMTC+procentraspredeleniyPOCH+procentraspredeleniyFOCA+procentraspredeleniyALPO+procentraspredeleniyFCK),3))
if procentraspredeleniyFOCA != 0 or procentraspredeleniyALPO != 0 or procentraspredeleniyFCK != 0:
    if procentraspredeleniyFOCA != 0 and a < 2011:
        print('Нельзя включать Фосагро в портфели раньше 2011 года. Портфель расчитан неккоректно.')
    if procentraspredeleniyALPO != 0 and a < 2012:
        print('Нельзя включать Алросу в портфели раньше 2012 года. Портфель расчитан неккоректно.')
    if procentraspredeleniyFCK != 0 and a < 2010:
        print('Нельзя включать ФСК ЕЭС в портфели раньше 2010 года. Портфель расчитан неккоректно.')
if a>=2012:
    while number != number1:
        number += 1
        OB = startsum
        chisliGMKN = int(startsum * procentraspredeleniyGMKN / (n_c[number-2]))
        chisliSBERP=int(startsum * procentraspredeleniySBERP / (C_c[number-2]) / 10) * 10
        chisliGAZP=int(startsum * procentraspredeleniyGAZP / (G_c[number-2]) / 10) * 10
        chisliLKOH=int(startsum * procentraspredeleniyLKOH / L_c[number-2])
        chisliOFZ=int(startsum * procentraspredeleniyOFZ / (O_c[number-2]))
        chisliMTC=int(startsum * procentraspredeleniyMTC / (O_c[number-2])/10)*10
        chisliPOCH=int(startsum * procentraspredeleniyPOCH / (R_c[number-2]))
        chisliFOCA=int(startsum * procentraspredeleniyFOCA / (F_c[number-2]))
        chisliALPO=int(startsum * procentraspredeleniyALPO / (A_c[number-2])/100)*10
        chisliFCK=int(startsum * procentraspredeleniyFCK / (FCK_c[number-2])/10000)*10000
        Ras=OB-chisliGMKN*n_c[number-2]-chisliSBERP*C_c[number-2]-chisliGAZP*G_c[number-2]-chisliLKOH*L_c[number-2]-chisliOFZ*O_c[number-2]-chisliMTC*M_c[number-2]-chisliPOCH*R_c[number-2]-chisliFCK*FCK_c[number-2]-chisliFOCA*F_c[number-2]-chisliALPO*A_c[number-2]
        startsum = chisliGMKN * n_c[number-1] + chisliGMKN *n_d[number-2]+chisliSBERP*C_c[number-1]+chisliSBERP*(C_d[number-2])+chisliGAZP*(G_c[number-1])+chisliGAZP*(G_d[number-2])+chisliLKOH*L_c[number-1]+chisliLKOH*L_d[number-2]+chisliOFZ*O_c[number-1]+chisliOFZ*O_d[number-2]+chisliMTC*M_c[number-1]+chisliMTC*M_d[number-1]+chisliPOCH*R_c[number-1]+chisliPOCH*R_d[number-2]+chisliFOCA*F_c[number-1]+chisliFOCA*F_d[number-2]+chisliALPO*A_c[number-1]+chisliALPO*A_d[number-2]+chisliFCK*FCK_c[number-1]+chisliFCK*FCK_d[number-2]+Ras
        print('Сумма портфеля на конец', number-1,  'года',startsum)
if a ==2011:
    while number != number1:
        number += 1
        OB = startsum
        chisliGMKN = int(startsum * procentraspredeleniyGMKN / (n_c[number-2]))
        chisliSBERP=int(startsum * procentraspredeleniySBERP / (C_c[number-2]) / 10) * 10
        chisliGAZP=int(startsum * procentraspredeleniyGAZP / (G_c[number-2]) / 10) * 10
        chisliLKOH=int(startsum * procentraspredeleniyLKOH / L_c[number-2])
        chisliOFZ=int(startsum * procentraspredeleniyOFZ / (O_c[number-2]))
        chisliMTC=int(startsum * procentraspredeleniyMTC / (M_c[number-2])/10)*10
        chisliPOCH=int(startsum * procentraspredeleniyPOCH / (R_c[number-2]))
        chisliFOCA=int(startsum * procentraspredeleniyFOCA / (F_c[number-2]))
        chisliFCK=int(startsum * procentraspredeleniyFCK / (FCK_c[number-2])/10000)*10000
        Ras=OB-chisliGMKN*n_c[number-2]-chisliSBERP*C_c[number-2]-chisliGAZP*G_c[number-2]-chisliLKOH*L_c[number-2]-chisliOFZ*O_c[number-2]-chisliMTC*M_c[number-2]-chisliPOCH*R_c[number-2]-chisliFCK*FCK_c[number-2]-chisliFOCA*F_c[number-2]
        startsum = chisliGMKN * n_c[number - 1] + chisliGMKN * n_d[number - 2] + chisliSBERP * C_c[
            number - 1] + chisliSBERP * (C_d[number - 2]) + chisliGAZP * (G_c[number - 1]) + chisliGAZP * (
                   G_d[number - 2]) + chisliLKOH * L_c[number - 1] + chisliLKOH * L_d[number - 2] + chisliOFZ * O_c[
                       number - 1] + chisliOFZ * O_d[number - 2] + chisliMTC * M_c[number - 1] + chisliMTC * M_d[
                       number - 1] + chisliPOCH * R_c[number - 1] + chisliPOCH * R_d[number - 2] + chisliFOCA * F_c[
                       number - 1] + chisliFOCA * F_d[number - 2]  + chisliFCK * FCK_c[number - 1] + chisliFCK * FCK_d[number - 2]+Ras
        print('Сумма портфеля на конец', number-1,  'года',startsum)
if a==2010:
    while number != number1:
        number += 1
        OB = startsum
        chisliGMKN = int(startsum * procentraspredeleniyGMKN / (n_c[number - 2]))
        chisliSBERP = int(startsum * procentraspredeleniySBERP / (C_c[number - 2]) / 10) * 10
        chisliGAZP = int((startsum * procentraspredeleniyGAZP / (G_c[number - 2])) / 10) * 10
        chisliLKOH = int(startsum * procentraspredeleniyLKOH / L_c[number - 2])
        chisliOFZ = int(startsum * procentraspredeleniyOFZ / (O_c[number - 2]))
        chisliMTC = int((startsum * procentraspredeleniyMTC / (M_c[number - 2])) / 10) * 10
        chisliPOCH = int(startsum * procentraspredeleniyPOCH / (R_c[number - 2]))
        chisliFCK = int(startsum * procentraspredeleniyFCK / (FCK_c[number - 2]) / 10000) * 10000
        Ras=OB-chisliGMKN*n_c[number-2]-chisliSBERP*C_c[number-2]-chisliGAZP*G_c[number-2]-chisliLKOH*L_c[number-2]-chisliOFZ*O_c[number-2]-chisliMTC*M_c[number-2]-chisliPOCH*R_c[number-2]-chisliFCK*FCK_c[number-2]
        startsum = chisliGMKN * n_c[number - 1] + chisliGMKN * n_d[number - 2] + chisliSBERP * C_c[
            number - 1] + chisliSBERP * (C_d[number - 2]) + chisliGAZP * (G_c[number - 1]) + chisliGAZP * (
                   G_d[number - 2]) + chisliLKOH * L_c[number - 1] + chisliLKOH * L_d[number - 2] + chisliOFZ * O_c[
                       number - 1] + chisliOFZ * O_d[number - 2] + chisliMTC * M_c[number - 1] + chisliMTC * M_d[
                       number - 1] + chisliPOCH * R_c[number - 1] + chisliPOCH * R_d[number - 2] +  chisliFCK * FCK_c[number - 1] + chisliFCK * FCK_d[number - 2]+Ras
        print('Сумма портфеля на конец', number-1, 'года', startsum)

if a<2010:
    while number != number1:
        number += 1
        OB=startsum
        chisliGMKN = int(startsum * procentraspredeleniyGMKN / (n_c[number-2]))
        chisliSBERP=int(startsum * procentraspredeleniySBERP / (C_c[number-2]) / 10) * 10
        chisliGAZP=int((startsum * procentraspredeleniyGAZP / (G_c[number-2])) / 10) * 10
        chisliLKOH=int(startsum * procentraspredeleniyLKOH / L_c[number-2])
        chisliOFZ=int(startsum * procentraspredeleniyOFZ / (O_c[number-2]))
        chisliMTC=int((startsum * procentraspredeleniyMTC / (M_c[number-2]))/10)*10
        chisliPOCH=int(startsum * procentraspredeleniyPOCH / (R_c[number-2]))
        Ras=OB-chisliGMKN*n_c[number-2]-chisliSBERP*C_c[number-2]-chisliGAZP*G_c[number-2]-chisliLKOH*L_c[number-2]-chisliOFZ*O_c[number-2]-chisliMTC*M_c[number-2]-chisliPOCH*R_c[number-2]
        startsum = chisliGMKN * n_c[number-1] + chisliGMKN *n_d[number-2]+chisliSBERP*C_c[number-1]+chisliSBERP*C_d[number-2]+chisliGAZP*G_c[number-1]+chisliGAZP*G_d[number-2]+chisliLKOH*L_c[number-1]+chisliLKOH*L_d[number-2]+chisliOFZ*O_c[number-1]+chisliOFZ*O_d[number-2]+chisliMTC*M_c[number-1]+chisliMTC*M_d[number-2]+chisliPOCH*R_c[number-1]+chisliPOCH*R_d[number-2]+Ras
        print('Сумма портфеля на конец', number-1,  'года',startsum)
m=input()
time.sleep(300)

