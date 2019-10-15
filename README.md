# NLP-Project

## papers
1. Show, Attend and Tell : https://arxiv.org/pdf/1502.03044v2.pdf#cite.Pascanu2014

2. Attention is all you need : https://arxiv.org/pdf/1502.03044v2.pdf#cite.Pascanu2014
Notes : 
- Overall architecture follows encoder-decoder style, encoder has 6 layers, each with 2 sublayers (attention layer and a feed-forward layer), decoder also has 6 layers, each with 3 sublayers (two attention layers and a feed-forward layer, the first of which is masked to ensure the ith sequence is predicted based on known outputs before the ith position.
- attention layer consists of : query, key-value pair, which are mapped to an output. Weight for each value is calculated through a compatibility function between the query and key, scaled by 1/sqrt(dk) where dk is the dimension of query or key, author suspects that without scaling, large dk leads to a softmax output nearing the diminishing gradient.
-

## useful learning links
understanding LSTM : https://colah.github.io/posts/2015-08-Understanding-LSTMs/
