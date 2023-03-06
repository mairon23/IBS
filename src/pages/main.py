from helper.additional_methods import splitter
from src.pages.layers import WorkWithElement


class Main(WorkWithElement):
    def get_text_in_response(self) -> str:
        """
        Метод, который получает текст ответа запроса на frontend.
        """
        return splitter(self.get_element_by_data_key('output-response').text)
