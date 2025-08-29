from datetime import datetime
class Menu:
    def Main_Menu(self):
        print("Bienvenido al supermercado Bing Bong")
        print("1.Ingreso de datos")
        print("2.Realizar compra")
        print("3.Realizar venta")
        print("4.Mostrar inventario")
        print("5.Movimientos")
        print("6.Personas")
        print("7.Modificar productos")
        print("8.Salir")
    def Pur_Menu(self):
        print("Opciones de compra")
        print("1.Nuevo producto")
        print("2.Restock")
        print("3.Salir")
    def Inv_Menu(self):
        print("Inventario")
        print("1.Productos")
        print("2.Categorias")
        print("3.Salir")
    def Move_Menu(self):
        print("Movimientos")
        print("1.Compras")
        print("2.Ventas")
        print("3.Estadisticas")
        print("4.Salir")
    def Per_Menu(self):
        print("Personas relevantes")
        print("1.Empleados")
        print("2.Proveedores")
        print("3.Clientes")
        print("4.Salir")
    def In_Menu(self):
        print("Ingreso de datos al sistema")
        print("1.Categorías")
        print("2.Empleados")
        print("3.Proveedores")
        print("4.Clientes")
        print("5.Salir")
class Clients:
    def __init__(self, Nit,Name,Phone,Adress,Mail):
        self.Nit = Nit
        self.Name = Name
        self.Phone = Phone
        self.Adress = Adress
        self.Mail = Mail
class Employees:
    def __init__(self,Ecode,Name,Phone,Adress,Mail,Salary):
        self.Ecode = Ecode
        self.Name = Name
        self.Phone = Phone
        self.Adress = Adress
        self.Mail = Mail
        self.Salary = Salary
class Category:
    def __init__(self,Cat_Code,Name):
        self.Cat_Code = Cat_Code
        self.Name = Name
class Products:
    def __init__(self,ID_Pro,Name,Category,Price,Tpurchase,Tsells):
        self.ID_Pro = ID_Pro
        self.Name = Name
        self.Category = Category
        self.Price = Price
        self.Tpurchase = Tpurchase
        self.Tsells = Tsells
        self.Stock = Tpurchase - Tsells
class Suppliers:
    def __init__(self,ID_Sup,Name,Company,Phone,Adress,Mail,Category):
        self.ID_Sup = ID_Sup
        self.Name = Name
        self.Company = Company
        self.Phone = Phone
        self.Adress = Adress
        self.Mail = Mail
        self.Category = Category
class Sells:
    def __init__(self,ID_Sell,Date,Client,Employee,Total):
        self.ID_Sell = ID_Sell
        self.Date = Date
        self.Client = Client
        self.Employee = Employee
        self.Total = Total
class Sells_Details:
    def __init__(self,ID_SD,Quantity,Product,Price,SubTotal,Sell):
        self.ID_SD = ID_SD
        self.Quantity = Quantity
        self.Product = Product
        self.Price = Price
        self.SubTotal = SubTotal
        self.Sell = Sell
class Purchase:
    def __init__(self,ID_Pur,Date,Supplier,Employee,Total):
        self.ID_Pur = ID_Pur
        self.Date = Date
        self.Supplier = Supplier
        self.Employee = Employee
        self.Total = Total
class Purchase_Details:
    def __init__(self,ID_PD,Purchase,Quantity,Product,P_Price,SubTotal,Expiration):
        self.ID_PD = ID_PD
        self.Purchase = Purchase
        self.Quantity = Quantity
        self.Product = Product
        self.P_Price = P_Price
        self.SubTotal = SubTotal
        self.Expiration = Expiration
class Mod_Category:
    def __init__(self):
        self.categorys = {}
        self.Load_Cat()
    def Load_Cat(self):
        try:
            with open("Categorias.txt","r", encoding = "utf-8") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        Cat_Code,Name = line.split(":")
                        self.categorys[Cat_Code] = {'Nombre':Name}
        except FileNotFoundError:
            print("No existe el archivo de categorias.txt")
    def Save_Cat(self):
        with open("Categorias.txt","w", encoding = "utf-8") as file:
            for code, value in self.categorys.items():
                file.write(f"{code}:{value['Nombre']}\n")
    def Add_Cat(self,cat):
        self.categorys[cat.Cat_Code] = {'Nombre': cat.Name}
    def Check_C(self):
        if len(self.categorys) == 0:
            return False
        else:
            return True
    def Show_Cat(self):
        count = 1
        for code, value in self.categorys.items():
            print(f"Categoria {count}")
            print(f"Nombre: {value['Nombre']} - Código: {code}")
            print(" ")
            count += 1
    def Find_Cat(self,look):
        find = -1
        for code, value in self.categorys.items():
            if look == code:
                find = code
        return find
    def Cat_Name(self,Code):
        category = " "
        for code,value in self.categorys.items():
            if code == Code:
                category = value['Nombre']
        return category
