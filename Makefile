VERSION := $(shell sh -c 'cat VERSION')

docker: 
	@docker build -t rock1017/log-generator:$(VERSION) .

push: docker
	@docker image tag rock1017/log-generator:$(VERSION) rock1017/log-generator:latest
	@docker push rock1017/log-generator:$(VERSION)
	@docker push rock1017/log-generator:latest