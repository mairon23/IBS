from dataclasses import dataclass


@dataclass
class RequestMethods:
    get: str = 'get'
    post: str = 'post'
    put: str = 'put'
    delete: str = 'delete'
    patch: str = 'patch'
