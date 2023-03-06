from dataclasses import dataclass


@dataclass
class MainSchemes:
    create = {
        "name": "morpheus",
        "job": "leader"
    }
    update = {
        "name": "morpheus",
        "job": "zion resident"
    }
    register = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    register_unsuccessful = {
        "email": "eve.holt@reqres.in"
    }
    login = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    login_unsuccessful = {
        "email": "peter@klaven"
    }
