# Snakemake executor plugin: google-batch

This is the [Google Batch](https://cloud.google.com/batch/docs/get-started) external executor plugin for snakemake.
For documentation, see the [Snakemake plugin catalog](https://snakemake.github.io/snakemake-plugin-catalog/plugins/executor/googlebatch.html).

### Notes

- Conda is used to install Snakemake and dependencies.
- The COS (container OS) uses the default Snakemake container, unless you specify differently.

For examples, look into the [examples](examples) directory.

### GCS storage plugin bootstrap

Each remote job installs a pinned GCS storage-plugin fork into Snakemake's
`.snakemake/pip-deployments` directory before source and input staging begins.
This replaces Snakemake's unpinned automatic storage-plugin deployment and makes
the concurrent large-object download implementation available during staging.
Override the pip requirement with `--googlebatch-storage-plugin-spec`; the default
is an exact commit archive from `deto/snakemake-storage-plugin-gcs`.

## Developer

The instructions for creating and scaffolding this plugin are [here](https://github.com/snakemake/poetry-snakemake-plugin#scaffolding-an-executor-plugin).
Instructions for writing your plugin with examples are provided via the [snakemake-executor-plugin-interface](https://github.com/snakemake/snakemake-executor-plugin-interface).


## License

HPCIC DevTools is distributed under the terms of the MIT license.
All new contributions must be made under this license.

See [LICENSE](https://github.com/converged-computing/cloud-select/blob/main/LICENSE),
[COPYRIGHT](https://github.com/converged-computing/cloud-select/blob/main/COPYRIGHT), and
[NOTICE](https://github.com/converged-computing/cloud-select/blob/main/NOTICE) for details.

SPDX-License-Identifier: (MIT)

LLNL-CODE- 842614
