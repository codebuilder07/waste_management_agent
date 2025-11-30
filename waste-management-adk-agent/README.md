# Waste Management ADK Agent

## Overview
The Waste Management ADK Agent is a FastAPI-based application designed to facilitate interactions with Google ADK services for waste management. This project provides a structured way to manage waste-related queries and store relevant information using a local rule agent and memory service.

## Project Structure
```
waste-management-adk-agent
├── src
│   ├── main_agent.py          # Entry point of the application
│   ├── adk
│   │   ├── __init__.py        # Marks the adk directory as a package
│   │   ├── adk_client.py      # Client for interacting with Google ADK services
│   │   └── config.py          # Configuration settings for the ADK client
│   ├── tools
│   │   ├── __init__.py        # Marks the tools directory as a package
│   │   ├── rule_agent_client.py# Functions for interacting with the local rule agent
│   │   ├── memory_client.py    # Functions for memory-related data storage
│   │   └── agent_tools.py      # Utility functions for agents
│   ├── agents
│   │   ├── __init__.py        # Marks the agents directory as a package
│   │   └── google_adk_agent.py # Defines the Google ADK agent
│   └── models
│       └── schemas.py         # Data models and schemas
├── tests
│   ├── test_main_agent.py     # Unit tests for main_agent.py
│   └── test_tools.py          # Unit tests for tools
├── requirements.txt            # Project dependencies
├── Dockerfile                  # Instructions for building a Docker image
├── .env.example                # Example environment variables
└── README.md                   # Project documentation
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd waste-management-adk-agent
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up environment variables by copying `.env.example` to `.env` and updating the values as needed.

## Usage
To run the application, execute the following command:
```
uvicorn src.main_agent:app --host 0.0.0.0 --port 8002
```

## API Endpoints
- **POST /waste-management/rules**: Retrieve waste management rules based on user queries.
- **POST /memory/store**: Store information in the memory service.

## Testing
To run the tests, use:
```
pytest
```

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.