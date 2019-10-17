# NLP-Project

## papers
1. Show, Attend and Tell : https://arxiv.org/pdf/1502.03044v2.pdf#cite.Pascanu2014

2. Attention is all you need : https://arxiv.org/pdf/1502.03044v2.pdf#cite.Pascanu2014
Notes : 
- Overall architecture follows encoder-decoder style, encoder has 6 layers, each with 2 sublayers (attention layer and a feed-forward layer), decoder also has 6 layers, each with 3 sublayers (two attention layers and a feed-forward layer, the first of which is masked to ensure the ith sequence is predicted based on known outputs before the ith position.
- attention layer consists of : query, key-value pair, which are mapped to an output. Weight for each value is calculated through a compatibility function between the query and key, scaled by 1/sqrt(dk) where dk is the dimension of query or key, author suspects that without scaling, large dk leads to a softmax output nearing the diminishing gradient.
-

3. A multi-task U-Net for segmentation with lazy labels
- Separate into three tasks : detection, separation and segmentation
- Detection : using the weak annotations, produce classification of rough regions through the under-segmentation mask.
- Separation : using rough scribbles of fine separations, separate instances connected without a clear boundary.
- Segmentation : using a few strong annotations, produce pixel-wise classification.
- All three tasks share the same contracting path, but this paper introduces a new multi-task block for the expansive path.
- Use a weighted loss function over the samples to account for missing annotations as the weak/strong annotations are shared between the three tasks
- For each multi-task block : Detection and Segmentation have a common path similar to decoder part of standard U-net, they share same weights, use the same concatenation with feature maps from contracting path via the skip connections. however, inserted an additional residual sub-block for Segmentation to allow for extra network parameters to learn about object boundary localization. For Segmentation, path built on the top of Detection/Segmentation, with long skip connections starting from the sub-blocks of the Detection/Segmentation path, these extract higher resolution features from Segmentation task and use them in the Separation. 

## useful learning links
understanding LSTM : https://colah.github.io/posts/2015-08-Understanding-LSTMs/
