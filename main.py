from langchain import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain 

_DEFAULT_TEMPLATE = """Given an input question, first create a syntactically correct SQL query to run, then look at the results of the query and return the answer.
Use the following format:

Question: "Question here"
Answer: "Final answer here"

Question: {input}"""

PROMPT = PromptTemplate(
    input_variables=["input"], template=_DEFAULT_TEMPLATE
)

# db = SQLDatabase.from_uri("sqlite:///./Chinook_sqlite.db")

llm = OpenAI(temperature=0, verbose=True)

chain = LLMChain(llm=llm, prompt=PROMPT)

def user_typed_prompt(prompt):
    print("This is data about <insert table information here>!")
    result = db_chain.run(prompmt)
    
