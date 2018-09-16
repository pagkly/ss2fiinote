#39\5bbf
#b'blob 151\x00
startp=135
interest=40/10000
endp=0
year=5
for f in range(1,year*365):
    endp=(10040/10000)*startp
    startp=endp
    #print(startp)
print(startp)
