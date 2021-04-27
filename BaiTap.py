ds1=[1,2,3,4]
ds2=[1,]
ds3=[]
l1= len(ds1)
l2 = len(ds2)
if l1 > l2:
    so_phan_tu_nho = l2
    so_phan_tu_lon = l1
else:
    so_phan_tu_lon = l1
    so_phan_tu_nho = l2

for dem in range(0,so_phan_tu_nho):
    ds3.append(ds1[dem]+ds2[dem])

for dem in range( so_phan_tu_lon -(so_phan_tu_lon - so_phan_tu_nho) ,so_phan_tu_lon):
     ds3.append(ds1[dem])
print(ds3)
print(so_phan_tu_lon)
print(so_phan_tu_nho)

