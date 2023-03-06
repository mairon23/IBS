from dataclasses import dataclass


@dataclass
class MainPage:
    list_users: str = 'users'
    single_user: str = 'users-single'
    single_user_not_found: str = 'users-single-not-found'
    list_resource: str = 'unknown'
    single_resource: str = 'unknown-single'
    single_resource_not_found: str = 'unknown-single-not-found'
    create: str = 'post'
    put_update: str = 'put'
    patch_update: str = 'patch'
    delete: str = 'delete'
    register: str = 'register-successful'
    register_unsuccessful: str = 'register-unsuccessful'
    login: str = 'login-successful'
    login_unsuccessful: str = 'login-unsuccessful'
    delayed_response: str = 'delay'
    spinner: str = 'spinner'
