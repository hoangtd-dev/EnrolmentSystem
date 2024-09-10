from abc import ABC, abstractmethod

class BaseSystem(ABC):
	@abstractmethod
	def run(): raise NotImplementedError