class Mod_Employee:
    def __init__(self):
        self.employees = {}
        self.Load_Employee()
    def Load_Employee(self):
        try:
            with open("Empleados.txt","r", encoding = "utf-8") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        Ecode,Name,Phone,Adress,Mail,Salary = line.split(":")
                        self.employees[Ecode] = {'Nombre':Name,'Telefono':Phone,'Dirección':Adress,'Correo':Mail,'Salario':Salary}
        except FileNotFoundError:
            print("El archivo de empleados.txt no existe")
    def Save_Emp(self):
        with open("Empleados.txt","w", encoding = "utf-8") as file:
            for code, value in self.employees.items():
                file.write(f"{code}:{value['Nombre']}:{value['Telefono']}:{value['Dirección']}:{value['Correo']}:{value['Salario']}\n")
    def Add_Emp(self,emp):
        self.employees[emp.Ecode] = {'Nombre': emp.Name,'Telefono':emp.Phone,'Dirección':emp.Adress,'Correo':emp.Mail,
                                      'Salario':emp.Salary}
    def Show_Emp(self):
        count = 1
        for key,value in self.employees.items():
            print(f"Empleado {count}")
            print(f"Código: {key}, Nombre: {value['Nombre']}, Telefono: {value['Telefono']},"
                  f" Dirección: {value['Dirección']}, Correo: {value['Correo']}, Salario: {value['Salario']}")
    def Check_Emp(self):
        if len(self.employees) == 0:
            return False
        else:
            return True
    def Find_Emp(self,emp):
        employee = -1
        for code, value in self.employees.items():
            if emp == code:
                employee = code
        return employee
class Mod_Supplier:
    def __init__(self):
        self.suppliers = {}
        self.Load_Supplier()
    def Load_Supplier(self):
        try:
            with open("Proveedores.txt","r", encoding = "utf-8") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        ID_sup,Name,Company,Phone,Adress,Mail,Category = line.split(":")
                        self.suppliers[ID_sup] = {'Nombre':Name,'Empresa':Company,'Telefono':Phone,'Dirección':Adress,'Correo':Mail,
                                                  'Categoria':Category}
        except FileNotFoundError:
            print("El archivo Proveedores.txt no existe")
    def Save_Prov(self):
        with open("Proveedores.txt","w", encoding = "utf-8") as file:
            for code, value in self.suppliers.items():
                file.write(f"{code}:{value['Nombre']}:{value['Empresa']}:{value['Telefono']}:{value['Dirección']}:{value['Correo']}:{value['Categoria']}\n")
    def Add_Sup(self,sup):
        self.suppliers[sup.ID_Sup] = {'Nombre': sup.Name,'Empresa': sup.Company,'Telefono':sup.Phone,
                                      'Dirección': sup.Adress,'Correo':sup.Mail,'Categoria':sup.Category}
    def Show_Sup(self):
        count = 1
        for code, value in self.suppliers.items():
            cat = mod_c.Cat_Name(value['Categoria'])
            print(f"Proveedor {count}")
            print(f"Código {code}, Nombre: {value['Nombre']}, Empresa: {value['Empresa']}")
            print(f"Telefno: {value['Telefono']}, Dirección: {value['Dirección']}, Correo: {value['Correo']}")
            print(f"Categoria: {cat}")
            count = count + 1
            print(" ")
    def Check_Sup(self):
        if len(self.suppliers) == 0:
            return False
        else:
            return True
    def Find_Sup(self,sup):
        supplier = -1
        for code, value in self.suppliers.items():
            if sup == code:
                supplier = code
        return supplier
