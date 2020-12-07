from pathlib import Path
from typing import List, Tuple
from flask import app, Flask
from flask.views import View

class MyApp(Flask):
    
    APP_DIR = Path(__file__).resolve().parent.parent
    template_folder = f"{APP_DIR}/templates"
    static_folder = f"{APP_DIR}/static"

    def __init__(self):
        super().__init__(__name__,
                        template_folder=self.template_folder,
                        static_folder=self.static_folder)
    
    def add_resources(self, resources: List[Tuple[str, View]]):
        for url, view in resources:
            print(url, view)
            self.add_url_rule(url, view_func=view)