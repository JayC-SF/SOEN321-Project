# SOEN-321 Project: Jailbreak LLMs Project

## Purpose  
This project is focused on developing tools and methods to detect and analyze attempts to jailbreak Large Language Models (LLMs). By identifying patterns and techniques used in jailbreak attempts, we aim to enhance the security and reliability of LLMs, ensuring they adhere to ethical and operational constraints.

## Features  
- Detection of prompt engineering techniques used to bypass restrictions.  
- Analysis of vulnerabilities in LLMs that enable jailbreaks.  
- Logging and reporting system for potential jailbreak attempts.  

## WARNING  
Due to the nature of this project, jailbreaking LLMs can lead to the generation of outputs that violate the LLMs' own guidelines. This may include:  
- Strong or offensive language.  
- Slurs or discriminatory remarks.  
- Descriptions of violent behaviors or dangerous activities.  
- Harmful instructions, such as dangerous recipes or actions.  

## Installation  
Follow these steps to set up the project environment. The recommended Python version is 3.11.0 or above.

1. Upgrade `pip` to the latest version:  
   ```bash
   python.exe -m pip install --upgrade pip
   ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Create a .env file to store your LLM API keys. Add the following line, replacing {your_API_KEY} with your actual API key:
    `GEMINI_KEY={your_API_KEY}`

## Team Members:

- Juan-Carlos Sreng-Flores – 40101813
- Lucas Miquet-Westphal - 40215325
- Daniel Lam – 40248073
- Mohammed Rahman - 40203098
- Rihazul Islam - 40212505
- Sathurthikan Saththyvel 40213455
- Walid Achlaf - 40210355



