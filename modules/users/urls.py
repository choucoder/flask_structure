from .views import ListView, RegisterView, DetailsView, EditView

module_name = 'users'

routes = [
    ('/users', ListView.as_view('user_list')),
    ('/users/register', RegisterView.as_view('user_register')),
    ('/users/<int:id>', DetailsView.as_view('user_details')),
    ('/users/<int:id>/edit', EditView.as_view('user_edit')),
]

