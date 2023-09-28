import os
import openai

# Check data formatting 
# https://cookbook.openai.com/examples/chat_finetuning_data_prep

def fine(objeto):
    objeto = objeto
    print (f"ENTRANDO FINE OBJETO = {objeto}")
    """openai.api_key = os.getenv("OPENAI_API_KEY") # Chave openai
    openai.File.create(
    file=open("mydata.jsonl", "rb"),
    purpose='fine-tune'
    )

    #Create a fine-tuned model
    openai.FineTuningJob.create(training_file="file-abc123", model="gpt-3.5-turbo") # Colocar o nome da persona do GPT ?

    # In addition to creating a fine-tuning job, you can also list existing jobs, retrieve the status of a job, or cancel a job.

    # List 10 fine-tuning jobs
    openai.FineTuningJob.list(limit=10)

    # Retrieve the state of a fine-tune
    openai.FineTuningJob.retrieve("ft-abc123")

    # Cancel a job
    openai.FineTuningJob.cancel("ft-abc123")

    # List up to 10 events from a fine-tuning job
    openai.FineTuningJob.list_events(id="ft-abc123", limit=10)

    # Delete a fine-tuned model (must be an owner of the org the model was created in)
    openai.Model.delete("ft-abc123")

    #Use a fine-tuned model -> Acho que é só ua alternativa
    completion = openai.ChatCompletion.create(
    model="ft:gpt-3.5-turbo:my-org:custom_suffix:id",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ]
    )
    print(completion.choices[0].message)

"""

# Invocando funcao fine

#fine(objeto = None)