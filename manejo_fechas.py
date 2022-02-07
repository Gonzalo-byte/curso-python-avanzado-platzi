from datetime import datetime

ahora = datetime.now()

print(f"fecha: {ahora}")
print(f"fecha formateada: {ahora.strftime('%d/%m/%Y')}")
print(f"día: {ahora.strftime('%d')}")
print(f"mes: {ahora.strftime('%m')}")
print(f"año: {ahora.strftime('%Y')}")