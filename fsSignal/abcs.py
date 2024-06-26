# Builtin modules
from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import Any, Iterable, Union, TypeVar
# Third party modules
# Local modules
# Program
T = TypeVar("T")

class T_Lock(metaclass=ABCMeta):
	@abstractmethod
	def acquire(self, blocking:bool=..., timeout:float=...) -> bool: ...
	@abstractmethod
	def release(self) -> None: ...
	@abstractmethod
	def locked(self) -> bool: ...
	@abstractmethod
	def _is_owned(self) -> bool: ...
	@abstractmethod
	def __enter__(self) -> None: ...
	@abstractmethod
	def __exit__(self, type:Any, value:Any, traceback:Any) -> Any: ...

class T_Locker(metaclass=ABCMeta):
	lock:T_Lock
	@abstractmethod
	def acquire(self, blocking:bool=..., timeout:float=...) -> bool: ...
	@abstractmethod
	def release(self) -> None: ...
	@abstractmethod
	def owned(self) -> bool: ...
	@abstractmethod
	def locked(self) -> bool: ...
	@abstractmethod
	def __enter__(self) -> Any: ...
	@abstractmethod
	def __exit__(self, type:Any, value:Any, traceback:Any) -> Any: ...

class T_Signal(metaclass=ABCMeta):
	_force:bool
	@abstractmethod
	def get(self) -> bool: ...
	@abstractmethod
	def getSoft(self) -> bool: ...
	@abstractmethod
	def getHard(self) -> bool: ...
	@abstractmethod
	def check(self) -> None: ...
	@abstractmethod
	def checkSoft(self) -> None: ...
	@abstractmethod
	def checkHard(self) -> None: ...
	@abstractmethod
	def sleep(self, seconds:Union[int, float], raiseOnKill:bool=...) -> None: ...
	@abstractmethod
	def signalSoftKill(self, *args:Any, **kwargs:Any) -> None: ...
	@abstractmethod
	def signalHardKill(self, *args:Any, **kwargs:Any) -> None: ...
	@abstractmethod
	def iter(self, it:Iterable[T], checkDelay:float=...) -> Iterable[T]: ...
	@abstractmethod
	def softKill(self) -> None: ...
	@abstractmethod
	def hardKill(self) -> None: ...
	@abstractmethod
	def reset(self) -> None: ...
	@abstractmethod
	def getSoftSignal(self) -> T_Signal: ...
	@abstractmethod
	def getHardSignal(self) -> T_Signal: ...
	@abstractmethod
	def isActivated(self) -> bool: ...
	@abstractmethod
	def warpLock(self, lock:Any) -> T_Locker: ...
