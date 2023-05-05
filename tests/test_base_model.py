import unittest
import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
	def setUp(self):
		self.sample_dict_inst = {
			'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
			'name': 'My First Model',
			'__class__': 'BaseModel',
			'created_at': '2017-09-28T21:05:54.119427',
			'updated_at': '2017-09-28T21:05:54.119572'
		}
		self.sample_obj_inst = BaseModel()

	def test_constructor_dict_param(self):
		''' 
			Test when instance dictionary is passed into
			the BaseModel Constructor (__init__) as kwargs
		'''
		obj_inst = BaseModel(**self.sample_dict_inst)
		self.assertTrue(obj_inst.id == self.sample_dict_inst.get('id'))
		self.assertTrue(type(obj_inst.created_at) == datetime.datetime)
		self.assertTrue(type(obj_inst.updated_at) == datetime.datetime)
		
	def test_constructor(self):
		'''
			Test when a new instance of BaseModel is created
		'''
		new_obj_inst = BaseModel()
		new_obj_inst.name = 'My First Model'

		self.assertFalse(self.sample_obj_inst.id == new_obj_inst.id)
		self.assertTrue(type(new_obj_inst.created_at) == datetime.datetime)
		self.assertTrue(type(new_obj_inst.updated_at) == datetime.datetime)

	def test_str_dunder(self):
		obj_to_str = f"[BaseModel] (56d43177-cc5f-4d6c-a0c1-e167f8c27337) {self.sample_dict_inst}"
		obj_inst = BaseModel(**self.sample_dict_inst)
		
		self.assertEquals(str(obj_inst), obj_to_str)