import os
import json
import time
import requests

from dotenv import load_dotenv


# Load environment variables
load_dotenv()

# Constants
GRAPHQL_ENDPOINT = os.getenv("SUBGRAPH_URL")
QUERIES_DIR = 'Queries'
OUTPUTS_DIR = 'Outputs'


def main():
    # Ensure the output directory exists
    if not os.path.exists(OUTPUTS_DIR):
        os.makedirs(OUTPUTS_DIR)

    # List all GraphQL query files
    query_files = [f for f in os.listdir(QUERIES_DIR) if f.endswith('.graphql')]
    query_files.sort() # ascending order

    # Process each query file
    for query_file in query_files:
        query_path = os.path.join(QUERIES_DIR, query_file)
        output_path = os.path.join(OUTPUTS_DIR, query_file.replace('.graphql', '.json'))

        try:
            # Read query from a file
            with open(query_path, 'r') as file:
                query = file.read()

            # Execute query
            start_time = time.time()
            query_result = requests.post(GRAPHQL_ENDPOINT, json={'query': query}, timeout=40)
            elapsed_time = time.time() - start_time

            # Save query result
            with open(output_path, 'w') as file:
                json.dump(query_result.json(), file, indent=4)

            print(f"\nSaved results of {query_file} to {output_path}")
            print(f'Elapsed time: {elapsed_time:.2f} seconds')

        except Exception as e:
            print(f"\nFailed to execute {query_file}: {e}")


if __name__ == "__main__":
    main()