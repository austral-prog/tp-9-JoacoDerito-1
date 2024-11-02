def create_inventory(lista):
	inventory={}
	for items in lista:
		if items in inventory:
			inventory[items]+=1
		else:
			inventory[items]=1
	return inventory

def add_items(inventario, lista):
	for items in lista:
		if items in inventario:
			inventario[items]+=1
		else:
			inventario[items]=1
	return inventario

def decrement_items(inventory, lista):
	for items in lista:
		if items in inventory:
			if inventory[items]>0:
				inventory[items]-=1
		else:
			inventory[items]=0
	return inventory

def remove_item(inventario, articulo):
	for items in inventario:
		if articulo in inventario:
			del inventario[articulo]
		return inventario

def list_inventory(inventario):
	lista=[]
	for clave, valor in inventario.items():
		if inventario[clave]>0:
			tupla=clave, valor
			lista.append(tupla)
	return lista
