# Sample to show how to run workflows from code

Clone this repository to your own github user and change the defaults in `src\run_workflow.py`

You can trigger a workflow run from code by running 

```cmd
python src\run_workflow.py
```

The workflow run is super simple, but at the end it will commit back the status of the previous steps to the INFO.txt file

> Note: You need a github secret GH_TOKEN containing your repo personal access token (this is to commit back to the repo) and a .env file with the following contents... the latter is used when we trigger the workflow run

```text
GITHUB_TOKEN=yourtoken
```
