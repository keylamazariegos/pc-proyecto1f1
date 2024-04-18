#menu principal 
cantidaddetanquere = 40
canttanquesup = 40
canttanqued = 40
resultadoregular = 0
resultadodiesel = 0
resultadosuper = 0
cant_quetzales = 0 
cant_quetzales = 0
totald = 0 
totalv = 0
totaln = 0
while True : 
    print ("¿Dónde desea navegar?")
    print ("1.Gestionar inventario")
    print ("2.Venta de combustible.")
    print ("3.Gestión de Turnos")
    print ("4.Reporte de Rentabilidad")
    print ("5.Salida")

    opcionselec= int(input ("Ingrese la opción: "))

    #Gestionar inventario 
    if opcionselec == 1:
    #submenu opición gestionar inventario
        print ("Opciones:")
        print ("1. Agregar combustible.")
        print ("2. No deseo agregar combustible")
        #agregar combustible 
        opcion = int(input ("Ingrese la opción deseada: "))
        if opcion == 1: 
            print ("Actualmente tiene", cantidaddetanquere, "galones de REGULAR")
            print ("Actualmente tiene", canttanquesup,  "galones de SUPER")
            print ("Actualmente tiene", canttanqued, "galones de DIESEL")
            print ("NOTA: La capacidad máxima es de 80 galones por depósito.")
            galre= int (input ("Ingrese la cantidad (en galones) que desea agregar de Regular: "))
            cantidaddetanquere= 40+ galre
    
            if cantidaddetanquere <= 80: 
                print (cantidaddetanquere, "galones de gasolina REGULAR, ahora")
                galsup= int (input ("Ingrese la cantidad (en galones) que desea agregar de SUPER: "))    
            else: 
                print ("Operación inválida, superó la capacidad máxima")
                galsup= int (input ("Ingrese la cantidad (en galones) que desea agregar de SUPER: "))       
                canttanquesup= 40+ galsup
            if  galsup <= 40:   
                canttanquesup= 40+ galsup
                print ("La cantidad del tanque SUPER es: ", canttanquesup)
                gald= int (input ("Ingrese la cantidad (en galones) que desea agregar de DIESEL: "))
            else: 
                print ("Operación inválida, superó la capacidad máxima de tanque SUPER")
                gald= int (input ("Ingrese la cantidad (en galones) que desea agregar de DIESEL: "))

            if gald <= 40:   
                canttanqued= 40 + gald
                print ("La cantidad de este tanque ahora es: ", canttanqued, "galones")
            else: 
                print ("Operación inválida, superó la capacidad máxima de tanque DIESEL")
        else: 
            print ("Vuelva pronto")

        #Venta de combustible 
    if opcionselec == 2: 
            precioregular = 29.00
            preciosuper = 30.00
            preciodiesel = 26.50
            print("1.Regular")
            print ("Tenemos disponibles" , (cantidaddetanquere) ,  "galones de regular")
            print("Un galón de combustible tipo regular tiene costo de: 29.00")
            print("2.Super")
            print ("Tenemos disponibles" , (canttanquesup) , "galones de super")
            print("Un galón de combustible tipo super tiene costo de:30.00" )
            print("3.Diesel")
            print ("Tenemos disponibles" , (canttanqued) , "galones de diesel")
            print("Un galón de combustible tipo diesel tiene costo de: 26.50")
            seleccion = int(input("Seleccione el tipo de combustible:"))
            while seleccion == 1:
                    if cantidaddetanquere > 5:
                        print ("1.Cantidad de Galones")
                        print ("2.Quetzales equivalentes a N galones")
                        metodo = int(input("Seleccione su método de compra: "))
                        if metodo == 1:
                            cant_regular = int(input("Seleccione la cantidad de galones que desea adquirir: "))
                            cantidaddetanquere = cantidaddetanquere - cant_regular 
                            resultadoregular = cant_regular * precioregular
                            print ("Su compra se ha realizado con éxito, el total a pagar es de: ", resultadoregular)
                            nombre = input ("Ingrese su nombre completo: ")
                            nonit = int(input("Ingrese su número de NIT: "))
                            bomba = int(input("Ingrese el número de bomba: "))
                            print ("    Factura     ")
                            print ("Nombre: ", nombre)
                            print ("Número de NIT: ", nonit)
                            print ("Número de bomba: ", bomba )
                            print ("Su consumo fue de: ", resultadoregular)
                        else: 
                            cant_quetzales = int(input("Ingrese la cantidad de quetzales a pagar:"))
                            resultadoregular = cant_quetzales / precioregular
                            print ("Estará adquiriendo", resultadoregular , "galones")
                            cantidaddetanquere = cantidaddetanquere - resultadoregular
                            nombre = input("Ingrese su nombre completo: ")
                            nonit = int(input("Ingrese su número de NIT: "))
                            bomba = int(input("Ingrese el número de bomba: "))
                            print ("    Factura     ")
                            print ("Nombre: ", nombre)
                            print ("Número de NIT: ", nonit)
                            print ("Número de bomba: ", bomba )
                            print ("Su consumo fue de: ", resultadoregular)

                            
                        break
                    else:
                        print ("No se puede proceder a la compra")

            while seleccion == 2:
                    if canttanquesup > 5:
                        print ("1.Cantidad de Galones")
                        print ("2.Quetzales equivalentes a N galones")
                        metodo = int(input("Seleccione su método de compra: "))
                        if metodo == 1:
                            cant_super = int(input("Seleccione la cantidad de galones que desea adquirir: "))
                            canttanquesup = canttanquesup - cant_super
                            resultadosuper = cant_super * preciosuper
                            print ("Su compra se ha realizado con éxito, el total a pagar es de: ", resultadosuper)
                            nombre = input("Ingrese su nombre completo: ")
                            nit = int(input("Ingrese su número de NIT: "))
                            bomba = int(input ("Ingrese el número de bomba: "))
                            print ("       Factura      ")
                            print ("Nombre: ", nombre)
                            print ("Número de NIT: ", nit)
                            print ("Número de bomba: ", bomba )
                            print ("Total: ", resultadosuper)
                            
                        else: 
                            cant_quetzales = int(input("Ingrese la cantidad de quetzales a pagar:"))
                            resultadosuper = cant_quetzales / preciosuper
                            print ("Estará adquiriendo", resultadosuper , "galones")
                            canttanquesup = canttanquesup - resultadosuper
                            print ("Por favor ingrese los siguientes datos para su factura")
                            nombre = input ("Ingrese su nombre completo: ")
                            nonit = int(input("Ingrese su número de NIT: "))
                            bomba = int(input("Ingrese el número de bomba: "))
                            print ("       Factura      ")
                            print ("Nombre: ", nombre)
                            print ("Número de NIT: ", nonit)
                            print ("Número de bomba: ", bomba )
                            print ("Total: ", cant_quetzales)
                        break
                    else:
                        print ("No se puede proceder a la compra")
                    break

            while seleccion == 3:
                    if canttanqued > 5:
                        print ("1.Cantidad de Galones")
                        print ("2.Quetzales equivalentes a N galones")
                        metodo = int(input("Seleccione su método de compra: "))
                        if metodo == 1:
                            cant_diesel = int(input("Seleccione la cantidad de galones que desea adquirir: "))
                            canttanqued = canttanqued - cant_diesel
                            resultadodiesel = cant_diesel * preciodiesel
                            print ("Su compra se ha realizado con éxito, el total a pagar es de: ", resultadosuper)
                            print ("Por favor ingrese los siguientes datos para su factura")
                            nombre = input ("Ingrese su nombre completo: ")
                            nonit = int(input("Ingrese su número de NIT: "))
                            bomba = int(print ("Ingrese el número de bomba: "))
                            print ("    Factura     ")
                            print ("Nombre: ", nombre)
                            print ("Número de NIT: ", nonit)
                            print ("Número de bomba: ", bomba )
                            print ("Su consumo fue de: ", resultadodiesel)
                        else: 
                            cant_quetzales = int(input("Ingrese la cantidad de quetzales a pagar:"))
                            resultadodiesel = cant_quetzales / preciodiesel
                            print ("Estará adquiriendo", resultadodiesel , "galones")
                            canttanqued = canttanqued - resultadodiesel
                            nombre = input ("Ingrese su nombre completo: ")
                            nonit = int(input("Ingrese su número de NIT: "))
                            bomba = int(input ("Ingrese el número de bomba: "))
                            print ("    Factura     ")
                            print ("Nombre: ", nombre)
                            print ("Número de NIT: ", nonit)
                            print ("Número de bomba: ", bomba )
                            print ("Total: ", cant_quetzales)
                        break
                    else:
                            print ("No se puede proceder a la compra")
                    break
            
        #Gestión de Turnos
    if opcionselec == 3: 
        #trabajadores iniciales
            jordiurna = 1
            jorvespertina = 1
            jornocturna = 1

            #se mostrará el total de trabajadores para evaluar si se añade o retira algún trabajador
            print ("Hay un total de:", jordiurna, "en el turno diurno")
            print ("Hay un total de:", jorvespertina, "en el turno vespertino")
            print ("Hay un total de:", jornocturna, "en el turno nocturna")
            print ("¿Desea agregar o extraer personas a la estación de servicio")
            print ("1.Agregar")
            print ("2.Extraer")
            print ("3.Ninguna")

            seleccion = int(input("Seleccione la opción que desea: "))

            #AGREGAR PERSONAL
            while seleccion == 1:
                print("1.Jornada diurna")
                print("12:00 a.m. - 8:00 a.m.")
                print("Q14.00 quetzales por hora")
                print("2.Jornada vespertina")
                print ("8:00 a.m. - 4:00 p.m.")
                print ("Q14.50 quetzales por hora")
                print("3.Jornada nocturna")
                print ("4:00 p.m. - 12 a.m.")
                print ("Q15.50 quetzales por hora")
                segseleccion = int(input("Seleccione la jornada en la que desea agregar personal: "))
                if segseleccion == 1:
                    agd = int(input("Ingrese la cantidad de personas a agregar: "))
                    totald = (agd) + (jordiurna)
                    print ("La cantidad de trabajadores para esta jornada es de: ", totald)
                if segseleccion == 2:
                    agv = int(input("Ingrese la cantidad de personas a agregar: "))
                    totalv = (agv) + (jorvespertina)
                    print ("La cantidad de trabajadores para esta jornada es de: ", totalv)
                if segseleccion == 3:
                    agn= int(input("Ingrese la cantidad de personas a agregar: "))
                    totaln = (agn) + (jornocturna)
                    print ("La cantidad de trabajadores para esta jornada es de: ", totaln)

            #EXTRAER PERSONAL
            while seleccion == 2:
                print("1.Jornada diurna")
                print("12:00 a.m. - 8:00 a.m.")
                print("Q14.00 quetzales por hora")
                print("2.Jornada vespertina")
                print ("8:00 a.m. - 4:00 p.m.")
                print ("Q14.50 quetzales por hora")
                print("3.Jornada nocturna")
                print ("4:00 p.m. - 12 a.m.")
                print ("Q15.50 quetzales por hora")
                segseleccion = int(input("Ingrese la jornada en la que desea extraer personal: "))
                if segseleccion == 1:
                    exd = int(input("Ingrese la cantidad de personas a extraer: "))
                    totald = (exd) - (jordiurna)
                    if totald < 1:
                        print("No se puede realizar la siguiente acción, debe haber mínimo un trabajador en este turno")
                    else:
                        print ("La cantidad de trabajadores para esta jornada es de: ", totald)
                if segseleccion == 2:
                    exv = int(input("Ingrese la cantidad de personas a extraer: "))
                    totalv = (exv) - (jorvespertina)
                    if totalv < 1:
                        print("No se puede realizar la siguiente acción, debe haber mínimo un trabajador en este turno")
                    else:
                        print ("La cantidad de trabajadores para esta jornada es de: ", totalv)
                if segseleccion == 3:
                    exn= int(input("Ingrese la cantidad de personas a extraer: "))
                    totaln = (exn) - (jornocturna)
                    if totaln < 1:
                        print("No se puede realizar la siguiente acción, debe haber mínimo un trabajador en este turno")
                    else:
                        print ("La cantidad de trabajadores para esta jornada es de: ", totalv)
                break
            #NINGUNA
            while seleccion == 3:
                print ("Vuelva Pronto") 

    #Salida
    if opcionselec == 4:
            #declarar las variables de operaciones finales
        ingreso_total= resultadoregular + resultadosuper + canttanqued + cant_quetzales     
        materiaprimareg= cantidaddetanquere * 7 
        materiaprimasup= 8 * canttanquesup 
        materiaprimadiesel= canttanqued*6
        mateprimatotal= materiaprimareg + materiaprimadiesel
          #mano de obra
        obrad= 14*totald
        obrav= 14.50*totalv
        obran= 15.50*totaln
        mano_de_obra = obrad + obrav + obran
        ubruta= ingreso_total - mateprimatotal - mano_de_obra - 10.00

        print ("ingresos totales                    Q",ingreso_total)
        print ("Materia prima:")
        print ("        Costo combustible REGULAR:  Q", materiaprimareg)
        print ("        Costo combustible SUPER:    Q", materiaprimasup)
        print ("        Costo combustible DIESEL:   Q", materiaprimadiesel)

        print ("Mano de obra:")
        print ("        Salario Jornada Diurna:     Q", materiaprimareg)
        print ("        Salario Jornada Vespertina: Q", materiaprimasup)
        print ("        Salario Jornada Nocturna:   Q", materiaprimadiesel)

        print ("Costos Fijos:                       Q10.00")
        print ("Utilidad Bruta:                     Q",ubruta)

    
        #Salida
    if opcionselec == 5:
            print("Vuelva Pronto")