buildd:
	docker build -t flask_hello_world:test .

rund:
	docker run -p 8888:8888 -t flask_hello_world:test


