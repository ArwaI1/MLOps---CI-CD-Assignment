import sys
import mlflow

# Read the Run ID from the artifact downloaded by GitHub Actions
with open("model_info.txt", "r") as f:
    run_id = f.read().strip()

# Fetch the run data from MLflow
run = mlflow.get_run(run_id)
accuracy = run.data.metrics.get("accuracy", 0.0)

print(f"Run ID: {run_id}, Accuracy: {accuracy}")

# Logic to fail the pipeline if accuracy is too low
if accuracy < 0.85:
    print("Error: Accuracy below 0.85 threshold. Failing the pipeline.")
    sys.exit(1)
else:
    print("Success: Accuracy meets threshold. Proceeding to deploy.")
    sys.exit(0)