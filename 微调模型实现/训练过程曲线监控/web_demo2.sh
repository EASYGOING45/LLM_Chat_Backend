#!/bin/bash
source activate py310_chat
streamlit run /root/ChatGLM3/basic_demo/web_demo_streamlit.py --server.enableCORS false --server.port 6006