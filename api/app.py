from flask import Flask
from flask_restful import Api
from werkzeug.security import generate_password_hash
from requests import post
import sneakers_resource
import cart_resource
from data import db_session
from data.sneakers import Sneakers
from data.cart import Cart

app = Flask(__name__)
api = Api(app)
app.secret_key = "dsjgfjkdshfjksdhfbsjkdfhsdjkhfskdfl"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

BASE_URL = '/api'

db_session.global_init("db/database.db")

# добавление REST-API
api.add_resource(sneakers_resource.SneakersListResource, '/api/sneakers')
api.add_resource(sneakers_resource.SneakersResource, '/api/sneakers/<int:sneakers_id>')
api.add_resource(cart_resource.CartListResource, '/api/cart')
api.add_resource(cart_resource.CartResource,
                 '/api/cart/<int:cart_id>')


@app.route(BASE_URL + '/postCart')
def post_cart():
    post("http://127.0.0.1:5000/api/cart", data={'item_id': 5})
    return "Cart has been added"

@app.route(BASE_URL + '/setUpMockSneakers')
def index():
    
    title = ["Мужские Кроссовки Nike Blazer Mid Suede", "Мужские Кроссовки Nike Air Max 270", "Мужские Кроссовки Nike Blazer Mid Suede", "Кроссовки Puma X Aka Boku Future Rider", "Кроссовки Puma X Aka Boku Future Rider", "Мужские Кроссовки Under Armour Curry 8", "Мужские Кроссовки Nike Kyrie 7", "Мужские Кроссовки Jordan Air Jordan 11", "Мужские Кроссовки Nike LeBron XVIII", "Мужские Кроссовки Nike Lebron XVIII Low", "Мужские Кроссовки Nike Blazer Mid Suede", "Кроссовки Puma X Aka Boku Future Rider" ]
    price = [12999, 15600, 8499, 8999, 15199, 11299, 10799, 16499, 13999, 8499, 8999, 11299] # 12 
    image_url = ["/img/sneakers/1.jpg", "/img/sneakers/2.jpg", "/img/sneakers/3.jpg", "/img/sneakers/4.jpg", "/img/sneakers/5.jpg", "/img/sneakers/6.jpg", "/img/sneakers/7.jpg", "/img/sneakers/8.jpg", "/img/sneakers/9.jpg", "/img/sneakers/1.jpg", "/img/sneakers/4.jpg", "/img/sneakers/10.jpg"]
    session = db_session.create_session()
    
    for i in range(len(title)):
     
        new_sneakers = Sneakers(title=title[i], price=price[i], image_url=image_url[i])
        session.add(new_sneakers)

    session.commit()
    session.close()

    return 'Sneakers has been added to database'


if __name__ == '__main__':
    app.run()
