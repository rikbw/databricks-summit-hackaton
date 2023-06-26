from langchain import SQLDatabase, SQLDatabaseChain
from langchain.chat_models import ChatOpenAI
from langchain import LLMChain, PromptTemplate
from IPython.display import display, HTML
import os

os.environ["OPENAI_API_KEY"] = "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"

db = SQLDatabase.from_uri("sqlite:///./Chinook_Sqlite.sqlite")

llm = ChatOpenAI(
    model="gpt-3.5-turbo-16k",
    temperature=0,
    verbose=True
)

db_chain = SQLDatabaseChain.from_llm(llm=llm, db=db, top_k=5)


# Explain chain (adds context to response from SQL chain)

_PROMPT_TEMPLATE = """You are an expert in communication. Your job is to inform Data Analysts about the schema and data in a SQL database.

Given the following response to a user's question, create a new response to the same question that is more informative.

Provide a structured response. The new response should be in an HTML format. Use tables where appropriate.

Question: {question}
Response: {response}

New Response:"""

PROMPT = PromptTemplate(
    input_variables=["question", "response"],
    template=_PROMPT_TEMPLATE,
)
explain_chain = LLMChain(
    llm=ChatOpenAI(
        model="gpt-3.5-turbo-16k",
        temperature=0.7
    ),
    prompt=PROMPT
)


# Final function
def user_typed_prompt(question):
    #print("Question", question)
    response = db_chain.run(question)
    #print("Response", response)
    final_result_html = explain_chain.run(
        question=question,
        response=response,
    )
    # print("Final Result", final_result_html)
    return display(HTML(final_result_html))

    