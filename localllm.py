# # Use a pipeline as a high-level helper
# from langchain.llms.huggingface_pipeline import HuggingFacePipeline
# from crewai import LLM

# hf = HuggingFacePipeline.from_model_id(
#     model_id="microsoft/DialoGPT-medium", task="text-generation", pipeline_kwargs={"max_new_tokens": 200, "pad_token_id": 50256},
# )
# i thik you should start learning that hf also
# llm = LLM(
#     model=hf
# )

