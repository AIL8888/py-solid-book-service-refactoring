from dataclasses import dataclass

from app.display.registry import get_displayer
from app.printing.registry import get_printer
from app.serialization.registry import get_serializer
from app.services.book_service import BookService


@dataclass(frozen=True)
class Book:
    title: str
    content: str

    def display(self, display_type: str) -> None:
        displayer = get_displayer(display_type)
        displayer.display(self)

    def print_book(self, print_type: str) -> None:
        printer = get_printer(print_type)
        printer.print(self)

    def serialize(self, serialize_type: str) -> str:
        serializer = get_serializer(serialize_type)
        return serializer.serialize(self)


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    service = BookService()
    return service.execute(book, commands)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
