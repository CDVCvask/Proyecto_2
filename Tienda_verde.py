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
    def __init__(self,ID_SD,Quantity,Product,Price,SubTotal):
        self.ID_SD = ID_SD
        self.Quantity = Quantity
        self.Product = Product
        self.Price = Price
        self.SubTotal = SubTotal
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
    def Add_Sup(self,sup):
        self.suppliers[sup.ID_Sup] = {'Nombre': sup.Name,'Empresa': sup.Company,'Telefno':sup.Phone,
                                      'Dirección': sup.Adress,'Correo':sup.Mail,'Categoria':sup.Category}
    def Show_Sup(self):
        count = 1
        for code, value in self.suppliers.items():
            cat = mod_c.Cat_Name(value['Categoria'])
            print(f"Proveedor {count}")
            print(f"Código {code}, Nombre: {value['Nombre']}, Empresa: {value['Empresa']}")
            print(f"Telefno: {value['Telefno']}, Dirección: {value['Dirección']}, Correo: {value['Correo']}")
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
    def Add_Product(self,product):
        self.products[product.ID_Pro] = {'Nombre': product.Name,'Categoría':product.Category,'Precio':product.Price,
                                        'Stock':product.Stock}
class See_Purchase:
    def __init__(self):
        self.purchases = {}
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
    def Add_Pur_De(self,pur):
        self.purchase_Details[pur.ID_PD] = {'Codigo compra':pur.Purchase,'Cantidad': pur.Quantity, 'Producto':pur.Product,
                                            'Precio': pur.P_Price,'SubTotal': pur.SubTotal, 'Caducidad': pur.Expiration}
    def Show_Pur_De(self,code):
        count = 1
        for key,value in self.purchase_Details.items():
            if code == key:
                print(f"Producto: {count}")
                print(f"Producto: {value['Producto']}, Precio: {value['Precio']} X Cantidad: {value['Cantidad']}"
                      f" = SubTotal: {value['SubTotal']}")
                print(" ")
                count = count + 1
menus = Menu()
contC = 0
contE = 0
contProv = 0
contPur = 0
contProd = 0
contPur_de = 0
mod_c = Mod_Category()
mod_prov = Mod_Supplier()
mod_emp = Mod_Employee()
mod_prod = Mod_Product()
see_p = See_Purchase()
see_pd = See_Purchase_Details()
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
                        pass
                    case "5":
                        pass
                    case _:
                        print("La opción seleccionada no es valida")
            case "2":
                first = True
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
                                        time = datetime.datetime.now()
                                        for i in range(num):
                                            code_prod = f"Prod{contProd}"
                                            code_pur_de = f"PurDe{contPurDe}"
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
                                                                    pur_de = Purchase_Details(contPur_de,code_pur,quantity,
                                                                                              code_prod,p_price,sub_total,
                                                                                              expiration)
                                                                    contPur_de += 1
                                        contPur = contPur + 1
                                        purchase = Purchase(code_pur,time,supplier,employee,total)
                        else:
                            menus.Pur_Menu()
            case "3":
                pass
            case "4":
                menus.Inv_Menu()
                opt1 = input("Seleccione que parte del inventario desea ver: ")
                match opt1:
                    case "1":
                        pass
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
                opt1 = input("Seleccione que parte del inventario desea ver: ")
                match opt1:
                    case "1":
                        empty = see_p.Check_Pur()
                        if empty == False:
                            print("No hay ninguna compra que mostrar")
                        else:
                            see_p.Show_Pur()
                    case "2":
                        pass
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
                        pass
                    case "4":
                        pass
                    case "5":
                        pass
                    case _:
                        print("Opción ingresada no valida")
            case "7":
                pass
            case "8":
                print("Gracias por utilizar el programa")
                break
            case _:
                print("Opción invalida")
    except ValueError:
        print("El tipo de dato ingresado no es valido")