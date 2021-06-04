totalCompra = 75450
print('El total de la compra es: ${}'.format(totalCompra))
pagoCompra = int(input('Por favor ingrese el dinero para realizar el pago: '))
if pagoCompra < totalCompra:
    print('El pago proporcionado es insuficiente, por favor proporcione el faltante: ${}'.format(totalCompra - pagoCompra))
elif pagoCompra == totalCompra:
    print('El pago proporcionado es exacto al total de la compra, no tiene vuelta! Gracias por su compra!')
else:
    print('Se proceso el pago y su vuelta es de: ${}'.format(pagoCompra - totalCompra))