
# AirBnB clone

This project is a copy of the AirBnB website.

## Authors

- [@AplusJS](https://github.com/aplusJsDev)


- [@AyoubMotei](https://github.com/AyoubMotei)
## Steps

### 1. The console
- Create a data model

- manage (create, update, destroy, etc) objects via a console / command interpreter

- store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine

<img alt="step1 screenshot" src="./images/step1.jpg" />

#### Run The console Locally

Clone the project

```bash
  git clone https://github.com/aplusJsDev/AirBnB_clone.git
```

Go to the project directory

```bash
  cd AirBnB_clone
```

Then Run:

```bash
  ./console.py
```
#### Usage/Execution

<img alt="execution1 example" src="./images/air_console1.jpg">

<img alt="execution1 example" src="./images/air_console2.jpg">