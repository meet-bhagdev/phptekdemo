# Laravel ToDo App

This is a simple ToDo app with multiple user support.

This is built on Laravel Framework 5.1. This is for the php[tek] conference. 

## Prerequisties
- PHP
- Composer
- Laravel


## Installation

Install the required drivers-
```
sudo apt-get install freetds-common freetds-bin unixodbc php5-sybase
sudo apt-get install freetds-dev freetds-bin tdsodbc
```

Clone the repository-
```
git clone https://github.com/csucla2015/phptekdemo.git
```

Then cd into the folder with this command-
```
cd phptekdemo
```

Then do a composer install
```
composer install
```


Then edit `.env` file with appropriate credential for your database server. Just edit these two parameter(`DB_USERNAME`, `DB_PASSWORD`).

Then create a database named `todos` and then do a database migration using this command-
```
php artisan migrate
```

Then change permission of storage folder using thins command-
```
(sudo) chmod 777 -R storage
```


## Run server

Run server using this command-
```
php artisan serve
```

Then go to `http://localhost:8000` from your browser and see the app.

## Ask a question?

If you have any questions, please contact me at meetb@microsoft.com
