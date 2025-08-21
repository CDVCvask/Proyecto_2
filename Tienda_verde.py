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
        print("1.Empleados")
        print("2.Proveedores")
        print("3.Clientes")
        print("4.Salir")
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
