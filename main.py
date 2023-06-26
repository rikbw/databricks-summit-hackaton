from langchain import PromptTemplate, SQLDatabase, SQLDatabaseChain
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain 
from langchain import LLMChain, PromptTemplate

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

db_chain = SQLDatabaseChain(llm=llm, database=db, top_k=5)


# Explain chain (adds context to response from SQL chain)

_PROMPT_TEMPLATE = """You are an expert in communication. Your job is to inform Data Analysts about the schema and data in a SQL database.

Given the following response to a user's question, create a new response to the same question that is more informative.

Question: {question}
Response: {response}

New Response:"""

PROMPT = PromptTemplate(
    input_variables=["question", "response"],
    template=_PROMPT_TEMPLATE,
)
explain_chain = LLMChain(llm=llm, prompt=PROMPT)


# Final function
def user_typed_prompt(question):
    print("Question", question)
    response = db_chain.run(question)
    print("Response", question)
    final_result = explain_chain.run(
        question=question,
        response=response,
    )
    print("Final Result", final_result)
    return final_result

    