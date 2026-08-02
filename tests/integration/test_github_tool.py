"""Integration tests for GitHubTool.

NOTE: this currently hits the live GitHub API. See issue #57 — these calls
should be replaced with a local mock server (pytest-httpserver) serving
fixtures from tests/fixtures/github_responses/, so the tests don't depend
on network access or GitHub's rate limits.
"""

import pytest

from agent.tools.github_tool import GitHubTool


@pytest.mark.integration
def test_fetches_real_repo_metadata() -> None:
    """Reproduction: exercises GitHubTool against the real GitHub API."""
    tool = GitHubTool()
    result = tool.execute({"github_username": "octocat", "repo_name": "Hello-World"})

    assert result.success
    assert result.data["name"] == "Hello-World"