class Mod_Product:
    def __init__(self):
        self.products = {}
        self.Load_Product()
    def Load_Product(self):
        try:
            with open("Productos.txt", "r", encoding = "utf-8") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        ID_pro,Name,Category,Price,Stock = line.split(":")
                        self.products[ID_pro] = {'Nombre':Name,'Categoría':Category,'Precio':Price,'Stock':Stock}
        except FileNotFoundError:
            print("El archivo Productos.txt  no existe")
    def Save_Prod(self):
        with open("Productos.txt","w", encoding = "utf-8") as file:
            for code, value in self.products.items():
                file.write(f"{code}:{value['Nombre']}:{value['Categoría']}:{value['Precio']}:{value['Stock']}\n")
    def Add_Product(self,product):
        self.products[product.ID_Pro] = {'Nombre': product.Name,'Categoría':product.Category,'Precio':product.Price,
                                        'Stock':product.Stock}
    def Show_Product(self):
        count = 1
        for key,value in self.products.items():
            print(f"Producto {count}")
            print(f"Codigo de producto: {key}, Nombre: {value['Nombre']},Categoría: {value['Categoría']},"
                  f" Precio: {value['Precio']}, Stock: {value['Stock']}")
            count = count + 1
    def Check_Product(self):
        if len(self.products) == 0:
            return False
        else:
            return True
    def Find_Product(self,prod):
        product = -1
        for code, value in self.products.items():
            if prod == code:
                product = code
        return product
    def Get_Price(self,code):
        price = 0
        for key,value in self.products.items():
            if code == key:
                price = value['Precio']
        return price
    def Check_Stock(self,code):
        stock = 0
        for key,value in self.products.items():
            if code == key:
                stock = value['Stock']
        return stock
    def Selling(self,code,quantity):
        for key,value in self.products.items():
            if code == key:
                value['Stock'] = value['Stock'] - quantity
    def Buying(self,code,quantity):
        for key,value in self.products.items():
            if code == key:
                value['Stock'] = value['Stock'] + quantity
class See_Purchase:
    def __init__(self):
        self.purchases = {}
        self.Load_Purchase()
    def Load_Purchase(self):
        try:
            with open("Compras.txt","r", encoding = "utf-8") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        ID_pur,Date,Supplier,Employee,Total = line.split("/")
                        self.purchases[ID_pur] = {'Fecha':Date,'Proveedor':Supplier,'Empleado':Employee,'Total':Total}
        except FileNotFoundError:
            print("El archivo Compras.txt no existe")
    def Save_Pur(self):
        with open("Compras.txt","w", encoding = "utf-8") as file:
            for code, value in self.purchases.items():
                file.write(f"{code}/{value['Fecha']}/{value['Proveedor']}/{value['Empleado']}/{value['Total']}\n")
    def Add_Pur(self,pur):
        self.purchases[pur.ID_Pur] = {'Fecha':pur.Date,'Proveedor':pur.Supplier,'Empleado':pur.Employee,'Total':pur.Total}
    def Show_Pur(self):
        count = 1
        for key,value in self.purchases.items():
            print(f"Compra {count}")
            print(f"Proveedor: {value['Proveedor']}, Empleado a cargo: {value['Empleado']}, Fecha: {value['Fecha']}")
            see_pd.Show_Pur_De(key)
            print(f"Total = {value['Total']}")
            count = count + 1
            print(" ")
    def Check_Pur(self):
        if len(self.purchases) == 0:
            return False
        else:
            return True
class See_Purchase_Details:
    def __init__(self):
        self.purchase_Details = {}
        self.Load_Purchase_Details()
    def Load_Purchase_Details(self):
        try:
            with open("DetalleCom.txt","r", encoding = "utf-8") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        ID_PD,Purchase,Quantity,Product,Price,SubTotal,Expiration = line.split(":")
                        self.purchase_Details[ID_PD] = {'Codigo compra': Purchase,'Cantidad': Quantity,'Producto':Product,'Precio':Price,'SubTotal':SubTotal,'Caducidad':Expiration}
        except FileNotFoundError:
            print("El archivo DetalleCom.txt no existe")
    def Save_Pur_De(self):
        with open("DetalleCom.txt","w", encoding = "utf-8") as file:
            for code, value in self.purchase_Details.items():
                file.write(f"{code}:{value['Codigo compra']}:{value['Cantidad']}:{value['Producto']}:{value['Precio']}:{value['SubTotal']}:{value['Caducidad']}\n")
    def Add_Pur_De(self,pur):
        self.purchase_Details[pur.ID_PD] = {'Codigo compra':pur.Purchase,'Cantidad': pur.Quantity, 'Producto':pur.Product,
                                            'Precio': pur.P_Price,'SubTotal': pur.SubTotal, 'Caducidad': pur.Expiration}
    def Show_Pur_De(self,code):
        count = 1
        for key,value in self.purchase_Details.items():
            if code == value['Codigo compra']:
                print(f"Producto: {count}")
                print(f"Producto: {value['Producto']}, Precio: {value['Precio']} X Cantidad: {value['Cantidad']}"
                      f" = SubTotal: {value['SubTotal']}")
                print(" ")
                count = count + 1
