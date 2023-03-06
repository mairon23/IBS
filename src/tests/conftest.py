import pytest
import requests
from selenium import webdriver

from src.api.api_methods.api_base import Responses
from src.data.routes import Routes
from helper.additional_methods import merge_link
from src.pages.main import Main


@pytest.fixture
def driver():
    """
    Инициализация драйвера.
    """
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get(Routes.main_page)
    yield driver
    driver.quit()


@pytest.fixture
def instance_of_class(driver):
    """
    Создание экземпляра классов.
    """
    return Main(driver)


@pytest.fixture
def send_request(request):
    """
    Отправка запроса.
    """
    req_method = request.param[0]
    url = merge_link(request.param[1])
    json = request.param[2]
    return Responses(requests.request(method=req_method, url=url, json=json))
