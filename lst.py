ism=[]
fam=[]
for i in range(10):
    a=input()
    b=input()
    ism.append(a)
    fam.append(b)
print(f"{ism}\n{fam}")
cnt1=0
cnt2=0
for i in range(len(fam)):
    if fam[i][-1]=="a":
        cnt2+=1
    else:
        cnt1+=1
print(f"Guruhda {cnt1}ta ug`il\n{cnt2}ta qiz mavjud")