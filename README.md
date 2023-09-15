<h1 align="center">Flask GraphQL PWA Boilerplate 🚀📦</h1>

### Table of Contents

- [📢 What is _Flask GraphQL PWA Boilerplate_?](#-what-is-flask-graphql-pwa-boilerplate)
- [⚙️ Execution](#%EF%B8%8F-execution)
- [⭐ Current Features](#-current-features)

## 📢 What is _Flask GraphQL PWA Boilerplate_?

The **Flask GraphQL PWA Boilerplate** is a template for building a **Progressive Web App (PWA)** using **Flask** and **GraphQL**. This template includes a base schema and a simple example of a book library. The app is also designed as a PWA, allowing it to be installed in a web browser and providing offline support.

Give it a try! 🚀

## ⚙️ Execution

To run the **Flask GraphQL PWA Boilerplate**, you can use `pipenv`. First, ensure you have `pipenv` installed. Then, navigate to the root directory of the project, where you can install the dependencies and activate the virtual environment using the following commands:

```bash
pipenv install
pipenv shell
```

Finally, start the server by running:

```bash
python app.py
```

## ⭐ Current features

The GraphQL schema, queries, and mutations are defined in the schema.py file. Currently, the following schema is defined:

```python
class Book(graphene.ObjectType):
    id = graphene.ID()
    title = graphene.String()
    author = graphene.String()
    isbn = graphene.String()
```

You can query the list of books using the following GraphQL query:

```graphql
query {
  books {
    id
    title
    author
    isbn
  }
}
```

Additionally, you can create a new book using the following GraphQL mutation:

```graphql
mutation {
  createBook(title: "The Lord of the Rings", author: "J. R. R. Tolkien", isbn: "978-0544003415") {
    book {
      id
    }
  }
}
```

The GraphiQL Playground for executing these operations is available at the `/graphql` endpoint [http://localhost:5000/graphql](http://localhost:5000/graphql).

Regarding the PWA features, the following are included, and you can install the app through your web browser:

- ✅ Service Worker
- ✅ Web App Manifest
- ✅ Offline support

See browser support for PWAs [here](https://caniuse.com/serviceworkers).

<hr>

<div align="center">
    <span>Made with ❤️ by <b><a href="https://www.linkedin.com/in/jalvarezz13/">jalvarezz13</a></b></span>
</div>
