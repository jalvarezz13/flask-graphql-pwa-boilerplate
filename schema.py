import graphene

# Variables
last_book_id = 5


class Book(graphene.ObjectType):
    id = graphene.ID()
    title = graphene.String()
    author = graphene.String()
    isbn = graphene.String()


# Create an in-memory list of books for testing
books_data = [
    Book(id="1", title="The Great Gatsby", author="F. Scott Fitzgerald", isbn="9780743273565"),
    Book(id="2", title="To Kill a Mockingbird", author="Harper Lee", isbn="9780061120084"),
    Book(id="3", title="1984", author="George Orwell", isbn="9780451524935"),
    Book(id="4", title="The Catcher in the Rye", author="J.D. Salinger", isbn="9780316769488"),
    Book(id="5", title="Pride and Prejudice", author="Jane Austen", isbn="9780141439518"),
]


class Query(graphene.ObjectType):
    books = graphene.List(Book)

    def resolve_books(self, info):
        return books_data


class CreateBook(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        author = graphene.String()
        isbn = graphene.String()

    book = graphene.Field(Book)

    def mutate(self, info, title, author, isbn):
        global last_book_id
        # Increment the ID for the new book
        last_book_id += 1
        new_book = Book(id=str(last_book_id), title=title, author=author, isbn=isbn)
        books_data.append(new_book)
        return CreateBook(book=new_book)


class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