class Mod_Clients:
    def __init__(self):
        self.clients = {}
        self.Load_Clients()
    def Load_Clients(self):
        try:
            with open("Clientes.txt","r", encoding = "utf-8") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        Nit,Name,Phone,Adress,Mail = line.split(":")
                        self.clients[Nit] = {'Nombre':Name,'Telefono':Phone,'Dirección':Adress,'Correo':Mail}
        except FileNotFoundError:
            print("El archivo Clientes.txt no existe")
    def Save_Clients(self):
        with open("Clientes.txt","w", encoding = "utf-8") as file:
            for code, value in self.clients.items():
                file.write(f"{code}:{value['Nombre']}:{value['Telefono']}:{value['Dirección']}:{value['Correo']}\n")
    def Add_Client(self,client):
        self.clients[client.Nit] = {'Nombre': client.Name,'Telefono': client.Phone, 'Dirección': client.Adress,
                                    'Correo': client.Mail}
    def Check_Client(self):
        if len(self.clients) == 0:
            return False
        else:
            return True
    def Show_Client(self):
        count = 1
        for key,value in self.clients.items():
            print(f"Cliente {count}")
            print(f"NIT: {key}, Nombre: {value['Nombre']}, Telefono: {value['Telefono']}, Correo: {value['Correo']},"
                  f" Dirección: {value['Dirección']}")
            count = count + 1
    def Find_Client(self,find):
        client = -1
        for key,value in self.clients.items():
            if find == key:
                client = key
        return client
class See_Sell:
    def __init__(self):
        self.sellers = {}
        self.Load_Sells()
    def Load_Sells(self):
        try:
            with open("Ventas.txt","r", encoding = "utf-8") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        ID_Sell,Date,Client,Employee,Total = line.split(":")
                        self.sellers[ID_Sell] = {'Fecha':Date,'Cliente':Client,'Empleado':Employee,'Total':Total}
        except FileNotFoundError:
            print("El archivo Ventas.txt no existe")
    def Save_Sells(self):
        with open("Ventas.txt","w", encoding = "utf-8") as file:
            for code, value in self.sellers.items():
                file.write(f"{code}:{value['Fecha']}:{value['Cliente']}:{value['Empleado']}:{value['Total']}\n")
    def Add_Seller(self,seller):
        self.sellers[seller.ID_Sell] = {'Fecha':seller.Date,'Cliente':seller.Client,'Empleado':seller.Employee,'Total':seller.Total}
    def Show_Seller(self):
        count = 1
        for key,value in self.sellers.items():
            print(f"Venta: {count}")
            print(f"Cliente: {value['Cliente']}, Empleado: {value['Empleado']}, Fecha: {value['Fecha']}")
            see_sell_de.Show_Sell_De(key)
            print(f"Total = {value['Total']}")
            count = count + 1
            print(" ")
    def Check_Sell(self):
        if len(self.sellers) == 0:
            return False
        else:
            return True
class See_Sell_De:
    def __init__(self):
        self.sellers_details = {}
        self.Load_Sell_Details()
    def Load_Sell_Details(self):
        try:
            with open("DetalleVentas.txt","r", encoding = "utf-8") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        ID_SD,Quantity,Product,Price,Sell,SubTotal = line.split(":")
                        self.sellers_details[ID_SD] = {'Cantidad':Quantity,'Producto':Product,'Precio':Price,'Venta':Sell,'Subtotal':SubTotal}
        except FileNotFoundError:
            print("El archivo DetalleVentas.txt no existe")
    def Save_Sell_D(self):
        with open("DetalleVentas.txt","w", encoding = "utf-8") as file:
            for code, value in self.sellers_details.items():
                file.write(f"{code}:{value['Cantidad']}:{value['Producto']}:{value['Precio']}:{value['Venta']}:{value['Subtotal']}\n")
    def Add_Seller_Details(self,seller):
        self.sellers_details[seller.ID_SD] = {'Cantidad':seller.Quantity,'Producto':seller.Product,'Precio': seller.Price,'Venta': seller.Sell,
                                              'Subtotal': seller.SubTotal}
    def Show_Sell_De(self,code):
        count = 1
        for key,value in self.sellers_details.items():
            if code == value['Venta']:
                sub = value['Precio'] * value['Cantidad']
                print(f"Producto: {count}")
                print(f"Producto: {value['Producto']}, Precio: {value['Precio']} X Cantidad: {value['Cantidad']} = SubTotal: {sub}")
                count = count + 1
