# Author: Hussain Al Zerjawi
# Purpose: Practicing webhooks using Python and the Flask framework
# Date: 12/10/2022

from flask import Flask, request, abort, Response

# Initialize the app variable with a Flask instance
app = Flask(__name__)


@app.route("/webhook", methods=["POST"])
def webhook():
    if request.method == "POST":
        print(request.json)
        return Response(status=200)
    else:
        abort(400)

if __name__ == '__main__':
    app.run()
