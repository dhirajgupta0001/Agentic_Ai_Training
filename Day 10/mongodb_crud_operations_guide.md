# MongoDB CRUD Operations: Beginner's Guide

## Introduction

MongoDB is a NoSQL database that stores data in the form of **documents**. Documents are grouped into **collections**, and collections are stored inside **databases**.

MongoDB follows the CRUD model:

* **C** → Create
* **R** → Read
* **U** → Update
* **D** → Delete

CRUD operations are the fundamental operations used to interact with data in MongoDB.

---

# MongoDB Data Hierarchy

```text
MongoDB Server
    │
    ├── Database
    │      │
    │      ├── Collection
    │      │      │
    │      │      ├── Document
    │      │      ├── Document
    │      │      └── Document
```

Example:

```text
companyDB
│
├── employees
│   ├── {name: "John", age: 25}
│   ├── {name: "Alice", age: 30}
│
├── departments
│   ├── {name: "HR"}
│   ├── {name: "IT"}
```

---

# SQL vs MongoDB

| SQL      | MongoDB    |
| -------- | ---------- |
| Database | Database   |
| Table    | Collection |
| Row      | Document   |
| Column   | Field      |

---

# Starting MongoDB Shell

Open terminal and launch MongoDB shell:

```bash
mongosh
```

You should see:

```text
test>
```

---

# Creating or Switching Databases

Use:

```javascript
use companyDB
```

Output:

```text
switched to db companyDB
```

MongoDB creates the database only when data is first inserted.

Check current database:

```javascript
db
```

Output:

```text
companyDB
```

---

# Collections

Collections are similar to tables in relational databases.

MongoDB automatically creates a collection when you insert the first document.

Example:

```javascript
db.employees.insertOne({
    name: "John",
    age: 25,
    department: "IT"
})
```

This automatically creates:

```text
Database: companyDB
Collection: employees
```

View collections:

```javascript
show collections
```

Output:

```text
employees
```

---

# CRUD Operations

```text
C → Create
R → Read
U → Update
D → Delete
```

---

# CREATE Operations

Create operations add documents to a collection.

---

## insertOne()

Insert a single document:

```javascript
db.employees.insertOne({
    name: "Alice",
    age: 28,
    department: "HR"
})
```

Stored document:

```json
{
    "_id": ObjectId("..."),
    "name": "Alice",
    "age": 28,
    "department": "HR"
}
```

MongoDB automatically generates the `_id` field.

---

## insertMany()

Insert multiple documents:

```javascript
db.employees.insertMany([
    {
        name: "Bob",
        age: 30,
        department: "IT"
    },
    {
        name: "Charlie",
        age: 35,
        department: "Finance"
    }
])
```

---

# READ Operations

Read operations retrieve documents from collections.

---

## find()

Retrieve all documents:

```javascript
db.employees.find()
```

Example output:

```json
[
    {
        "name": "Alice",
        "age": 28
    },
    {
        "name": "Bob",
        "age": 30
    }
]
```

---

## Pretty Print Results

```javascript
db.employees.find().pretty()
```

---

## find() with Filter

Retrieve specific documents:

```javascript
db.employees.find({
    name: "Alice"
})
```

---

## findOne()

Retrieve a single document:

```javascript
db.employees.findOne({
    department: "HR"
})
```

---

# UPDATE Operations

Update operations modify existing documents.

---

## updateOne()

Update one matching document:

```javascript
db.employees.updateOne(
    { name: "Alice" },
    {
        $set: {
            age: 29
        }
    }
)
```

Before:

```json
{
    "name": "Alice",
    "age": 28
}
```

After:

```json
{
    "name": "Alice",
    "age": 29
}
```

---

## updateMany()

Update multiple documents:

```javascript
db.employees.updateMany(
    { department: "IT" },
    {
        $set: {
            status: "Active"
        }
    }
)
```

Updates all employees in the IT department.

---

## replaceOne()

Replace the entire document:

```javascript
db.employees.replaceOne(
    { name: "Alice" },
    {
        name: "Alice",
        age: 30,
        city: "New York"
    }
)
```

Result:

```json
{
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
```

Note:

All previous fields are removed unless explicitly included.

---

# DELETE Operations

Delete operations remove documents from a collection.

---

## deleteOne()

Delete a single document:

```javascript
db.employees.deleteOne({
    name: "Alice"
})
```

Deletes the first matching document.

---

## deleteMany()

Delete multiple documents:

```javascript
db.employees.deleteMany({
    department: "IT"
})
```

Deletes all matching documents.

---

# Useful MongoDB Commands

---

## Show Databases

```javascript
show dbs
```

---

## Show Collections

```javascript
show collections
```

---

## Show Current Database

```javascript
db
```

---

## Count Documents

```javascript
db.employees.countDocuments()
```

---

## Drop Collection

Delete an entire collection:

```javascript
db.employees.drop()
```

---

## Drop Database

Delete the current database:

```javascript
db.dropDatabase()
```

---

# Complete Beginner Example

```javascript
// Create database
use companyDB

// Insert documents
db.employees.insertMany([
    {
        name: "John",
        age: 25,
        department: "IT"
    },
    {
        name: "Alice",
        age: 28,
        department: "HR"
    }
])

// Read all documents
db.employees.find().pretty()

// Update document
db.employees.updateOne(
    { name: "John" },
    {
        $set: {
            age: 26
        }
    }
)

// Delete document
db.employees.deleteOne(
    { name: "Alice" }
)

// Display final documents
db.employees.find().pretty()
```

---

# Atomic Operations in MongoDB

MongoDB guarantees that write operations are atomic at the document level.

Example:

```javascript
db.accounts.updateOne(
    { accountNo: 1001 },
    {
        $set: {
            balance: 5000
        }
    }
)
```

The document is updated completely or not at all.

---

# Bulk Write Operations

MongoDB supports executing multiple write operations together.

Example:

```javascript
db.employees.bulkWrite([
    {
        insertOne: {
            document: {
                name: "Tom"
            }
        }
    },
    {
        updateOne: {
            filter: {
                name: "John"
            },
            update: {
                $set: {
                    age: 30
                }
            }
        }
    }
])
```

Useful for:

* High-performance operations
* Batch updates
* Bulk imports

---

# MongoDB CRUD Summary

| Operation   | Method         |
| ----------- | -------------- |
| Create One  | `insertOne()`  |
| Create Many | `insertMany()` |
| Read Many   | `find()`       |
| Read One    | `findOne()`    |
| Update One  | `updateOne()`  |
| Update Many | `updateMany()` |
| Replace One | `replaceOne()` |
| Delete One  | `deleteOne()`  |
| Delete Many | `deleteMany()` |

---

# Interview Questions

### What is CRUD?

CRUD stands for Create, Read, Update, and Delete.

---

### What is a document?

A document is a BSON/JSON-like data structure stored inside a collection.

Example:

```json
{
    "name": "John",
    "age": 25
}
```

---

### What is a collection?

A collection is a group of MongoDB documents.

---

### Difference between Collection and Database?

| Database               | Collection            |
| ---------------------- | --------------------- |
| Contains collections   | Contains documents    |
| Higher-level container | Lower-level container |

---

### Difference between insertOne() and insertMany()?

| insertOne()          | insertMany()               |
| -------------------- | -------------------------- |
| Inserts one document | Inserts multiple documents |

---

# Interview Definition

MongoDB CRUD operations are the fundamental database operations used to create, read, update, and delete documents within collections. These operations enable applications to manage and manipulate data stored in MongoDB databases.
