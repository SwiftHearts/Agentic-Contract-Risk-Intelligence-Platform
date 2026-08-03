#!/bin/bash

cd Src
python -m streamlit run agentic_contract_app.py --server.port 8000 --server.address 0.0.0.0
