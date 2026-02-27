### Initial Setup
1. Install miniconda on your machine: <a href="https://www.anaconda.com/docs/getting-started/miniconda/install">Miniconda Installation Doc</a>
2. Create a conda env `conda create -n <env-name>`
3. Select the env `conda activate <env-name>`
4. Now intall python-freethreading `conda install python-freethreading`
5. Test the GIL status with `python 0_gil_test.py`
6. To understand more about GIL in python and freethreading, watch this video: <a href="https://youtu.be/m4zDBk0zAUY?si=HHLL_QQLilFUBC0_">Youtube-Lex-Fredman-&-Guido-Van-Rossum</a>
7. Install uv `pip install uv` and initialize repo `uv init --python 3.13`
8. Why `python 3.13`? Answer: free-threading has just started yet. So, libraries are yet to implement the freethreaded version.