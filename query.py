from database import Database

class Queries:
    def __init__(self, db):
        self.db = db

    # Questão 1
    def query1_a(self):
        query = "MATCH (t:Teacher {name: 'Renzo'}) RETURN t.ano_nasc AS ano_nasc, t.cpf AS cpf"
        return self.db.execute_query(query)

    def query1_b(self):
        query = "MATCH (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name AS name, t.cpf AS cpf"
        return self.db.execute_query(query)

    def query1_c(self):
        query = "MATCH (c:City) RETURN c.name AS city_name"
        return self.db.execute_query(query)

    def query1_d(self):
        query = """
        MATCH (s:School)
        WHERE s.number >= 150 AND s.number <= 550
        RETURN s.name AS school_name, s.address AS address, s.number AS number
        """
        return self.db.execute_query(query)

    # Questão 2
    def query2_a(self):
        query = """
        MATCH (t:Teacher)
        RETURN max(t.ano_nasc) AS ano_nasc_mais_jovem, min(t.ano_nasc) AS ano_nasc_mais_velho
        """
        return self.db.execute_query(query)

    def query2_b(self):
        query = "MATCH (c:City) RETURN avg(c.population) AS media_populacao"
        return self.db.execute_query(query)

    def query2_c(self):
        query = """
        MATCH (c:City {cep: '37540-000'})
        RETURN replace(c.name, 'a', 'A') AS city_name_replaced
        """
        return self.db.execute_query(query)

    def query2_d(self):
        query = """
        MATCH (t:Teacher)
        RETURN substring(t.name, 2, 1) AS char_from_name
        """
        return self.db.execute_query(query)
