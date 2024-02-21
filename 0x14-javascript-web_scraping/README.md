# Project Name

**0x14. JavaScript - Web scraping**

## Requirements

- All your files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/node`.
- Your code should be `semistandard` compliant (version 16.x.x).
- All your files must be executable.
- You are not allowed to use `var`.

## Learning Objectives

- How to manipulate JSON data.
- How to use `request` and fetch API.
- How to read and write a file using `fs` module.

## Installation Instructions

### Install Node 14

```
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

### Install semi-standard

[Documentation](https://github.com/standard/semistandard)

```
$ sudo npm install semistandard --global
```

### Install request module and use it

[Documentation](https://github.com/request/request)

```
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```

## Javascript Scripts

- **0. Readme** - A script that reads and prints the content of a file. Usage: ./_script_ _path_to_file_. - `0-readme.js`.
- **1. Write me** - A script that writes a string to a file. Usage: ./_script_ _path_to_file_ _string_. - `1-writeme.js`.
- **2. Status code** - A script that display the status code of a `GET` request. Usage: ./_script_ *https://alx-intranet.hbtn.io/status*. - `2-statuscode.js`.
- **3. Star wars movie title** - A script that prints the title of a Star Wars movie where the episode number matches a given integer. Usage: ./_script_ _number_. - `3-starwars_title.js`.
- **4. Star wars Wedge Antilles** - A script that prints the number of movies where the character “Wedge Antilles” is present. Usage: ./_script_ *https://swapi-api.alx-tools.com/api/films*. - `4-starwars_count.js`.
- **5. Loripsum** - A script that gets the contents of a webpage and stores it in a file. Usage: ./_script_ *http://loripsum.net/api* _file_. - `5-request_store.js`.
- **6. How many completed?** - A script that computes the number of tasks completed by user id. Usage: ./_script_ *https://jsonplaceholder.typicode.com/todos*- `6-completed_tasks.js`.
