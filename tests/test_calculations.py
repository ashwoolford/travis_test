import unittest 
from travis_test.pkg.calculations import CalculatioinsTest 


class TestStemmer(unittest.TestCase):


	def setUp(self):
		self.t = CalculatioinsTest()
		print('Setup')

	def tearDown(self):	
		print('Tear Down\n')

	def test_add(self):
		self.assertEqual(self.t.add(2,3),5)
		self.assertEqual(self.t.add(2,5),7)
		self.assertEqual(self.t.add(4,2),6)

	def test_sub(self):
		self.assertEqual(self.t.sub(3,2),1)
		self.assertEqual(self.t.sub(5,1),4)
		self.assertEqual(self.t.sub(4,2),2)

	def test_mul(self):
		self.assertEqual(self.t.mul(2,3),6)
		self.assertEqual(self.t.mul(2,5),10)
		self.assertEqual(self.t.mul(4,2),8)		


#if __name__ == '__main__':
#	unittest.main()		