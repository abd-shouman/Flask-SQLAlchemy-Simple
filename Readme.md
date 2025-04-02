# Flask-SQLAlchemy Template
A Sample Flask-SQLAlchemy boilerplate that helps you save time

## Project Structure
The Project is organized into 4 main directories
- Controllers
- Models
- Repositories
- Utils

## Modulrization
Blueprint is used to organize routing.<br/>
No view is added (Use tools like Postman for testing)

## Database
SQLAlchemy is used for Database connection<br/>
Mainly SQLAlchemy Declarative mapping (as opposed to Imperative mapping)

## Database Connection
The database connection is established using a connection string stored in a yaml file `config.yaml` <br/>
A sample connection string would look something like 
`connection_string: "sqlite:///mydatabase.db"`


## ToDo

- [ ] Add addtional models
    - [ ] Explore 1-* relationship between model
- [ ] Test Flask Commands

## Run the app
Entry point: App.py

### Option 1: Normal Python Run
- Run `app.py` as a python file

### Option 2: Flask command (Recommended)
- Run command 'Flask run'

### Warning: Using in-memory SQLLite 
If you use an in-memory SQLLite instead of a file database you may encounter some issue. <br/>If you use `option 1` and set `debug=True` in `app.run(host='0.0.0.0', port=5000, threaded=False, debug=False)` the app will fail to commit changes to the database.

This is because the `connection` instance created in the `DI` class will be different than the one seen by the `Task Repository` class, which will cause an error since `Task Repository` can not see any table.