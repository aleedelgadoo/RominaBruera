import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

# Usa la URI completa (la que termina en :5432/postgres)
DATABASE_URL = os.getenv('DATABASE_URL')

print("Intentando conectar...")
try:
    engine = create_engine(DATABASE_URL)
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("¡CONEXIÓN ESTABLECIDA EXITOSAMENTE!")
except Exception as e:
    print(f"ERROR: {e}")