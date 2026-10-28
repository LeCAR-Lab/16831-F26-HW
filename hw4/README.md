## Setup

You can run this code on your own machine or on Google Colab. 

1. **Local option:** Reuse the `rob831` environment from HW3; no new environment is needed. If you have not set it up, see the [HW3 setup instructions](../hw3/README.md). From the HW4 folder, run:

   ```bash
   conda activate rob831
   cd <path_to_16831-F26-HW>/hw4
   python -m pip install -r requirements.txt
   python -m pip install -e .
   ```

   **Optional Linux GPU setup:** If training fails with `CUDA error: no kernel image is available for execution on the device` on an NVIDIA Ampere or Ada GPU (such as an RTX 3090 or RTX 6000 Ada), install the CUDA 11.6 build of PyTorch in the same environment after the commands above:

   ```bash
   python -m pip install --upgrade "torch==1.12.1+cu116" --extra-index-url https://download.pytorch.org/whl/cu116
   ```

   Then rerun training. This keeps PyTorch at version 1.12.1 while replacing its CUDA build.

2. **Colab:** Before running the setup cells, select **Runtime → Change runtime type**, set **Runtime version** to **2025.07** and **Hardware accelerator** to **T4 GPU**, then save. The first few sections of the notebook will install all required dependencies. Open the notebook using the badge below:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LeCAR-Lab/16831-F26-HW/blob/main/hw4/rob831/hw4_part1/scripts/run_hw4_mb.ipynb) **Model Based Learning**

If Colab asks you to restart after installing dependencies, restart the session, re-run the setup cells upto the clone homework repo cell. In that cell, comment the repository cloning and requirements installation commands. Do:

```
%cd $SYM_PATH
# !git clone https://github.com/LeCAR-Lab/16831-F26-HW.git
%cd 16831-F26-HW/hw4
# %pip install -r requirements_colab.txt
%pip install -e .
```

Continue with **set up virtual display**. You do not need to clone the repository or reinstall the requirements after this restart.

## Complete the code

The following files have blanks to be filled with your solutions from homework 1. The relevant sections are marked with `TODO: get this from Piazza'.

- [rob831/hw4_part1/infrastructure/rl_trainer.py](rob831/hw4_part1/infrastructure/rl_trainer.py)
- [rob831/hw4_part1/infrastructure/utils.py](rob831/hw4_part1/infrastructure/utils.py)

You will then need to implement code in the following files:
- [rob831/hw4_part1/agents/mb_agent.py](rob831/hw4_part1/agents/mb_agent.py)
- [rob831/hw4_part1/models/ff_model.py](rob831/hw4_part1/models/ff_model.py)
- [rob831/hw4_part1/policies/MPC_policy.py](rob831/hw4_part1/policies/MPC_policy.py)
- [rob831/hw4_part1/infrastructure/rl_trainer.py](rob831/hw4_part1/infrastructure/rl_trainer.py)

The relevant sections are marked with `TODO`.

You may also want to look through [scripts/run_hw4_mb.py](rob831/hw4_part1/scripts/run_hw4_mb.py) (if running locally) or [scripts/run_hw4_mb.ipynb](rob831/hw4_part1/scripts/run_hw4_mb.ipynb) (if running on Colab), though you will not need to edit this files beyond changing runtime arguments in the Colab notebook.

See the [assignment PDF](hw4.pdf) for more details on what files to edit.
