import pandas as pd

# Cargar los datos desde el archivo CSV
data = pd.read_csv("data.csv")

# Mostrar los primeros 5 registros
print(data.head())
