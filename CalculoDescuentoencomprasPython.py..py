def calcular_descuento(monto_total, porcentaje_descuento=10):
    """Calcula el descuento y el monto final a pagar."""
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

def main():
    # Primera compra
    monto_compra_1 = 1500
    descuento_1 = calcular_descuento(monto_compra_1)
    total_a_pagar_1 = monto_compra_1 - descuento_1

    print(f"Monto total de la compra: ${monto_compra_1:.2f}")
    print(f"Descuento aplicado (10%): ${descuento_1:.2f}")
    print(f"Monto final a pagar: ${total_a_pagar_1:.2f}\n")

    # Segunda compra con un porcentaje de descuento diferente
    monto_compra_2 = 2000
    porcentaje_descuento_2 = 15  # Porcentaje de descuento específico
    descuento_2 = calcular_descuento(monto_compra_2, porcentaje_descuento_2)
    total_a_pagar_2 = monto_compra_2 - descuento_2

    print(f"Monto total de la compra: ${monto_compra_2:.2f}")
    print(f"Descuento aplicado (15%): ${descuento_2:.2f}")
    print(f"Monto final a pagar: ${total_a_pagar_2:.2f}")

if __name__ == "__main__":
    main()