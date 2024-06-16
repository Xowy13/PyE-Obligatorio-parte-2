import numpy as np

X_train = np.array([[0, 0], [0, 1], [1, 0], [1, 1], [0, 0], [0, 1],
[1, 0], [1, 1]])

y_train = np.array([0, 1, 0, 1, 0, 1, 0, 1])

compra = np.sum(y_train == 1)/len(y_train)
no_compra = 1-compra

edad_mayor = np.sum(X_train[:,0] == 1)/len(X_train)
edad_menor = 1-edad_mayor

edad_mayor_compra = np.sum((X_train[:,0] == 1) & (y_train == 1))/np.sum(y_train == 1)
edad_mayor_no_compra = np.sum((X_train[:, 0] == 1) & (y_train == 0))/np.sum(y_train == 0)

ingreso_mayor = np.sum(X_train[:,1] == 1)/len(X_train)
ingreso_menor = 1-ingreso_mayor

ingreso_mayor_compra = np.sum((X_train[:,1] == 1) & (y_train == 1))/np.sum(y_train == 1)
ingreso_mayor_no_compra = np.sum((X_train[:,1] == 1) & (y_train == 0))/np.sum(y_train == 0)

nueva_instancia = np.array([1, 1])

pcompra_instancia = edad_mayor_compra * ingreso_mayor_compra * compra
pno_compra_instancia = edad_mayor_no_compra * ingreso_mayor_no_compra * no_compra

pcompra_instancia_real = pcompra_instancia/(pcompra_instancia + pno_compra_instancia)

print(pcompra_instancia_real)
