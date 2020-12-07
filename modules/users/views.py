from flask.views import MethodView
from flask import render_template, abort, redirect, url_for, request
from modules.base.views import CustomView
from .forms import RegisterForm, UpdateForm


users = {
    1: {'id': 1, 'name': 'Adrian', 'surname': 'Troconis', 'password': '1813889'},
    2: {'id': 2, 'name': 'Jose', 'surname': 'Chourio', 'password': '110297'},
}


class ListView(CustomView):
    template_name = 'users/index.html'

    def get(self):
        all_users = users.values()
        context = {'users': all_users, 'name': 'List users'}
        return self.render_template(context)


class RegisterView(CustomView):
    template_name = 'users/register.html'

    def get(self):
        context = {'name': 'Register user'}
        return self.render_template(context)

    def post(self):
        form = RegisterForm()
        form = form.parse_args(strict=True)

        id = max(users.keys()) + 1
        users[id] = form
        users[id]['id'] = id

        return redirect(url_for('user_list'))


class EditView(CustomView):
    template_name = 'users/edit.html'

    def get(self, id):
        context = {'name': 'Edit user'}
        context['user'] = users[id]
        return self.render_template(context)

    def post(self, id):
        form = UpdateForm()
        form = form.parse_args(strict=True)
        form['id'] = id
        users[id] = form
        return redirect(url_for('user_list'))


class DetailsView(CustomView):

    template_name = 'users/details.html'

    def get(self, id):
        context = {'name': 'User details'}
        context['user'] = users[id]
        return self.render_template(context)