import jsonschema


complx_schema = {
  "$schema": "http://json-schema.org/draft-06/schema#",

  "definitions": {
    "address": {
      "type": "object",
      "properties": {
        "street_address": { "type": "string" ,
    "error_msg":"test error"},
        "city":           { "type": "string",
    "error_msg":"test error" },
        "state":          { "type": "string",
    "error_msg":"test error" }
      },
      "required": ["street_address", "city", "state"],
    "error_msg":"test error"
    }
  },

  "type": "object",

  "properties": {
    "billing_address": { "$ref": "#/definitions/address" },
    "shipping_address": {
      "allOf": [
        { "$ref": "#/definitions/address" },
        { "properties":
          { "type": { "enum": [ "residential", "business" ] } },
          "required": ["type"]
        }
      ]
    }
  }
}

def validate(_data, _schema):
    try:
        jsonschema.validate(_data, _schema)
    except jsonschema.ValidationError as e:
        return e.schema["error_msg"]

data = {
  "billing_address": {
    "street_address": "id ex reprehenderit",
    "city": "anim voluptate nulla",
    "state": "mollit non",
    "error_msg":"test error"
  },
  "shipping_address": {
    "street_address": "eu",
    "city": "mollit consequat commodo",
   # "state": "sunt",
    #"type": "business",
    "error_msg":"test error"
  }
}

if __name__ == '__main__':
    validate(data, complx_schema)