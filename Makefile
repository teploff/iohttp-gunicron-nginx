.PHONY: up down

up:
	docker-compose -f deployment/docker-compose.yml up --build -d ;\
	docker image prune -f ;\

down:
	docker-compose -f deployment/docker-compose.yml down ;\