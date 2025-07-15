import os
import pathlib
import subprocess
from datetime import datetime
from typing import Type, List, Optional
from mcp import Tool
from chirpn_mcp.utils.github_helper import GithubHelper
from chirpn_mcp.utils.get_config import load_yaml
from chirpn_mcp.utils.logger import logger
from chirpn_mcp.schemas.schemas import github_push_tool_schema

class GithubPushTool(Tool):    
    """Tool to push changes to the Github Repository."""
    
    name: str = "GithubPushTool"
    description: str = "Push changes made in the local to the github repository."
    inputSchema: dict = github_push_tool_schema

    def execute(self, base_branch: str, commit_message: str, file_path: List[str], repo_name: str, repo_owner: str) -> str:
        try:
            result = self._run(base_branch, commit_message, file_path, repo_name, repo_owner)
            return result
        except Exception as e:
            return f"[ERROR] Tool crashed: {str(e)}"

    def _run(self, base_branch : str, commit_message : str, file_path : List[str], repo_name:str, repo_owner:str) -> str:

        try:
            github_access_token = load_yaml("GITHUB_ACESS_TOKEN")
            github_username = load_yaml("GITHUB_USERNAME")
            fork = 0
            github_helper = GithubHelper(github_access_token, github_username)
            head_branch = '-'.join(commit_message.split()[:2]) # new branch name
            timestamp = datetime.now().strftime("%Y%m%d-%H%M")  # Format: YYYYMMDD-HHMMSS , adding timestamp to branch
            head_branch = f"{head_branch}-{timestamp}"
            head_branch = github_helper.sanitize_branch_name(head_branch)
            logger.info(f'head branch - {head_branch}')

            headers = {
                    "Authorization": f"token {github_access_token}" if github_access_token else None,
                    "Content-Type": "application/vnd.github+json"
                }
            if repo_owner != github_username:
                fork = 1
                logger.info(f'Creating a fork of the repository {repo_owner}/{repo_name} for user {github_username}')
                fork_response = github_helper.make_fork(repo_owner, repo_name, base_branch, headers)
            
            branch_response = github_helper.create_branch(repo_owner, repo_name, base_branch, head_branch, headers)
            logger.info(f"branch response -- {branch_response}")
            
            for file in file_path:
                if fork == 1:
                    repo_owner = github_username # change in our forked repo
                file_response = github_helper.add_file(repo_owner, repo_name, file,
                                                        head_branch, base_branch, headers, commit_message)
                logger.info(f"file response -- {file_response}")

            pr_response = github_helper.create_pull_request(repo_owner, repo_name, head_branch, base_branch, headers)
            logger.info(f"pr response -- {pr_response}")

            message = pr_response.get("message", "").lower()
            pr_url = pr_response.get("pr_url")

            if "pull request created" in message or "already existing pull request" in message:
                if pr_url:
                    return {
                        "Pull request added. Url of Pull Request": pr_url
                    }
                else:
                    return {"message": "Pull request created, but no URL returned."}

            return {"message": f"Failed to create pull request: {pr_response.get('error', 'Unknown error')}"}
        
        except Exception as err:
            return f"Error: Unable to add file/folder to repository {err}"


         

if __name__ == "__main__":
    # Example usage
    tool = GithubPushTool()
    result = tool.execute('main','testing-push', ['chirpn_mcp/tools/github_tools/github_push.py'], 'superagi_try','toheedakhtar',)
    logger.info(result)