from langchain.llms import OpenAI
import os
from mygetpass import get_file_contents



os.environ["OPENAI_API_KEY"] = get_file_contents("openai_api_key.secret")
#export OPENAI_API_KEY="..." in terminal



llm = OpenAI(temperature=0.9)
text = "What would be a good company name for a company that makes AI youtube video?"
print(llm(text))