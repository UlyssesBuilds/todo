# ToDo List
Full Stack learning 

This is a MVP of a TODO list utilizing OOP features and tying it in with a persistent SQL database

## Project Learning Overview
I recently solidified my understanding of Object-Oriented Programming (OOP) and revisited how OOP’s class-based design interacts with SQL. This project brings both together and has given me a much clearer view of how a persistent database can work alongside a web application.

Additionally, I’ve been deepening my understanding of building with Flask, working with HTTP protocols, and thinking through stateless design and server-client architecture—a mindset that is quite different from the command-line interface (CLI) workflows I’ve mostly worked in up to this point. I plan to continue building mini-projects to strengthen my understanding of systems architecture and how these components fit together.

While I’m currently using a cursor for SQL queries (which leans toward raw SQL operations), I recognize that Object Relational Mapping (ORM) is more commonly used in modern software engineering practices.

One key lesson from this project is just how critical good database design is—it directly affects how easily a system can evolve.
For example, I initially thought adding a simple "Complete Task" feature would be quick. In reality, it involved:

Database migrations

Object updates

Form handling

UI changes

This process helped me appreciate the hidden complexity behind feature updates and the importance of balancing upfront planning with iterative development.

# Tech Stack
Python
Flask
SQLite