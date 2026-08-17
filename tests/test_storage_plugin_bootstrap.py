import shlex

import pytest
from snakemake_interface_common.exceptions import WorkflowError

from snakemake_executor_plugin_googlebatch import (
    DEFAULT_GCS_STORAGE_PLUGIN_SPEC,
    ExecutorSettings,
    common_settings,
)
from snakemake_executor_plugin_googlebatch.executor import (
    PIP_DEPLOYMENTS_PATH,
    get_storage_plugin_bootstrap,
)


def test_storage_plugin_default_is_exact_commit():
    settings = ExecutorSettings(project="test", region="us-central1")

    assert settings.storage_plugin_spec == DEFAULT_GCS_STORAGE_PLUGIN_SPEC
    assert "b77bc2cece5cad1fa0d367270accde5ec4480666" in settings.storage_plugin_spec


def test_core_storage_plugin_auto_deployment_is_disabled():
    assert common_settings.auto_deploy_default_storage_provider is False


def test_bootstrap_installs_into_snakemake_deployment_directory():
    spec = "snakemake-storage-plugin-gcs @ https://example.test/plugin.zip"

    command = get_storage_plugin_bootstrap(spec)

    assert f"--target {PIP_DEPLOYMENTS_PATH}" in command
    assert shlex.quote(spec) in command
    assert "PYTHONPATH=.snakemake/pip-deployments" in command
    assert "import snakemake_storage_plugin_gcs as plugin" in command


def test_bootstrap_rejects_empty_override():
    with pytest.raises(WorkflowError, match="storage_plugin_spec"):
        get_storage_plugin_bootstrap("")
