import os
import click
from github import Github
from dotenv import load_dotenv


@click.command()
@click.option('--user_name', default='TessFerrandez')
@click.option('--repository_name', default='actionsdemo')
@click.option('--workflow_name', default='GitHub Actions Demo')
def main(user_name: str, repository_name: str, workflow_name: str):
    github_token = os.environ.get('GITHUB_TOKEN')

    git = Github(github_token)
    user = git.get_user(user_name)
    repo = user.get_repo(repository_name)
    workflow = next(wf for wf in repo.get_workflows() if wf.name == workflow_name)

    # start a run by sending a dispatch
    result = workflow.create_dispatch(ref='main', inputs={})
    print(f'STARTED WORKFLOW RUN: {result}')


if __name__ == "__main__":
    load_dotenv()
    main()
