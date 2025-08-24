class Menu:
    def Main_Menu(self):
        print("Bienvenido a la tienda verde")
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
    def Check(self):
        if len(self.categorys) == 0:
            return False
        else:
            return True
    def Show_Cat(self):
        count = 1
        for code, value in self.categorys.items():
            print(f"Categoria {count}")
            print(f"Nombre: {value['Nombre']} - Código: {code}")
menus = Menu()
contC = 0
mod_c = Mod_Category()
while 0 != 1:
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
                    for i in range(num):
                        cat_code = f"P{contC}"
                        while 0 != 1:
                            print(f"Ingreso de la categoría {count}")
                            name = input("Ingrese el nombre de la categoria")
                            if name == "":
                                print("No puede dejar este espacio en blanco")
                            else:
                                break
                        cat = Category(cat_code, name)
                        count = count + 1
                        contC = contC + 1
                        mod_c.Add_Cat(cat)
                case "2":
                    pass
                case "3":
                    pass
                case "4":
                    pass
                case "5":
                    pass
                case _:
                    print("La opción seleccionada no es valida")
        case "2":
            pass
        case "3":
            pass
        case "4":
            menus.Inv_Menu()
            opt1 = input("Seleccione que parte del inventario desea ver: ")
            match opt1:
                case "1":
                    pass
                case "2":
                    empty = mod_c.Check()
                    if empty == False:
                        print("No hay ninguna categoría que mostrar")
                    else:
                        mod_c.Show_Cat()
                case "3":
                    pass
                case _:
                    print("La opción selecionada no es valida")
        case "5":
            pass
        case "6":
            pass
        case "7":
            pass
        case "8":
            pass
        case _:
            print("Opción invalida")
