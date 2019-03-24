from flask import *
import os	
app = Flask(__name__)

#app.run(host='0.0.0.0')

@app.route('/', methods=['GET','POST'])
def index():
	images = os.listdir(os.path.join(app.static_folder, "images"))
	return render_template('routing/hello.html', images=images)

if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 2486))
    app.run(host=host, port=port)
