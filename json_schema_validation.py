from jsonschema import validate


schema = {
    "type" : "object",
    "properties" : {
        "price" : {
                "type" : "number",
                "validation_msg":"custom_validation msg"
            },
        "name" : {"type" : "string"},
    },
    "message":"test_msg"
}



if __name__ == '__main__':
    validate(instance={"name": "Eggs", "price": 231}, schema=schema)