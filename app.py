from flask import Flask, render_template
from application.app import MyApp
from application.urls import routes

def main():
    app = MyApp()
    app.add_resources(routes)
    app.run(host='0.0.0.0', port=5000, debug=True)

if __name__ == '__main__':
    main()