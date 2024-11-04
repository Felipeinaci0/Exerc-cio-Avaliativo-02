from database import Database
from query import Queries
from teacher_crud import TeacherCRUD

db = Database("bolt://44.200.219.219:7687", "neo4j", "squeaks-drums-leakage")
db.drop_all()

queries = Queries(db)
teacher_crud = TeacherCRUD(db)

# Questão 1
print("Questão 1) a:", queries.query1_a())
print("Questão 1) b:", queries.query1_b())
print("Questão 1) c:", queries.query1_c())
print("Questão 1) d:", queries.query1_d())

# Questão 2
print("Questão 2) a:", queries.query2_a())
print("Questão 2) b:", queries.query2_b())
print("Questão 2) c:", queries.query2_c())
print("Questão 2) d:", queries.query2_d())

# Questão 3:

# a. Criando um novo professor
teacher_crud.create("Chris Lima", 1956, "189.052.396-66")

# b. Consultando o professor "Chris Lima"
print("Professor Chris Lima:", teacher_crud.read("Chris Lima"))

# c. Atualizando o CPF do professor "Chris Lima"
teacher_crud.update("Chris Lima", "162.052.777-77")
print("Chris Lima após atualização de CPF:", teacher_crud.read("Chris Lima"))

# d. Deletando o professor "Chris Lima"
teacher_crud.delete("Chris Lima")
print("Chris Lima após deleção:", teacher_crud.read("Chris Lima"))

db.close()
