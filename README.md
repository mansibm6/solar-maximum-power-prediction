# Photovoltaic maximum-power regression

Compares raw-input and normalized dense regressors for photovoltaic maximum power Pmax.

## Setup and execution

Use Python 3.11 and a separate virtual environment for this project. Run commands from this folder:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python check_inputs.py
python -m jupyterlab
```

On Windows, activate with `.venv\Scripts\activate`. For notebooks, select this environment’s kernel and execute from the top in a fresh kernel. The first code cell exposes `INPUT_PATHS` where old machine-specific paths existed. `PROJECT_DATA_DIR` changes the base for those configured paths; remaining relative paths use the notebook working directory.

## Notebooks

- [MPPT_Prediction.ipynb](MPPT_Prediction.ipynb)

## Inputs

No fixed external dataset is required for the default entry point. See the notes below for bundled files or command-line input requirements.

## Outputs

Two in-memory regression models, loss plots, and scaled/unscaled predictions.

## Implementation and limitations

MPPT Prediction PV Data.csv is bundled and now used by default. Expected predictors include V1, P, G, Vopt; target is Pmax. Original fixed normalization constants and model architectures are retained. Random splits and TensorFlow kernels can change exact metrics between runs.

Reusable model/analysis functions live in `experiment_mppt_prediction.py`. Notebooks retain the experiment sequence, training, and visual narrative.

## Verification

The workspace regression suite checks source/notebook validity and selected behavior with bundled or synthetic inputs. Full experiment training and historical metric reproduction are not implied. See the workspace `REFACTOR_REPORT.md` for exact test coverage and unresolved runtime requirements.
