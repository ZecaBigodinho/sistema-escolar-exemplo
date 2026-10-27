import os
import psycopg
from dotenv import load_dotenv

load_dotenv()


class AlunoDAO:
    def conectar(self):
        return psycopg.connect(os.getenv("DATABASE_URL"))

    def listar(self):
        with self.conectar() as conn:
            return conn.execute("SELECT id, nome FROM alunos ORDER BY nome").fetchall()
