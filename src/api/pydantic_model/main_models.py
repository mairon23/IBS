from typing import List

from pydantic import BaseModel


class ListUserData(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


class ListSupport(BaseModel):
    url: str
    text: str


class ListResourceData(BaseModel):
    id: int
    name: str
    year: int
    color: str
    pantone_value: str


class ListUsers(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[ListUserData]
    support: ListSupport


class SingleUser(BaseModel):
    data: ListUserData
    support: ListSupport


class ListResource(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: ListResourceData
    support: ListSupport


class SingleResource(BaseModel):
    data: ListResourceData
    support: ListSupport


class Create(BaseModel):
    name: str
    job: str
    id: str
    createdAt: str


class Update(BaseModel):
    name: str
    job: str
    updatedAt: str


class RegisterSuccessful(BaseModel):
    id: int
    token: str


class Unsuccessful(BaseModel):
    error: str


class Login(BaseModel):
    token: str
