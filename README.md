# MVRepair

![image](https://github.com/user-attachments/assets/9382700f-a4e8-4658-8483-349e6ade1e07)


# dataset
![image](https://github.com/user-attachments/assets/a2841fd6-ca10-4631-8e97-ade3d05e48c2)



# Data processing step. 

In this step, MVRepair builds the code SST based on the code AST. To reduce irrelevant semantic noise, MVRepair performs program slicing from points of interest in the program. To obtain comprehensive and precise program semantics, the code SST is also extended by the nodes directly connected to the key nodes for interprocedural analysis. MVRepair segments the code using the nodes of the code SST.

# Model training step. 

In this step, MVRepair uses the multi-head attention mechanism to fuse the code SST and code information and uses ChatGPT to generate prompt templates for vulnerability type prediction to learn implicit vulnerability patterns. Then, the model after type prediction and the prompt template generated by ChatGPT are utilized by MVRepair to generate a trained model for fixing memory-related vulnerabilities.

# Vulnerability repair step. 

Through interprocedural analysis, the AST of the target program is first constructed so that the code SST extraction can be carried out to capture the precise program semantics related to memory usage. Then, the code is segmented according to the key nodes to ensure that the model learns the complete code semantics. Then, the key code information and code segments were fed into the well-trained model.


# RQ1: Effectiveness of MVRepair
![image](https://github.com/user-attachments/assets/74f1b9fa-98bf-4cce-be27-c8ff640e09d4)



# RQ2: Effectiveness of SST-Segmentation on Other ℓLM Models

![image](https://github.com/user-attachments/assets/608973f3-095f-43d0-bafb-4c026ffc617a)


# RQ3: Influences of Design Choices

![image](https://github.com/user-attachments/assets/e38cfdd2-e736-44f4-af07-6c80c06cc6fd)


# RQ4: Influences of Hyper-paramaters
![image](https://github.com/user-attachments/assets/d78764a6-ccd1-450c-b5b1-1d192d949bdd)


# Dis:

# Effectiveness of CWE-type
![image](https://github.com/user-attachments/assets/e9360903-df87-4407-b502-f47e340f5587)

![image](https://github.com/user-attachments/assets/a8c56db9-9583-4329-80a3-fe0122d633a5)


# Applicability of MVRepair
![image](https://github.com/user-attachments/assets/699c6dfd-72ed-4105-8866-b14309c3a588)


# The impact of different prompts
![image](https://github.com/user-attachments/assets/7475598d-f80c-42fb-b5d7-41c50f0ae648)

