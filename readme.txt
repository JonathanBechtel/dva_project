## DESCRIPTION

This repository features the codebase used to develop the minimum-spanning-trees used to explore the crypto data, model the relationships, and cluster accordingly using minimum spanning trees.

This codebase features three key components:
* Data ingest (Python)
* Modelling scripts (Python)
* UI/Frontend (Javascript)

## INSTALLATION 

1. git clone https://github.com/JonathanBechtel/dva_project.git
2. Create python 3.10 environment (i.e. conda create --name mst_tree_project python=3.10.8)
3. Within activated python 3.10 environment, install python packages: pip -r requirements.txt

## EXECUTION

To execute the web-based frontend/UI:

1. Within command prompt/terminal, change to the /web directory within the cloned git repo. 
2. Execute the following command to start a local python webserver: python -m http.server (may be python3 rather than python)
3. Navigate to a http://localhost:8000 within a browser (tested with Chrome)
4. For the 3d force-directed graph of the minimum-spanning-trees, click 3d-FDG.html
5. Navigate by clicking any individual node, clicking & dragging, etc

To replicate the data ingest:
1. Execute /script/crypto_data.py with python to obtain crypto data from block.cc w/an appropriate API key

To replicate the modeling via the MST (correlation-based and dynamic-time-warping-based):
1. Navigate to /notebooks/ directory
2. Open "MST - Second Go.ipynb" within a jupyterlab/notebook environment
3. Execute the notebook to generate the following outputs: corr_graph.csv & dtw_graph.csv
4. To convert these outputs to json (as used by the web frontend):
    1. execute: python /web/toJson.py
6. To generate the analysis of the MSTs (correlation-based and dynamic-time-warping-based):
    1. Open "DTW-Corr Metrics.ipynb" within a jupyterlab/notebook environment
    2. Execute the notebook to generate analysis of the two MST approaches in terms of modelling the crypto price/return relationships over time
    3. Open "Clustering & Visualization With DTW.ipynb" within a jupyterlab/notebook environment
    4. Execute the notebook to generate clusters based on the two MST approaches as well as cluster visualizations

