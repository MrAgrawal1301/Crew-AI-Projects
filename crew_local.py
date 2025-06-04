from crewai import Crew , Process 
from agents_local import planner , writer , editor
from tasks_local  import plan , write , edit 



crew = Crew(
    agents=[planner, writer, editor],
    tasks=[plan, write, edit],
    verbose=True,
    process= Process.sequential
)



print("==> Starting Crew execution")


result = crew.kickoff(inputs={"topic": "Artificial Intelligence"} )


print("==> Crew finished. Result:")

print(result)


