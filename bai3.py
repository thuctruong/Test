ds1=[1,3]
ds2=[2,4]
ds3=[]


l1 = len(ds1)
l2 = len(ds2)

#loai bo truong hop 1 phan tu
if l1+l2 == 1:
    print(ds1+ds2)
else:
    ds3=ds1+ds2
    ds3.sort()
    l3= len(ds3)
    #xet chuoi chan or le
    if l3%2 == 0:  #truong hop so chan
        index_tv = (  ds3[ l3//2 - 1 ] + ds3[ l3//2  ] ) / 2

    else:  #truong hop so le
        index_tv = ds3[l3//2]
print(ds3)