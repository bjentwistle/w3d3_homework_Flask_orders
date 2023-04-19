from flask import Flask

app = Flask(__name__)

from controllers import controller

if __name__ == "__main__":
    app.run(debug = True)

# above is boiler plate code for starting - telling your app we are using Flask for the framework

