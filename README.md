# SQL Query Agent: AI-Powered SQL Query Assistant

**SQL Query Agent** is an AI-powered tool designed to automate **SQL query generation** from natural language queries. Built using **LangChain**, **OpenAI API**, and **Python**, this tool allows users to input business-related questions in plain English. The tool then automatically translates these questions into **SQL queries** and interacts with databases to retrieve **real-time insights**, making data analysis accessible without requiring SQL knowledge.

## Features
- **Natural Language Processing (NLP)**: Uses **LangChain** and **OpenAI API** to convert natural language into SQL queries.
- **Database Integration**: Compatible with **MySQL**, **PostgreSQL**, and other SQL-based databases for seamless query execution.
- **Real-Time Insights**: Provides real-time data insights based on user input, enhancing decision-making.
- **User-Friendly**: No SQL knowledge required—just ask questions in plain English and get answers from the database.
- **AI-Powered Automation**: Streamlines data access and reporting by automating SQL query generation and execution.

## Technologies Used
- **LangChain**: A framework for building NLP-based applications, enabling the translation of user inputs into SQL queries.
- **OpenAI API**: Utilized for natural language understanding and translation into SQL syntax.
- **Python**: The primary programming language used for building the tool and integrating with databases.
- **MySQL & PostgreSQL**: The databases supported for query execution.
- **Flask**: A lightweight web framework used to develop the API that interfaces with the user.
- **Docker**: Containerized the application for easy deployment and scalability.

## Installation
To run the **SQL Query Agent**, follow the steps below:

1. Clone the repository:
    ```bash
    git clone https://github.com/NaviReddy369/SQL-QUERY-AGENT.git
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up your **OpenAI API key** in the environment variables:
    ```bash
    export OPENAI_API_KEY="your-openai-api-key"
    ```

4. Run the application:
    ```bash
    python app.py
    ```

## How to Use
1. Start the application, and you'll be prompted to input a question in **plain English**.
2. The tool will automatically convert your query into an **SQL query** and execute it on your connected database.
3. It will return the results in **real-time**, enabling fast and intuitive data exploration.

## Future Enhancements
- Support for additional databases (**SQL Server**, **SQLite**, etc.).
- Integrating **advanced AI models** for more complex queries.
- **Web interface** for more intuitive usage.
- Adding more **natural language capabilities** to understand a broader range of business queries.

## Contributing
Feel free to **fork** this repository, make changes, and submit **pull requests**. Contributions are welcome!

## License
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.
