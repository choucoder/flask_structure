from flask_restful import reqparse

class RegisterForm(reqparse.RequestParser):
    """Formulario de validacion para la creacion de un usuario
    """
    def __init__(self):
        super().__init__()
        self.add_argument('name', type=str, required=True)
        self.add_argument('surname', type=str, required=True)
        self.add_argument('password', type=str, required=True)
        self.add_argument('create', type=str, required=True)


class UpdateForm(reqparse.RequestParser):
    """Formulario de validacion para la creacion de un usuario
    """
    def __init__(self):
        super().__init__()
        self.add_argument('name', type=str, required=True)
        self.add_argument('surname', type=str, required=True)
        self.add_argument('password', type=str, required=True)
        self.add_argument('update', type=str, required=True)