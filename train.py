import os
import mlflow

# We use an environment variable so you can easily change accuracy in the YAML for screenshots
accuracy = float(os.getenv("MOCK_ACCURACY", 0.90))

with mlflow.start_run() as run:
    mlflow.log_metric("accuracy", accuracy)
    
    # Export the Run ID to a text file
    with open("model_info.txt", "w") as f:
        f.write(run.info.run_id)

print(f"Logged accuracy: {accuracy} with Run ID: {run.info.run_id}")