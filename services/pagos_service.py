from datetime import datetime
from models.pagos import Pagos
from models.ventas import Ventas
from db import db

def registrar_pago(data):
    ventas_num = data.get('VentasNum')
    monto = float(data.get('Monto'))
    concepto = data.get('Concepto')
    porc_cobro = data.get('PorcCobro')
    poc_interes = data.get('pocInteres')
    forma_pago_cod = data.get('FomaPagCod')

    # Validaciones básicas
    if not ventas_num or not monto or not forma_pago_cod:
        raise ValueError("Faltan campos obligatorios.")

    venta = Ventas.query.get(ventas_num)
    if not venta:
        raise ValueError("La venta no existe.")

    if monto > venta.Saldo:
        raise ValueError("El monto excede el saldo actual de la venta.")

    # Calcular nuevo saldo
    nuevo_saldo = round(venta.Saldo - monto, 2)

    # Crear pago
    nuevo_pago = Pagos(
        PorcCobro=porc_cobro,
        pocInteres=poc_interes,
        Concepto=concepto,
        Monto=monto,
        Fecha=datetime.now(),
        Saldo=nuevo_saldo,
        VentasNum=ventas_num,
        FomaPagCod=forma_pago_cod
    )

    # Actualizar saldo de la venta
    venta.Saldo = nuevo_saldo

    # Guardar en base de datos
    db.session.add(nuevo_pago)
    db.session.commit()

    return nuevo_pago
