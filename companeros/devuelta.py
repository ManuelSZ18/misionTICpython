#calcular las vueltas
valorcompra = int(input("Señor, El articulo vale: "))
pagocompra = int(input("Gracias señor, yo le pago con un billete de: "))

if valorcompra <= pagocompra:
    if valorcompra < pagocompra:
        vueltas = pagocompra - valorcompra;
        print("Señor, sus vueltas son {}: ".format(vueltas)); 
    else:
        print('No tiene vueltas.')
else:
    print("Señor, no le alcanza para pagar la compra, lo siento")