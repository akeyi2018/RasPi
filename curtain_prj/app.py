import os
from flask import Flask, render_template, request
from sunrise import sun_info

app = Flask(__name__)

def get_json():
    path = os.path.dirname(os.path.realpath(__file__))
    re = sun_info('', path)
    return re.get_latlon_from_json()
    

@app.route('/')
def index():
    return render_template('index.html', status ='')

@app.route('/open')
def open_curtain():
    return render_template('index.html', status = 'open')

@app.route('/close')
def close_curtain():
    return render_template('index.html', status = 'close')

@app.route('/getinfo')
def get_curtain_info():
    pass
    
@app.route('/user_info')
def get_user_info():
    user = get_json()
    print(user)
    return render_template('index.html', user = user)

@app.route('/setpostcode')
def set_post_code():
    return 'set post code'
    # if request.method == 'POST':
    #     lat,lon = cal_location(str(request.form['postcode']))
    #     return render_template('index.html',
    #     set_result=str(request.form['postcode']),
    #     lat = lat,
    #     lon = lon)

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=5000)