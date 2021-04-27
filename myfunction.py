def create_facebook_acc():
    print("Create facebook")

def create_database():
    print("Create Database")

def phep_cong(x,y):
    print(x+y)

def phep_cong_tru(x,y,dau="+"):
   if dau == "+":
        a = x+y
   elif dau == "-":
        a = x-y
   return a

def phep_tinh(x,y,z):
    """ Doc string cua ham """
    a = 0
    if z == "+":
        a == x + y
    elif z == "-":
        a == x - y
    return a

def xin_chao(*name,loi_chao):  # ham tuy bien
    print(loichao)
    for i in name:
        print(i)


#ham vo danh
def double_v(x):
    return x*3

# double_val

ds_goc=[1,2,3,4,5,6,7,8,9]
ds_moi = list(filter(lambda x:x%2==0,ds_goc ))
print(ds_moi)
ds_moi = list(map(lambda x: x * 2,ds_goc ))
print(ds_moi)

