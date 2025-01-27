# AppRSSFeed

### Running locally

Run the following commands to bootstrap your environment if you are unable to run the application using Docker

```bash
cd rss_feed
pip install -r requirements/dev.txt
npm install
npm run-script build
npm start  # run the webpack dev server and flask server using concurrently
```

Go to `http://localhost:5000`. You will see a pretty welcome screen.

#### Database Initialization (locally)

Once you have installed your DBMS, run the following to create your app's
database tables and perform the initial migration

```bash
flask db init
flask db migrate
flask db upgrade
```


## Running Tests/Linter

To run all tests, run

```bash
flask test
```

To run the linter, run

```bash
flask lint
```

The `lint` command will attempt to fix any linting/style errors in the code. If you only want to know if the code will pass CI and do not wish for the linter to make changes, add the `--check` argument.
