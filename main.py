from langchain import PromptTemplate, SQLDatabase, SQLDatabaseChain
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain 

import os
os.environ["OPENAI_API_KEY"] = ""

# _DEFAULT_TEMPLATE = """Given an input question, first create a syntactically correct SQL query to run, then look at the results of the query and return the answer.
# Use the following format:

# Question: "Question here"
# Answer: "Final answer here"

# Only use the following tables:

# {table_info}

# Question: {input}"""

# PROMPT = PromptTemplate(
#     input_variables=["input", "table_info"], template=_DEFAULT_TEMPLATE
# ).partial(table_info="Employee, Album, Customer")

db = SQLDatabase.from_uri("sqlite:///./Chinook_Sqlite.sqlite")

llm = ChatOpenAI(
    temperature=0,
    verbose=True
)

chain = SQLDatabaseChain(llm=llm, database=db)

def user_typed_prompt(query):
    result = chain.run(query)
    print(result)

    