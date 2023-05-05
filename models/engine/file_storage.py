from models.base_model import BaseModel
from json import dump, load
import os

classes = {'BaseModel': BaseModel}

class FileStorage:
	__file_path = 'file.json'
	__objects = {}

	def all(self):
		return self.__class__.__objects

	def new(self, obj):
		cls_name_id = f"{obj.__class__.__name__}.{obj.id}"
		self.__class__.__objects[cls_name_id] = obj

	def save(self):
		objects = self.__class__.__objects
		dict_objects = {key: value.to_dict() for key, value in objects.items()}
		with open(self.__class__.__file_path, 'w') as fp:
			dump(dict_objects, fp)

	def reload(self):
		if os.path.exists(self.__class__.__file_path):
			with open(self.__class__.__file_path, 'r') as fp:
				dict_objects = load(fp)
			
			self.__class__.__objects = {k: classes[v['__class__']](**v) for k, v in dict_objects.items()}