# dpmt2trello

- Dumps DPMT projects to Trello. 
- The goal is to have a better user interface for selecting the project. 
- All of this **code is dirty shit** that should have never been written. Sorry.
- It might not work for you. Sorry. Try debugging it.



# Setting up

0. Clone this repository ``git clone https://github.com/Visgean/dpmt2trello.git``
1. Login to https://dpmt.inf.ed.ac.uk/
2. Copy the cookies to a new file ``cookie.txt`` in the same repository. The content of the file should be similar to file ``cookie_example.txt``.
3. Get your API keys for trello - https://trello.com/app-key
4. Export keys to shell:

    ```
    export TRELLO_API_KEY=asxasx
    export TRELLO_API_SECRET=asxjasxnjasnx
    export PROJECT_NAME=minf_project
    ```
5. Install requirements: ``pip3 install -r requirements.txt``
6. run ``python3 dump2trello.py``
    - the script will report any projects for which adding failed, add these manually.
7. the script will save all projects that it added - therefore you should run it every few days after people add new projects, you will likely need to get new cookie though.