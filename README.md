# Sample to show how to run workflows

You can trigger a workflow run from code by running 

```cmd
python src\run_workflow.py
```

The workflow run is super simple, but at the end it will commit back the status of the previous steps to the INFO.txt file

> Note: You need a github secret GH_TOKEN containing your repo personal access token and a .env file with the contents

```text
GITHUB_TOKEN=yourtoken
```
