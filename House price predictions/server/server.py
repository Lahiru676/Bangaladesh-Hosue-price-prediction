from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_city_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    data = request.get_json()  # Handles JSON input
    area_in_marla = float(data['area_in_marla'])
    city = data['city']
    bedrooms = int(data['bedrooms'])
    baths = int(data['baths'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(city, area_in_marla, bedrooms, baths)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()
