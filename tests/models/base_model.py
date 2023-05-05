from uuid import uuid4
import models as m
from datetime import datetime

class BaseModel:

	def __init__(self, *args, **kwargs):
		date_format = '%Y-%m-%dT%H:%M:%S.%f'
		if len(kwargs):
			for key in kwargs:
				if key != '__class__':
					if key == 'created_at':
						setattr(self, 'created_at', datetime.strptime((kwargs['created_at']), date_format))
					elif key == 'updated_at':
						setattr(self, 'updated_at', datetime.strptime((kwargs['updated_at']), date_format))
					else:
						setattr(self, key, kwargs[key])
		else:
			self.id = str(uuid4())
			self.created_at = datetime.now()
			self.updated_at = datetime.now()
		m.storage.new(self)

	def __str__(self):
		return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

	def save(self):
		self.updated_at = datetime.now()
		m.storage.save()
	
	def to_dict(self):
		dict_copy = self.__dict__.copy()
		dict_copy['__class__'] = self.__class__.__name__
		dict_copy['created_at'] = datetime.isoformat(self.created_at)
		dict_copy['updated_at'] = datetime.isoformat(self.updated_at)
		return dict_copy
