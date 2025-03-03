from flask import Flask, request, jsonify, render_template
from mastodon_service import create_post, retrieve_post, delete_post
from flask import Flask, request, jsonify, render_template
#Below part of the code was contributed by Deven Desai
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Define other routes for create, retrieve, and delete
@app.route('/create', methods=['POST'])
def create():
    content = request.json.get('content')
    response = create_post(content)
    return jsonify(response)

@app.route('/retrieve/<post_id>', methods=['GET'])
def retrieve(post_id):
    response = retrieve_post(post_id)
    return jsonify(response)

@app.route('/delete/<post_id>', methods=['DELETE'])
def delete(post_id):
    status_code = delete_post(post_id)
    return jsonify({'status': status_code})

if __name__ == '__main__':
    app.run(debug=True)