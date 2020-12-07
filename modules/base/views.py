from flask.views import MethodView
from flask import render_template


class CustomView(MethodView):
    template_name = ''

    def render_template(self, context):
        return render_template(self.template_name, **context)