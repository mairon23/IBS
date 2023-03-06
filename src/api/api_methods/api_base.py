class Responses:
    def __init__(self, response):
        self.response = response
        self.response_status = response.status_code
        self.response_json = response.json()

    def check_status_code(self, status_code: int) -> bool:
        """Метод проверки статус кода"""
        return self.response_status == status_code

    def validate_json_schemas(self, schema):
        """Метод для валидации json"""
        return schema.parse_obj(self.response_json)

    def get_text(self) -> str:
        """Метод для получения данных в виде текста"""
        response = self.response.text
        return response

    def check_validate_json(self, schema):
        """
        Метод для проверки валидации response
        :param schema: Схема json
        """
        if schema:
            return self.validate_json_schemas(schema)
        return False
