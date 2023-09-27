price_ht = float(input("Entrerez le prix hors taxe:"))
quantity = int(input("Entrerez la quantité d'articles:"))
tva = float(input("Entrerez le TVA en nombre décimal:"))
priceTTC = price_ht * quantity * (1 + tva)

print(f"le prix TTC est {priceTTC} euros.")
