# for local usage
1. cd to the directory
1. $ `docker-compose up`
1. $ `docker exec -it vytrac-26930_web_1 bash`
    - note: run this after the compose finish, make sure `vytrac-26930_web_1` is the currect name for the container
1. $ `./manage.py migrate`
1. $ `./manage.py dummy_data`
1. open new terminal and cd to the directory
1. `docker commit vytrac-26930_web_1 vytrac-26930_web:latest`
1. `docker-compose down`
    - note: this step maybe not nessury but just you need to restart the web countainer
1. `docker-compose up`

## alternativly for local usage
    - you can access the live code from pycharm `code with me` tool
    - in the terminal just run the following command and it will connect you to my code project live, so you will get all updates on the fly
- `/bin/bash -c "$(curl -fsSL 'https://code-with-me.jetbrains.com/xbv62f6qjP_vfIgiS6YxzQ/cwm-client-launcher-mac.sh')"`

- or you can copy and paset this in pycharm `code with me/ Join Another IDE as Particiant`
    - `https://code-with-me.jetbrains.com/xbv62f6qjP_vfIgiS6YxzQ#p=PY&fp=FAC96DF6F7A81B46BD3EE7883F5A9D468669F89CF68FB775F3E070F67B92CA3B`

# rest migrations
```
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
# you may need to delete database (postgres in this case), 
pipenv shell
pipenv uninstall django
pipenv install django
./manage.py makemigrations
./manage.py migrate
```