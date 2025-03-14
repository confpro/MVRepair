# MVRepair

Data processing step. In this step, MVRepair builds the code SST based on the code AST. To reduce irrelevant semantic noise, MVRepair performs program slicing from points of interest in the program. To obtain comprehensive and precise program semantics, the code SST is also extended by the nodes directly connected to the key nodes for interprocedural analysis. MVRepair segments the code using the nodes of the code SST.
Model training step. In this step, MVRepair uses the multi-head attention mechanism to fuse the code SST and code information and uses ChatGPT to generate prompt templates for vulnerability type prediction to learn implicit vulnerability patterns. Then, the model after type prediction and the prompt template generated by ChatGPT are utilized by MVRepair to generate a trained model for fixing memory-related vulnerabilities.
Vulnerability repair step. Through interprocedural analysis, the AST of the target program is first constructed so that the code SST extraction can be carried out to capture the precise program semantics related to memory usage. Then, the code is segmented according to the key nodes to ensure that the model learns the complete code semantics. Then, the key code information and code segments were fed into the well-trained model.
![image](https://github.com/user-attachments/assets/f323ae5f-9d0e-42c7-837f-9f2d71e21423)
