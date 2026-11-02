
import unittest
from app import hello_world
class TestHelloWorld(unittest.TestCase):  
  
  def test_hello_world_message(self):        
    self.assertEqual(hello_world(), "Hello, devops!")
    
  def test_hello_world_type(self):
    self.assertIsInstance(hello_world(), str)

  def test_welcome_message_ayush(self):
    self.assertEqual(welcome_message("Ayush"),"welcome to devops, Ayush!")
  
  def test_welcome_message_avesh(self):
      self.assertEqual(welcome_message("Avesh"),"welcome to devops, Avesh!")

  if __name__ == "__main__":    
    unittest.main()
