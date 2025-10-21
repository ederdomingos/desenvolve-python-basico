# aula4_questao4.py
# Calcula o valor do frete conforme distância e peso

def calcular_frete(distancia_km: float, peso_kg: float) -> float:
    if distancia_km < 0 or peso_kg < 0:
        raise ValueError("Distância e peso devem ser valores não negativos.")
    # Determina tarifa por kg
    if distancia_km <= 100:
        tarifa = 1.0
    elif distancia_km <= 300:
        tarifa = 1.5
    else:
        tarifa = 2.0
    valor = tarifa * peso_kg
    # Acrescenta taxa para pacotes com peso superior a 10 kg
    if peso_kg > 10:
        valor += 10.0
    return valor

def main():
    try:
        distancia = float(input("Informe a distância da entrega em km: ").strip())
        peso = float(input("Informe o peso do pacote em kg: ").strip())
    except ValueError:
        print("Entrada inválida. Informe números válidos para distância e peso.")
        return

    try:
        valor_frete = calcular_frete(distancia, peso)
    except ValueError as e:
        print(e)
        return

    print(f"Valor do frete: R$ {valor_frete:.2f}")

if __name__ == "__main__":
    main()