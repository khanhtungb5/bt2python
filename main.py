import mysql.connector
import StudentService

stuserv= StudentService
check = -1
stuserv.sqlconn()
while check != 0:
    print("1. Doc file excel ")
    print("2. Xem danh sách sinh viên")
    print("3. Xem danh sach sinh vien tren CSDL")
    print("4. In du lieu vao Mysql")
    print("5. Sua du lieu trong CSDL")
    print("6. Xoa du lieu trong CSDL")
    check = int(input("Nhập số: "))
    while check < 0 or check > 6:
        check = int(input("Nhập lại số: "))

    print("*" * 50)
    if check == 1:
        stuserv.readexcel()
    elif check == 2:
        stuserv.showsv(stuserv.getlistSV())
    elif check == 3:
        stuserv.showsvinsql()
    elif check == 4:
        stuserv.insertall(stuserv.getlistSV())
    elif check == 5:
        inp= str(input("Nhap MaSV hoc sinh can sua: "))
        id1=stuserv.search(inp)
        print(id1)
        stuserv.changedata(stuserv.getlistSV(), id1)
        stuserv.update_student(stuserv.getlistSV(), id1)
    elif check == 6:
        inp = str(input("Nhap MaSV hoc sinh can xoa: "))
        id1 = stuserv.search(inp)
        stuserv.deletedata(id1)
    else:
        break

    print("*" * 50)