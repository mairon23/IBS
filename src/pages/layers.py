from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.pages.base import BasePageObject


class WorkWithElement(BasePageObject):
    """
    Класс, представляющий методы работы с веб-элементами.
    """
    data_key = "//*[@data-key='{}']"

    def get_element_by_data_id(self, text: str) -> WebElement:
        """
        Метод, который возвращает WebElement, у которого есть data-id
        :param text: Значение data-id
        """
        data_id = "//*[@data-id='{}']"
        return self.wait_located((By.XPATH, data_id.format(text)))

    def get_element_by_data_key(self, text: str) -> WebElement:
        """
        Метод, который возвращает WebElement, у которого есть data-key
        :param text: Значение data-key
        """
        return self.wait_located((By.XPATH, self.data_key.format(text)))

    def click_by_data_id(self, text: str) -> None:
        """
        Метод, который кликает по элементу, у которого есть data-id
        :param text: Значение data-id
        """
        self.get_element_by_data_id(text).click()

    @staticmethod
    def get_text(element: WebElement) -> str:
        """
        Метод, который возвращает текст из элемента.
        :param element: WebElement
        """
        return element.text

    def wait_for_invisibility_element(self, text: str):
        """
        Метод, который ожидает исчезновения элемента.
        :param text: Значение data-key
        """
        self.check_invisibility_element((By.XPATH, self.data_key.format(text)))
