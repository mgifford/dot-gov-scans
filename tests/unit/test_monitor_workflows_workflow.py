"""Tests for the Monitor Workflow Health workflow."""

from pathlib import Path

import yaml


_WORKFLOW_PATH = Path(".github/workflows/monitor-workflows.yml")


def _load_workflow() -> dict:
    raw = yaml.safe_load(_WORKFLOW_PATH.read_text(encoding="utf-8"))
    # YAML parses bare `on:` as Python True; normalise to the string "on".
    if True in raw and "on" not in raw:
        raw["on"] = raw.pop(True)
    return raw


def test_monitor_workflows_workflow_exists() -> None:
    """The monitor-workflows.yml file should exist."""
    assert _WORKFLOW_PATH.exists(), "monitor-workflows.yml is missing"


def test_monitor_workflows_triggers_on_workflow_run() -> None:
    """Monitoring workflow must react to workflow_run completion events."""
    content = _WORKFLOW_PATH.read_text(encoding="utf-8")
    assert "workflow_run" in content
    assert "completed" in content


def test_monitor_workflows_watches_key_scan_workflows() -> None:
    """Monitoring workflow must watch all key scanning and deployment workflows."""
    workflow = _load_workflow()
    watched = workflow["on"]["workflow_run"]["workflows"]
    expected = {
        "Scan Social Media Links",
        "Scan Accessibility Statements",
        "Scan Technology Stack",
        "Scan Lighthouse",
        "Generate Scan Progress Report",
        "Deploy GitHub Pages",
    }
    for name in expected:
        assert name in watched, f"Missing watched workflow: {name}"


def test_monitor_workflows_has_issues_write_permission() -> None:
    """Monitoring workflow must have issues: write permission to create alerts."""
    workflow = _load_workflow()
    permissions = workflow.get("permissions", {})
    assert permissions.get("issues") == "write", (
        "monitor-workflows.yml must have 'issues: write' permission"
    )


def test_monitor_workflows_job_runs_only_on_failure() -> None:
    """The notify-on-failure job should only run when a workflow fails."""
    content = _WORKFLOW_PATH.read_text(encoding="utf-8")
    assert "workflow_run.conclusion == 'failure'" in content


def test_monitor_workflows_creates_or_updates_issue() -> None:
    """The alert step must create a new issue or comment on an existing one."""
    content = _WORKFLOW_PATH.read_text(encoding="utf-8")
    assert "gh issue create" in content
    assert "gh issue comment" in content
    assert "workflow-failure" in content


def test_monitor_workflows_posts_failure_summary() -> None:
    """The monitoring workflow should write a summary to the Actions step summary."""
    content = _WORKFLOW_PATH.read_text(encoding="utf-8")
    assert "GITHUB_STEP_SUMMARY" in content
    assert "Workflow Failure Detected" in content


def test_monitor_workflows_includes_run_url_in_issue() -> None:
    """Failure issues must link back to the failing workflow run."""
    content = _WORKFLOW_PATH.read_text(encoding="utf-8")
    assert "workflow_run.html_url" in content
    assert "RUN_URL" in content


def test_monitor_workflows_has_workflow_dispatch_for_testing() -> None:
    """Monitoring workflow should allow manual dispatch for testing the alert path."""
    workflow = _load_workflow()
    assert "workflow_dispatch" in workflow["on"]
