# Humming-Bird

This is a repository dedicated to code written for drone project. There are many potential avenues to pursue for this drone project including computer vision (for object + facial recognition), NLP (commands), and a mechanism to triggering a nerf gun. 

In order for this to operate, you will need an OpenAI API key which you create a .env file to store. 

Two initial pipelines that have been created as demonstrated in the below images, with implementations demonstrated in the jupyter notebooks. 

[Direct action pipeline](/images/Simplest.png)

This directly translates speech into Whisper commands in order to obtain general commands which are translated into direct drone-code through a intermedaite agent that writes ot a step by step plan. 

[Judge-revise-act pipeline](/images/agentic_1.png)

This modality applies another judge agent that judges the result of the command, code, and plan, and attempts to provide constructive feedback on the resulting source-code that will intaken and reused to create new code. This occurs iteratively until there are no more critiques. There is a sacrifice between tokens generated and accuracy of command systems. 

Here is a link in order to read a more thorough technical report on everything! [Click Here!](https://drive.google.com/file/d/1ySvLhD_-F-yIzr4IbxILDwCjSymwu-lH/view?usp=sharing)! 


