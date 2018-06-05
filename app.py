from flask import Flask
from api.controllers.delfos import DelfosController
delfos = Flask("delfos")

controller = DelfosController()

@delfos.route('/v1/delfos/lunch')
def lunch():
    value = controller.lunch("09:00")
    return value

if __name__ == '__main__':    
    delfos.run()