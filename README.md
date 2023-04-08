# Twitter-Kafka-Streaming-Service

> This project is a demonstration of how to stream Twitter data using Kafka and various related technologies such as ZooKeeper, Kafka Proxy, multiple Kafka brokers, Schema Registry, and Schema Registry-UI services. In addition, I developed custom Twitter stream classes, Consumer and Producer classes, with and without Avro serialization and connected it with Confluent schema registry.

## What I Have Done
- Created custom Twitter stream classes, Consumer and Producer classes, to stream Twitter data into Kafka
- Set up a Kafka cluster with multiple brokers for efficient processing of Twitter data
- Implemented schema registry for storing and managing data schemas, and ensured compatibility between the producer and consumer schemas
- Configured Kafka Proxy for secure and reliable communication between the Kafka cluster and other services
- Connected a user interface for Schema Registry using the Schema Registry-UI service

## Technologies Used
- Python
- Kafka
- ZooKeeper
- Kafka Proxy
- Schema Registry
- Schema Registry-UI
- Docker

## What I Learned
- Working with various components of a Kafka-based data streaming system such as brokers, schema registry, Kafka Proxy, and custom stream classes
- Efficient processing of high volumes of data using a distributed messaging system
- Ensuring data compatibility and consistency with the help of schema registry
- Working with Docker to containerize Kafka streaming applications and dependencies for easy deployment and scaling
- Insights into the nuances of working with Twitter's API and real-time data streaming from social media platforms
- Becoming a more proficient data engineer with a solid understanding of data streaming using Kafka.