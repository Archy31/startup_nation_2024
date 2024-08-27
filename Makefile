
start:
	source venv/bin/activate
	pip install -r requirements.txt
	sudo docker run --name startup-nation -p 5432:5432 -e POSTGRES_PASSWORD=secret -d postgres
	sudo docker exec -ti startup-nation createdb -U postgres sn_db

	
db:
	sudo docker exec -ti startup-nation psql -U postgres sn_db
