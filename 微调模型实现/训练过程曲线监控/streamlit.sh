#!/bin/bash
cd /root/ChatGLM3/composite_demo
source activate py310_chat
streamlit run main.py --server.enableCORS false --server.port 6006