## Reinforcement Learning
- Solve interactive problems
    . agent interacts with the environment and environment send reward or penalty signals to the agent this helps the agent to improve its performance

- it can be considered related to supervised learning although the feedback is not the ground through, but a indirect measure of how well the action was measured based on the final goal
- In reinforcement learning the feed back can be either immediate or via dekayed feedback

## Unsupervised Learning
- we are trying to find some how some structure in the data
### Clustering (Finding subgroups) 
    - members of each cluster are share a similarity to each others. and dissimilar to objects in the other clusters

### Dimentionality reduction for data compression
    - used in feature preprocessing to remove noise
        . noise can degrade the predictive performace of many algorithms
    - Dimentionality reduction compresses the data onto a smaller dimensional subspace while retaining most of the relevent information.
    
    - it can be useful for visualizing data

# Terminology and notations
    meuserments and properties -> features
    i to refers to ith training example 
    j to refers to jth dimention of the training dataset 
## ML terminology
    - Training example: A row in a table :
        observation, record, instance
    - Training
    - Feuture, abbrev x.
        A columnt in a data (preductorm variable, input, attribute, covariate)
    - Target, abbrev. y 
    (outcome, output, dependent variable, (class)lable, ground truth)
    - Loss function 
    cost function, error

# Roadmap
1. Raw data collection
    a. preprocessing pipeline 1:
        Missing data handling, 
        Initial Data Cleaning
        Initial feature extaction and selection
2. Data Set 
    a. devide data to Training and Test dataset
3. Training dataset
    a. Preprocessing pipeline 2:
        . Feature scaling
        . Dimentionality reduction
            . Feature selection
            . Feature extraction
4. Processed training dataset
5. Machine learing algorithm
    a. Hyperparameter choice + training
6. Predictive model candidate
7. Iterate and evaluate via cross-validation and go back to step 3
8. Final predictive model 
    a. Evaluate the test 
9. Test dataset
    goes through 3.a
    a. Evaluated

10. New dataset
    goes through 1.a and 3.a
    and predict

# 1.a Preprocessing 
    remove unrelated information
    cleaning and dimentional reduction
# 5 Training and selectin a model
    by definition each model and classification a:lgorithm has its inherent biases. (A model needs to make some assumptions to be a model!)
## Metrics:
    - Accuracy
        . proportion of correctly classified instances
    - precision
    -others

