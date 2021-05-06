
import json
from datetime import datetime
from datetime import date

info = {
	"name": "ffm",
	"birth": datetime.now(),
	"age": 18,
	'hobbies': ['music', 'read', 'dancing'],
	'addr': {
		'country': 'China',
		'city': 'shanghai'
	}
}


class CJsonEncoder(json.JSONEncoder):

	def default(self, obj):
		if isinstance(obj, datetime):
			return obj.strftime('%Y-%m-%d %H:%M:%S')
		elif isinstance(obj, date):
			return obj.strftime('%Y-%m-%d')
		else:
			return json.JSONEncoder.default(self, obj)


json_info = json.dumps(info, cls=CJsonEncoder)
print(json_info)

"""
json_info = {
	"name": "ffm",
	"birth": "2020-04-04 11:51:40",
	"age": 18,
	"hobbies": [
			"music",
			"read",
			"dancing"
			],
	"addr": {
		"country": "China",
		"city": "shanghai"
	}
}

"""