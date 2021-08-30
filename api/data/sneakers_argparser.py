from flask_restful import reqparse

# парсер аргументов для UsSneakerser
parser = reqparse.RequestParser()
parser.add_argument('title', required=True)
parser.add_argument('image_url', required=True)
parser.add_argument('price', required=True)



# парсер аргументов для Sneakers - редактирование
edit_parser = reqparse.RequestParser()
edit_parser.add_argument('title', required=False)
edit_parser.add_argument('image_url', required=False)
edit_parser.add_argument('price', required=False)

