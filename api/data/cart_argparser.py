from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('item_id', required=False)

edit_parser = reqparse.RequestParser()
edit_parser.add_argument('item_id', required=False)

