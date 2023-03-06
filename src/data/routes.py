from dataclasses import dataclass


@dataclass
class Routes:
    main_page: str = 'https://reqres.in/'
    api_main_page: str = 'https://reqres.in/api/'


@dataclass
class APIRoutes:
    list_users: str = 'users?page=2'
    single_user: str = 'users/2'
    single_user_not_found: str = 'users/23'
    list_resource: str = 'unknown'
    single_resource: str = 'unknown/2'
    single_resource_not_found: str = 'unknown/23'
    create: str = 'users'
    register: str = 'register'
    login: str = 'login'
    delayed_response: str = 'users?delay=3'

