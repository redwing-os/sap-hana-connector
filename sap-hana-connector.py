import os
from hdbcli import dbapi
import grpc
import vectordb_pb2
import vectordb_pb2_grpc
from sklearn.feature_extraction.text import TfidfVectorizer

# SAP HANA connection parameters from environment variables
HOST = os.environ.get('HANA_HOST', 'default_host')
PORT = os.environ.get('HANA_PORT', '30015')  # Default is usually 30015
USER = os.environ.get('HANA_USER', 'default_user')
PASSWORD = os.environ.get('HANA_PASSWORD', 'default_password')

# gRPC server configuration
GRPC_HOST = os.environ.get('GRPC_HOST', 'localhost')
GRPC_PORT = os.environ.get('GRPC_PORT', '50051')

# SAP HANA query configuration
TABLE_NAME = os.environ.get('HANA_TABLE', 'YOUR_TABLE')
COLUMN_NAME = os.environ.get('HANA_COLUMN', 'text_column')

def connect_to_hana(HOST, PORT, USER, PASSWORD):
    """
    Connect to SAP HANA database and return the connection object.
    """
    try:
        conn = dbapi.connect(
            address=HOST,
            port=PORT,
            user=USER,
            password=PASSWORD
        )
        print("Successfully connected to SAP HANA")
        return conn
    except Exception as e:
        print(f"Error connecting to SAP HANA: {e}")
        return None

# Function to write vectors to vector DB using gRPC
def write_vectors_to_vector_db(vectors, key_prefix):
    channel = grpc.insecure_channel(f'{GRPC_HOST}:{GRPC_PORT}')
    stub = vectordb_pb2_grpc.VectorDBStub(channel)
    for i, vector in enumerate(vectors):
        key = f"{key_prefix}_{i}"
        request = vectordb_pb2.VectorWriteRequest(key=key, vector=vector)
        response = stub.Write(request)
        if response.success:
            print(f"Vector {key} written successfully")
        else:
            print(f"Failed to write vector {key}")

def execute_query(conn, query):
    """
    Execute a query and return the results.
    """
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result
    except Exception as e:
        print(f"Error executing query: {e}")
        return None

# Function to generate vector embeddings (example placeholder)
def generate_vector_embeddings(data):
    """
    Generates vector embeddings from text data using TF-IDF.
    
    Args:
        data (list of str): A list of text data.

    Returns:
        list of list of float: A list of vector embeddings.
    """
    # Initialize the TF-IDF vectorizer
    vectorizer = TfidfVectorizer()

    # Fit and transform the data to get vector embeddings
    tfidf_matrix = vectorizer.fit_transform(data)

    # Convert the tfidf_matrix to a list of lists (vector embeddings)
    vectors = tfidf_matrix.toarray().tolist()

    return vectors

def main():
    conn = connect_to_hana(HOST, PORT, USER, PASSWORD)
    
    if conn:
        query = f"SELECT {COLUMN_NAME} FROM {TABLE_NAME}"
        result = execute_query(conn, query)
        
        if result:
            text_data = [row[0] for row in result]
            vectors = generate_vector_embeddings(text_data)
            write_vectors_to_vector_db(vectors, TABLE_NAME)
            
        conn.close()
     
if __name__ == "__main__":
    main()