from flask import Flask, request
from pt import gen_table


app = Flask(__name__)


@app.route('/')
def hello_world():
    return gen_table("projects", "Lon")

# @app.route('/json', methods=['POST'])
# def payload_play():
#     request_data = request.get_json()
#     if 'name' in request_data:
#         return f"Well....Hello {request_data['name']}!"
#     else:    
#         return "OK, I'm sorry.  Who are you?"
#     return "Something failed..."

# @app.route('/secret-guessing-game')
# def secret():
#     secret = request.args.get('secret')
#     if secret == 'starfish':
#         return 'Well done sir!'
#     else:
#         return "Nope!  Don't forget to send your secret as a parameter"
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8118)