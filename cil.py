from typing import Protocol

class Printable(Protocol):
    def print(self) -> None:
        pass

class ConsolePrinter:
    def print(self) -> None:
        print("Printing to console")

class FilePrinter:
    def print(self) -> None:
        # code to print to a file

def print_item(item: Printable) -> None:
    item.print()

print_item(ConsolePrinter())
print_item(FilePrinter())
