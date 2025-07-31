 python -m venv venv
 venv\Scripts\Activate

 pip install -r requirements.txt

 pip install langchain
 pip install google-generativeai
 pip install langchain-google-genai   //not necessory
 pip install langchain-huggingface huggingface_hub
 pip install transformers 
 pip install numpy scikit-learn  
 pip install python-dotenv 

 pip freeze > requirements.txt 



***Remove .env from Git Tracking***
```
git rm --cached .env
```

***Add .env to .gitignore***
```
.env
```

***Commit the Change***
```
git commit -m "Remove .env file from repository"

git push origin main
```
```
```


***05_chatmodel_hf_local.py***
# Not recommanded
for running hugging face model locally
```
pip install torch  
```

