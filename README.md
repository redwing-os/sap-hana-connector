# SAP HANA Connector Utility | Redwing Vector gRPC

## Overview

This script facilitates the extraction of text data from SAP HANA, converts this data into vector embeddings using TF-IDF, and then writes these embeddings to a vector database using gRPC.

## Prerequisites

- Python 3.x
- SAP HANA Python driver (`hdbcli`)
- gRPC and associated Python packages
- scikit-learn

## Installation

To install the necessary libraries, run the following commands:

```bash
pip install hdbcli grpcio scikit-learn
```

## Configuration

Set the following environment variables to configure the script:

- `HANA_HOST`: The hostname or IP address of the SAP HANA server.
- `HANA_PORT`: The port number on which SAP HANA is listening (default is 30015).
- `HANA_USER`: Your username for SAP HANA.
- `HANA_PASSWORD`: Your password for SAP HANA.
- `GRPC_HOST`: The hostname for the gRPC server.
- `GRPC_PORT`: The port number for the gRPC server.

You can set these variables in your environment like so:

```bash
export HANA_HOST=hostname
export HANA_PORT=port
export HANA_USER=username
export HANA_PASSWORD=password
export GRPC_HOST=grpc_hostname
export GRPC_PORT=grpc_port
```

## Usage

To run the script, use the following command:

```bash
python sap-hana-connector.py
```

Replace `script_name.py` with the actual name of your script.

## AWS Marketplace

For our ready-to-implement Vector Database with gRPC integration please visit the AWS Marketplace and utilize our product here https://aws.amazon.com/marketplace/pp/prodview-y2jhov2jzjryk

## Support

For any issues or support, please visit https://docs.redwing.ai or message hello [at] redwing.ai