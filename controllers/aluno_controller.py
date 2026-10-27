from database.aluno_dao import AlunoDAO


class AlunoController:
    def __init__(self):
        self.dao = AlunoDAO()

    def listar(self):
        return self.dao.listar()
