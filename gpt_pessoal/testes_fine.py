import json
import os
import openai
openai.api_key = ("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")
op = openai.File.create(
  file=open("dados.jsonl", "rb"),
  purpose='fine-tune'
)
# Minimo 10 linhas para finetuning
print(op)
openai.FineTuningJob.create(training_file=op.get("id"), model="gpt-3.5-turbo")