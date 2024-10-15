# %%
from config import config
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.globals import set_debug

model = ChatOpenAI(model="gpt-4o-mini", api_key=config.API_KEY)

# %%
messages = [
    SystemMessage(
        content="You are a great translator. When text is input, you translate it from English to Japanese and output it."
    ),
    HumanMessage(content="hi!"),
]
ret = model.invoke(messages)
print(f"ret: {ret}\t type: {type(ret)}")

# %%
from langchain_core.output_parsers import StrOutputParser

pt = ChatPromptTemplate.from_messages(
    [
        SystemMessage(
            content="You are a great translator. When text is input, you translate it from English to Japanese and output it."
        ),
        HumanMessagePromptTemplate.from_template(template="input: {text}"),
    ]
)
parser = StrOutputParser()

chain = pt | model | parser

set_debug(True)
ret = chain.invoke({"text": input("Enter text to translate: ")})
print(f"ret: {ret}\t type: {type(ret)}")

# %%