class Codes:
    def __init__(self):
        self.Codes = {}
        self.Load_Codes()
    def Check_Codes(self):
        if len(self.Codes) == 0:
            return False
        else:
            return True
    def Load_Codes(self):
        try:
            with open("Codes.txt","r", encoding = "utf-8") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        cC, cE, cP, cPu, cPr, cPud, cCl, cS, cSd = line.split(":")
                        self.Codes[0]={'C1':cC,'C2':cP,'C3':cPu,'C4':cPr,'C5':cPud,'C6':cCl,'C7':cS,'C8':cSd,'C9':cE}
        except FileNotFoundError:
            print("El archivo Codes.txt no existe")
    def Save_Codes(self,cC,cE,cP,cPu,cPr,cPud,cCl,cS,cSd):
        with open("Codes.txt","w", encoding = "utf-8") as file:
            file.write(f"{cC}:{cE}:{cP}:{cPu}:{cPr}:{cPud}:{cCl}:{cS}:{cSd}")
    def Get_CC(self):
        cC = self.Codes[0]['C1']
        return cC
    def Get_CE(self):
        cE = self.Codes[0]['C9']
        return cE
    def Get_CP(self):
        cP = self.Codes[0]['C2']
        return cP
    def Get_CPU(self):
        cPu = self.Codes[0]['C3']
        return cPu
    def Get_CPR(self):
        cPr = self.Codes[0]['C4']
        return cPr
    def Get_CPUD(self):
        cPud = self.Codes[0]['C5']
        return cPud
    def Get_CCL(self):
        cCl = self.Codes[0]['C6']
        return cCl
    def Get_CS(self):
        cS = self.Codes[0]['C7']
        return cS
    def Get_CSD(self):
        cSd = self.Codes[0]['C8']
        return cSd
menus = Menu()
code = Codes()
mod_c = Mod_Category()
mod_prov = Mod_Supplier()
mod_emp = Mod_Employee()
mod_prod = Mod_Product()
see_p = See_Purchase()
see_pd = See_Purchase_Details()
mod_clie = Mod_Clients()
see_sell = See_Sell()
see_sell_de = See_Sell_De()
first = True
start = code.Check_Codes()
if start == False:
    contC = 0
    contE = 0
    contProv = 0
    contPur = 0
    contProd = 0
    contPur_de = 0
    contCli = 0
    contSell = 0
    contSell_de = 0
else:
    contC = int(code.Get_CC())
    contE = int(code.Get_CE())
    contProv = int(code.Get_CP())
    contPur = int(code.Get_CPU())
    contProd = int(code.Get_CPR())
    contPur_de = int(code.Get_CPUD())
    contCli = int(code.Get_CCL())
    contSell = int(code.Get_CS())
    contSell_de = int(code.Get_CSD())
