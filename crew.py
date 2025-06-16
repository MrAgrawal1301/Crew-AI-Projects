import os
from crewai import Crew
from agents import planner , writer , editor
from tasks  import plan , write , edit 

from dotenv import load_dotenv
#want more changes 

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = os.getenv("OPENAI_MODEL_NAME")

crew = Crew(
    agents=[planner, writer, editor],
    tasks=[plan, write, edit],
    verbose=True
)

print("==> Starting Crew execution")

result = crew.kickoff(inputs={"topic": "Artificial Intelligence"})

print("==> Crew finished. Result:")

print(result)
