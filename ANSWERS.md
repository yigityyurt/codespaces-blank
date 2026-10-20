1. The Dockerfile uses optimized layering. Changing the order of dependency installation before copying source code preserves the build cache effectively.
2. Data written inside a container is lost when the container is removed. To keep data, Docker volumes or bind mounts should be used, and application state should be kept in an external database.
3. The latest tag is a risk for reproducibility because its content can change over time. Instead, a pinned version tag like python:3.11-slim was used.
4. An AI assistant was used to help structure the Dockerfile and write the homework steps.
