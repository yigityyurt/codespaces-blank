# CENG413 HW-1
docker build -t ceng413-hw1 .
docker run -d -p 8080:8080 --name running-app ceng413-hw1
