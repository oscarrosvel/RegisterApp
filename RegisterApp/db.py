import os
import psycopg2
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

# Usa la misma cadena de conexión que definiste para SQLAlchemy
dsn = os.getenv("SQLALCHEMY_DATABASE_URI")
if dsn and dsn.startswith("postgresql+psycopg2"):
    dsn = dsn.replace("postgresql+psycopg2", "postgresql")

def get_conn():
    """
    Retorna una conexión psycopg2 a la base de datos PostgreSQL.
    Uso:
        with get_conn() as conn, conn.cursor() as cur:
            cur.execute("SELECT 1")
    """
    return psycopg2.connect(dsn)