while 0 != 1:
    try:
        menus.Main_Menu()
        opt = input("Ingrese la opcion que desee: ")
        match opt:
            case "1":
                count = 1
                menus.In_Menu()
                opt1 = input("Seleccione el ingreso que desee: ")
                match opt1:
                    case "1":
                        num = int(input("Cuantas categorías desea ingresar: "))
                        if num <= 0:
                            print("La cantidad ingresada no es valida")
                        else:
                            for i in range(num):
                                cat_code = f"C{contC}"
                                while 0 != 1:
                                    print(f"Ingreso de la categoría {count}")
                                    name = input("Ingrese el nombre de la categoria: ")
                                    if name == "":
                                        print("No puede dejar este espacio en blanco")
                                    else:
                                        break
                                cat = Category(cat_code, name)
                                count = count + 1
                                contC = contC + 1
                                mod_c.Add_Cat(cat)
                    case "2":
                        count = 0
                        num = int(input("Cuantos empleados desea ingresar:"))
                        if num <= 0:
                            print("La cantidad ingresada no es valida")
                        else:
                            for i in range(num):
                                emp_code = f"E{contE}"
                                while 0 != 1:
                                    print(f"Ingreso de la empleado {count+1}")
                                    name = input("Ingrese el nombre del empleado/a: ")
                                    if name == "":
                                        print("No puede dejar el espacio en blanco")
                                    else:
                                        phone = input("Ingrese su telefono: ")
                                        adress = input("Ingrese su dirección: ")
                                        mail = input("Ingrese su correo: ")
                                        salary = int(input("Ingrese su salario: "))
                                        if salary <= 0:
                                            print("El salario ingresado no es valido")
                                        else:
                                            break
                                emp = Employees(emp_code, name, phone, adress, mail,salary)
                                count = count + 1
                                contE = contE + 1
                                mod_emp.Add_Emp(emp)
                    case "3":
                        count = 0
                        num = int(input("Cuantos prooverdores desea ingresar: "))
                        if num <= 0:
                            print("La cantidad ingresada no es valida")
                        else:
                            for i in range(num):
                                Prov_code = f"Prov{contProv}"
                                while 0 != 1:
                                    print(f"Ingreso de la prooverdore {count+1}")
                                    name = input("Ingrese el nombre del prooverdore: ")
                                    if name == "":
                                        print("No puede dejar este espacio en blanco")
                                    else:
                                        Company = input("Ingrese el nombre de su empresa(Si no tiene deje en blanco el espacio: ")
                                        if Company == "":
                                            Company = "N/A"
                                        phone = input("Ingrese el telefono del prooverdor: ")
                                        adress = input("Ingrese la dirección del proveedor: ")
                                        mail = input("Ingrese el correo del proveedor:")
                                        category= input("Ingrese el código de la categoría que provee: ")
                                        find = mod_c.Find_Cat(category)
                                        if find == -1:
                                            print("No se a encontrado ninguna categoría con ese código")
                                        else:
                                            break
                                supplier = Suppliers(Prov_code, name, Company, phone, adress, mail, find)
                                mod_prov.Add_Sup(supplier)
                                contProv = contProv + 1
                    case "4":
                        count = 1
                        num = int(input("Cuantos clientes desea ingresar: "))
                        if num <= 0:
                            print("La cantidad ingresada no es valida")
                        else:
                            for i in range(num):
                                nit = f"CL{contCli}"
                                while 0 != 1:
                                    print(f"Cliente {count}")
                                    name = input("Ingrese el nombre del cliente: ")
                                    if name == "":
                                        print("No puede dejar el espacio en blanco")
                                    else:
                                        phone = input("Ingrese el telefono del cliente: ")
                                        adress = input("Ingrese la dirección del cliente: ")
                                        mail = input("Ingrese el correo del cliente:")
                                        break
                                client = Clients(nit,name,phone,adress,mail)
                                mod_clie.Add_Client(client)
                                contCli = contCli + 1
                    case "5":
                        pass
                    case _:
                        print("La opción seleccionada no es valida")
            case "2":
                empty = mod_emp.Check_Emp()
                empty1 = mod_prov.Check_Sup()
                if empty == False:
                    print("No se pueden realizar compras porque no hay empleados registrados")
                else:
                    if empty1 == False:
                        print("No se pueden realizar compras porque no hay proveedores registrados")
                    else:
                        if first == True:
                            employee = input("Ingrese el código del empleado a cargo de la compra: ")
                            look = mod_emp.Find_Emp(employee)
                            if look == -1:
                                print("No hay ningún empleado con ese código")
                            else:
                                supplier = input("Ingrese el código del proveedor a cargo de la venta")
                                look = mod_prov.Find_Sup(supplier)
                                if look == -1:
                                    print("No existe ningún proveedor con ese código")
                                else:
                                    num = int(input("Cuantos productos se van a comprar(tipos, no cantidad total): "))
                                    if num <= 0:
                                        print("La cantidad ingresada no es valida")
                                    else:
                                        code_pur = f"Com{contPur}"
                                        total = 0
                                        time = datetime.now()
                                        for i in range(num):
                                            code_prod = f"Prod{contProd}"
                                            code_pur_de = f"PurDe{contPur_de}"
                                            name = input("Ingrese el nombre del producto: ")
                                            if name == "":
                                                print("No puede dejar este espacio vacío")
                                            else:
                                                category = input("Ingrese el código de la categoría del producto")
                                                find = mod_c.Find_Cat(category)
                                                if find == -1:
                                                    print("No se a encontrado ninguna categoría con ese código")
                                                else:
                                                    s_price = int(input("Ingrese el precio de venta del producto: "))
                                                    if s_price <= 0:
                                                        print("El precio ingresado no es valido")
                                                    else:
                                                        quantity = int(input("Ingrese la cantidad de este producto que va"
                                                                             " a comprar"))
                                                        if quantity <= 0:
                                                            print("La cantidad ingresada no es valida")
                                                        else:
                                                            p_price = int(input("Ingrese el precio de compra del producto: "))
                                                            if p_price <= 0:
                                                                print("El precio ingresado no es valido")
                                                            else:
                                                                sub_total = p_price * quantity
                                                                total = total + sub_total
                                                                expiration = input("Ingrese la fecha de caducidad"
                                                                                   " del producto(Si no tiene deje el espacio"
                                                                                   "en blanco: ")
                                                                if expiration == "":
                                                                    expiration = "N/A"
                                                                product = Products(code_prod, name, category,
                                                                                   s_price,quantity,0)
                                                                mod_prod.Add_Product(product)
                                                                contProd += 1
                                                                pur_de = Purchase_Details(code_pur_de,code_pur,quantity,
                                                                                          code_prod,p_price,sub_total,
                                                                                          expiration)
                                                                see_pd.Add_Pur_De(pur_de)
                                                                contPur_de += 1
                                        contPur = contPur + 1
                                        purchase = Purchase(code_pur,time,supplier,employee,total)
                                        see_p.Add_Pur(purchase)
                                        first = False
                        else:
                            menus.Pur_Menu()
                            opt1 = input("Ingrese la opción que desee: ")
                            match opt1:
                                case "1":
                                    employee = input("Ingrese el código del empleado a cargo de la compra: ")
                                    look = mod_emp.Find_Emp(employee)
                                    if look == -1:
                                        print("No hay ningún empleado con ese código")
                                    else:
                                        supplier = input("Ingrese el código del proveedor a cargo de la venta")
                                        look = mod_prov.Find_Sup(supplier)
                                        if look == -1:
                                            print("No existe ningún proveedor con ese código")
                                        else:
                                            num = int(input("Cuantos productos se van a comprar(tipos, no cantidad total): "))
                                            if num <= 0:
                                                print("La cantidad ingresada no es valida")
                                            else:
                                                code_pur = f"Com{contPur}"
                                                total = 0
                                                time = datetime.now()
                                                for i in range(num):
                                                    code_prod = f"Prod{contProd}"
                                                    code_pur_de = f"PurDe{contPur_de}"
                                                    name = input("Ingrese el nombre del producto: ")
                                                    if name == "":
                                                        print("No puede dejar este espacio vacío")
                                                    else:
                                                        category = input("Ingrese el código de la categoría del producto")
                                                        find = mod_c.Find_Cat(category)
                                                        if find == -1:
                                                            print("No se a encontrado ninguna categoría con ese código")
                                                        else:
                                                            s_price = int(input("Ingrese el precio de venta del producto: "))
                                                            if s_price <= 0:
                                                                print("El precio ingresado no es valido")
                                                            else:
                                                                quantity = int(
                                                                    input("Ingrese la cantidad de este producto que va"
                                                                          " a comprar"))
                                                                if quantity <= 0:
                                                                    print("La cantidad ingresada no es valida")
                                                                else:
                                                                    p_price = int(
                                                                        input("Ingrese el precio de compra del producto: "))
                                                                    if p_price <= 0:
                                                                        print("El precio ingresado no es valido")
                                                                    else:
                                                                        sub_total = p_price * quantity
                                                                        total = total + sub_total
                                                                        expiration = input("Ingrese la fecha de caducidad"
                                                                                           " del producto(Si no tiene deje el espacio"
                                                                                           "en blanco: ")
                                                                        if expiration == "":
                                                                            expiration = "N/A"
                                                                        product = Products(code_prod, name, category,
                                                                                           s_price, quantity, 0)
                                                                        mod_prod.Add_Product(product)
                                                                        contProd += 1
                                                                        pur_de = Purchase_Details(contPur_de, code_pur,
                                                                                                  quantity,
                                                                                                  code_prod, p_price, sub_total,
                                                                                                  expiration)
                                                                        see_pd.Add_Pur_De(pur_de)
                                                                        contPur_de += 1
                                                contPur = contPur + 1
                                                purchase = Purchase(code_pur, time, supplier, employee, total)
                                                see_p.Add_Pur(purchase)
                                case "2":
                                    total = 0
                                    employee = input("Ingrese el código del empleado a cargo de la compra: ")
                                    look = mod_emp.Find_Emp(employee)
                                    if look == -1:
                                        print("No hay ningún empleado con ese código")
                                    else:
                                        supplier = input("Ingrese el código del proveedor a cargo de la venta")
                                        look = mod_prov.Find_Sup(supplier)
                                        if look == -1:
                                            print("No existe ningún proveedor con ese código")
                                        else:
                                            code_pur = f"Com{contPur}"
                                            time = datetime.now()
                                            while 0 != 1:
                                                code_pur_de = f"PurDe{contPur_de}"
                                                product = input("Ingrese el código del producto para restock: ")
                                                look = mod_prod.Find_Product(product)
                                                if product == "CALLIOPE":
                                                    break
                                                if look == -1:
                                                    print("No se encontró ningún producto con ese código")
                                                else:
                                                    quantity = int(input("Cuantas unidades va a comprar: "))
                                                    price = mod_prod.Get_Price(product)
                                                    expiration = input("Ingrese la fecha de caducidad"" del producto(Si no tiene deje el espacio"
                                                                       "en blanco: ")
                                                    if expiration == "":
                                                        expiration = "N/A"
                                                    subtotal = quantity * price
                                                    total = total + subtotal
                                                    pur_de = Purchase_Details(contPur_de, code_pur,quantity,code_prod,price, subtotal,expiration)
                                                    contPur_de += 1
                                            contPur = contPur + 1
                                            purchase = Purchase(code_pur, time, supplier, employee, total)
                                            see_p.Add_Pur(purchase)
                                case "3":
                                    pass
                                case _:
                                    print("La opción seleccionada no es valida")
            case "3":
                empty = mod_emp.Check_Emp()
                if empty == False:
                    print("No se pueden realizar ventas si no hay empleados")
                else:
                    empty1 = mod_clie.Check_Client()
                    if empty1 == False:
                        print("No se pueden realizar ventas si no hay clientes")
                    else:
                        empty2 = mod_prod.Check_Product()
                        if empty2 == False:
                            print("No se pueden realizar ventas si no hay productos")
                        else:
                            employee = input("Ingrese el código del empleado a cargo de la venta: ")
                            look = mod_emp.Find_Emp(employee)
                            if look == -1:
                                print("No hay ningún empleado con ese código")
                            else:
                                client = input("Ingrese el Nit del cliente que hace la compra: ")
                                look = mod_clie.Find_Client(client)
                                if look == -1:
                                    print("No hay ningún cliente que coincida")
                                else:
                                    num = int(input("Cantidad de productos que sea van a vender(tipo de producto no total): "))
                                    if num <= 0:
                                        print("La cantidad ingresada no es valida")
                                    else:
                                        code_sell = f"S{contSell}"
                                        time = datetime.now()
                                        total = 0
                                        for i in range(num):
                                            code_sell_de = f"SD{contSell_de}"
                                            product = input("Ingrese el código del producto que se vende: ")
                                            look = mod_prod.Find_Product(product)
                                            if look == -1:
                                                print("No hay ningún producto que coincida")
                                            else:
                                                price = mod_prod.Get_Price(product)
                                                stock = mod_prod.Check_Stock(product)
                                                quantity = int(input("Ingrese la cantidad que va a vender del producto: "))
                                                if quantity <= 0 or quantity > stock:
                                                    print("La cantidad ingresada no es valida")
                                                else:
                                                    sub_total = price * quantity
                                                    total = total + sub_total
                                                    sell_de = Sells_Details(code_sell_de,quantity,product,price,sub_total,code_sell)
                                                    see_sell_de.Add_Seller_Details(sell_de)
                                                    mod_prod.Selling(product,quantity)
                                                    contSell_de += 1
                                        sell = Sells(code_sell,time,client,employee,total)
                                        see_sell.Add_Seller(sell)
            case "4":
                menus.Inv_Menu()
                opt1 = input("Seleccione que parte del inventario desea ver: ")
                match opt1:
                    case "1":
                        empty = mod_prod.Check_Product()
                        if empty == False:
                            print("No hay ningún producto que mostrar")
                        else:
                            mod_prod.Show_Product()
                    case "2":
                        empty = mod_c.Check_C()
                        if empty == False:
                            print("No hay ninguna categoría que mostrar")
                        else:
                            mod_c.Show_Cat()
                    case "3":
                        pass
                    case _:
                        print("La opción selecionada no es valida")
            case "5":
                menus.Move_Menu()
                opt1 = input("Seleccione cual movimiento desea ver: ")
                match opt1:
                    case "1":
                        empty = see_p.Check_Pur()
                        if empty == False:
                            print("No hay ninguna compra que mostrar")
                        else:
                            see_p.Show_Pur()
                    case "2":
                        empty = see_sell.Check_Sell()
                        if empty == False:
                            print("No hay ninguna venta que mostrar")
                        else:
                            see_sell.Show_Seller()
                    case "3":
                        pass
                    case "4":
                        pass
                    case _:
                        print("La opción seleccionada no es valida")
            case "6":
                menus.Per_Menu()
                opt1 = input("Seleccione el ingreso que desea ver: ")
                match opt1:
                    case "1":
                        empty = mod_emp.Check_Emp()
                        if empty == False:
                            print("No hay ningún empleado que mostrar")
                        else:
                            mod_emp.Show_Emp()
                    case "2":
                        empty = mod_prov.Check_Sup()
                        if empty == False:
                            print("No hay ningún proveedor que mostrar")
                        else:
                            mod_prov.Show_Sup()
                    case "3":
                        empty = mod_clie.Check_Client()
                        if empty == False:
                            print("No hay ningún cliente que mostrar")
                        else:
                            mod_clie.Show_Client()
                    case "4":
                        pass
                    case _:
                        print("Opción ingresada no valida")
            case "7":
                pass
            case "8":
                print("Gracias por utilizar el programa")
                mod_c.Save_Cat()
                code.Save_Codes(contC,contE,contProv,contPur,contProd,contPur_de,contCli,contSell,contSell_de)
                mod_emp.Save_Emp()
                mod_prov.Save_Prov()
                mod_prod.Save_Prod()
                mod_clie.Save_Clients()
                see_p.Save_Pur()
                see_pd.Save_Pur_De()
                see_sell.Save_Sells()
                see_sell_de.Save_Sell_D()
                break
            case _:
                print("Opción invalida")
    except ValueError:
        print("El tipo de dato ingresado no es valido")