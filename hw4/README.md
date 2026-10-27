## Setup

You can run this code on your own machine or on Google Colab. 

1. **Local option:** Reuse the `rob831` environment from HW3; no new environment is needed. If you have not set it up, see the [HW3 setup instructions](../hw3/README.md). From the HW4 folder, run:

   ```bash
   conda activate rob831
   cd <path_to_16831-F26-HW>/hw4
   python -m pip install -r requirements.txt
   python -m pip install -e .
   ```

2. **Colab:** The first few sections of the notebook will install all required dependencies. You can try out the Colab option by clicking the badges below:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LeCAR-Lab/16831-F26-HW/blob/main/hw4/rob831/hw4_part1/scripts/run_hw4_mb.ipynb) **Model Based Learning**


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
