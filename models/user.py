#!/usr/bin/python3
''' user module '''
from models.base_model import BaseModel


class User(BaseModel):
    '''
    initation of User that inherits BaseModel class
    Public Class Attributes:
    (string) email: initalized as a empty string
    (string) password: initalized as a empty string
    (string) first_name: initalized as a empty string
    (string) las_name: initalized as a empty string
    '''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
