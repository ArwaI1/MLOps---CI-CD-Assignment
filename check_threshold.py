import sys
import mlflow

with open("model_info.txt", "r") as f:
    run_id = f.read().strip()

# Fetch from DagsHub
run = mlflow.get_run(run_id)
accuracy = run.data.metrics.get("accuracy", 0.0)

print(f"Run ID: {run_id}, Accuracy: {accuracy}")

if accuracy < 0.85:
    print("Error: Accuracy below 0.85 threshold. Failing the pipeline.")
    sys.exit(1)
else:
    print("Success: Accuracy meets threshold. Proceeding to deploy.")
    sys.exit(0)