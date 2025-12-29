Installation
============

Clone the repository:

.. code-block:: bash

   git clone https://github.com/your-username/cine-to-nerdle.git
   cd cine-to-nerdle

Create a virtual environment:

.. code-block:: bash

   python -m venv .venv
   source .venv/bin/activate

Install dependencies:

.. code-block:: bash

   pip install -r requirements.txt

Now we need to download the backing dataset. The dataset is supplied by kaggle,
and therefore you will need to go to kaggle and register for an account.
After this has been completed, please go to settings and generate an API Key.

Next you will need to create a file called ``kaggle_tokens.ini`` (within the game_data
directory) and add your API Key to the file as below

.. code-block:: plaintext

   KAGGLE_API_TOKEN=<your_token_goes_here>

Next please run all code blocks in ``kaggle_load.ipynb`` to generate the backing datasets.
You should see **film_actors.parquet** and **film_dataset.parquet** after this.

You are now ready to play the game!
