# Base class Sequence for DNA,RNA,peptide...
from typing import Tuple, Union, List, overload
from abc import ABC, abstractmethod


class Sequence(ABC):
    def __init__(self, seq: str = "") -> None: ...
    @property
    def composition(self) -> dict:  ...
    @property
    def length(self) -> int:    ...
    @property
    def seq(self) -> str:   ...
    @property
    def weight(self) -> float:  ...
    @overload
    def align(self, subject: Union[str, "Sequence"], mode: int, return_score: bool) -> Tuple[str, str] :  ...
    @overload
    def align(self, subject: Union[str, "Sequence"], mode: int, return_score: bool) -> Tuple[str, str, float] :  ...
    def find(self, target:Union[str, "Sequence"]) -> List[int]:    ...
    def mutation(self, position: Union[str, int, List[int]], target: Union[str, "Sequence"]) -> str:   ...
    @abstractmethod
    def _print(self) -> str:    ...
    def __add__(self, s: Union[str, "Sequence"]) -> "Sequence": ...
    def __radd__(self, s: Union[str, "Sequence"]) -> "Sequence":    ...
    def __getitem__(self, index: int) -> str:   ...
    def __eq__(self, o: object) -> bool: ...
    def __len__(self) -> int:   ...
    def __str__(self) -> str:   ...
    def __repr__(self) -> str:  ...
    
    
class Peptide(Sequence):
    @property
    def pI(self) -> float:   ...
    def chargeInpH(self, pH:float) -> float:    ...
    def getHphob(self, window_size: int, show_img: bool) ->List[int]:    ...
    def _print(self) -> str:    ...


class RNA(Sequence):
    @property
    def reversed(self) -> Sequence: ...
    @property 
    def complemented(self) -> Sequence: ...
    @property 
    def GC(self) -> float:   ...
    def complement(self) -> None:   ...
    def reverse(self) -> None:  ...
    def getOrf(self, multi: bool, replace: bool) -> List[str]:  ...
    def transcript(self, filter: bool) -> List[str]: ...
    def _print(self) -> str:   ...


class DNA(RNA):
    def translate(self) -> Sequence: ...
    def transcript(self, filter=True) -> List[str]:  ...
    