import pytest

from src.api.json_schemes.main_schema import MainSchemes
from src.api.pydantic_model.main_models import (ListUsers,
                                                SingleUser,
                                                ListResource,
                                                SingleResource,
                                                Create,
                                                Update,
                                                RegisterSuccessful,
                                                Unsuccessful,
                                                Login
                                                )
from src.data.locators import MainPage
from src.data.req_methods import RequestMethods
from src.data.routes import APIRoutes
from helper.additional_methods import splitter


@pytest.mark.parametrize('send_request, locator, status_code, validate_json',
                         [pytest.param([RequestMethods.get, APIRoutes.list_users, ''],
                                       MainPage.list_users, 200, ListUsers),
                          pytest.param([RequestMethods.get, APIRoutes.single_user, ''],
                                       MainPage.single_user, 200, SingleUser),
                          pytest.param([RequestMethods.get, APIRoutes.single_user_not_found, ''],
                                       MainPage.single_user_not_found, 404, ''),
                          pytest.param([RequestMethods.get, APIRoutes.list_resource, ''],
                                       MainPage.list_resource, 200, ListResource),
                          pytest.param([RequestMethods.get, APIRoutes.single_resource, ''],
                                       MainPage.single_resource, 200, SingleResource),
                          pytest.param([RequestMethods.get, APIRoutes.single_resource_not_found, ''],
                                       MainPage.single_resource_not_found, 404, ''),
                          pytest.param([RequestMethods.post, APIRoutes.create, MainSchemes.create],
                                       MainPage.create, 201, Create),
                          pytest.param([RequestMethods.put, APIRoutes.single_user, MainSchemes.update],
                                       MainPage.put_update, 200, Update),
                          pytest.param([RequestMethods.patch, APIRoutes.single_user, MainSchemes.update],
                                       MainPage.patch_update, 200, Update),
                          pytest.param([RequestMethods.delete, APIRoutes.single_user, ''],
                                       MainPage.delete, 204, ''),
                          pytest.param([RequestMethods.post, APIRoutes.register, MainSchemes.register],
                                       MainPage.register, 200, RegisterSuccessful),
                          pytest.param([RequestMethods.post, APIRoutes.register, MainSchemes.register_unsuccessful],
                                       MainPage.register_unsuccessful, 400, Unsuccessful),
                          pytest.param([RequestMethods.post, APIRoutes.login, MainSchemes.login],
                                       MainPage.login, 200, Login),
                          pytest.param([RequestMethods.post, APIRoutes.login, MainSchemes.login_unsuccessful],
                                       MainPage.login_unsuccessful, 400, Unsuccessful),
                          pytest.param([RequestMethods.get, APIRoutes.delayed_response, ''],
                                       MainPage.delayed_response, 200, ListUsers)
                          ], indirect=['send_request'])
def test_main(send_request, instance_of_class, locator, status_code, validate_json):
    response_in_fixture = splitter(send_request.get_text())
    assert send_request.check_status_code(status_code)
    assert send_request.check_validate_json(validate_json)

    instance_of_class.click_by_data_id(locator)
    instance_of_class.wait_for_invisibility_element(MainPage.spinner)
    assert response_in_fixture == instance_of_class.get_text_in_response()
