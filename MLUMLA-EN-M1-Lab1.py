#!/usr/bin/env python
# coding: utf-8

# <center><img src="images/logo.png" alt="drawing" width="400" style="background-color:white; padding:1em;" /></center> <br/>
# 
# # ML through Application 
# ## Module 1, Lab 1: Getting Started with Jupyter Notebooks
# 
# Jupyter notebooks are a critical tool for developing ML projects. By the end of this notebook, you should be able to effectively navigate a Jupyter notebook.
# 
# You will learn the following:
# 
# - What a kernel is
# - The difference between the menu bar and the toolbar
# - The difference between code and Markdown cells
# - How to write math in Markdown cells
# - How to write Python in code cells
# - The run flow of notebooks
# 
# __Note:__ These lab instructions are written for using Jupyter, not JupyterLab. You might encounter differences in the UI if you run this lab in JupyterLab.
# 
# ----
# 
# You will be presented with two kinds of exercises throughout the notebook: activities and challenges. <br/>
# 
# | <img style="float: center;" src="images/activity.png" alt="Activity" width="125"/>| <img style="float: center;" src="images/challenge.png" alt="Challenge" width="125"/>|
# | --- | --- |
# |<p style="text-align:center;"> No coding is needed for an activity. You try to understand a concept, <br/>answer questions, or run a code cell.</p> |<p style="text-align:center;">Challenges are where you can practice your coding skills.</p>

# ## Index
# 
# - [Jupyter Notebook application interface](#Jupyter-Notebook-application-interface)
# - [Kernel](#Kernel)
# - [Cells](#Cells)
# - [Jupyter notebook run flow](#Jupyter-notebook-run-flow)

# ---
# ## Jupyter Notebook application interface

# A Jupyter notebook has a few key elements:
# 
# ![image.png](attachment:image.png "Jupyter key elements")

# ### Notebook name
# 
# This is the name of the notebook. A new notebook is named __Untitled__ by default, but you can change it at anytime.

# ### Menu bar
# 
# ![Screen%20Shot%202022-08-30%20at%201.54.29%20PM.png](attachment:Screen%20Shot%202022-08-30%20at%201.54.29%20PM.png)
# 
# The menu bar contains multiple menus:
# 
# - **File:** Options at the file (notebook) level
# - **Edit:** Cell options
# - **View:** Toggle options for the notebook view
# - **Insert:** Insert a cell above or below the selected cell
# - **Cell:** Cell-level run commands
# - **Kernel:** Kernel runtime commands
# - **Widgets:** Widget options (outside the scope of this document)
# - **Help:** Help resources and references

# ### Toolbar
# 
# ![Screen%20Shot%202022-08-30%20at%201.54.38%20PM.png](attachment:Screen%20Shot%202022-08-30%20at%201.54.38%20PM.png "Toolbar1")
# 
# The toolbar has a series of cell-level commands. Use the toolbar to perform actions such as running, stopping, or deleting a cell, or changing the type of a cell. You will learn more about cells in the following sections.

# <div style="border: 4px solid coral; text-align:center; margin:auto;">
#     <h3><i>Try it yourself!</i></h3>
#     <br>
#     <p style="text-align:center;margin:auto;"><img src="images/activity.png" alt="Activity" width="100" /> </p>
#     <p style="text-align:center;margin: auto;">Select the following cell. To run the cell and move to the next cell, choose <b>Run</b> on the toolbar OR press Shift+Enter.</p>
#     <br>
# </div>

# In[1]:


print("My first code cell!")


# Now you will import some libraries that you need for this notebook. You will learn more about importing libraries later.

# 
# <div style="border: 4px solid coral; text-align: center; margin: auto;">
#     <h3><i>Try it yourself!</i></h3>
#     <br>
#     <p style="text-align:center;margin:auto;"><img src="images/activity.png" alt="Activity" width="100" /> </p>
#     <p style=" text-align: center; margin: auto;">Select the following cell. To run the cell and move to the next cell, choose <b>Run</b> on the toolbar OR press Shift+Enter.</p>
#     <br>
# </div>

# In[2]:


import time

from MLUMLA_EN_M1_Lab1_quiz_questions import *


# ### Cell status
# 
# After you run a cell, how do you know that it finished running?
# 
# On the left side of each cell is a number inside brackets, like this: <font color=darkblue>`In [3]`</font>.
# 
# Each time that you run a cell, this value changes. This is because your notebook keeps track of the order that you run cells in. The number inside the brackets is where that cell was run in the order of cells in your notebook.
# 
# You will learn more about this in the <a href="#Jupyter-notebook-run-flow">Run Flow</a> section of this notebook.

# <div style="border: 4px solid coral; text-align: center; margin: auto;">
#     <h3><i>Try it yourself!</i></h3>
#     <br>
#     <p style="text-align:center;margin:auto;"><img src="images/activity.png" alt="Activity" width="100" /> </p>
#     <p style="text-align: center; margin: auto;">Select and run the following cell. Repeat this a few times to see the number in brackets increase with each run.</p><br>
#     <p style="text-align: center; margin: auto;"><b>Tip:</b> To run the selected cell without moving to the next cell, press Ctrl+Enter (Windows) or Cmd+Enter (Mac).</p>
#     <br>
# </div>

# In[6]:


print(
    "Run this cell multiple times. Do you notice how the number in brackets changes?"
)


# ### Cells that take longer to run
# 
# When a cell runs code that takes a noticeable amount of time to run, instead of the next sequential number appearing immediately in the brackets, an asterisk appears, like this: <font color=darkblue>`In [*]`</font>. When the cell is finished running, the asterisk updates to a number. The asterisk provides a helpful way to see if a cell is still running.
# 
# You can select multiple cells and run them. Jupyter will automatically run each cell in the set order, rather than running the cells at the same time. Look for the asterisk to see which cell is currently running.
# 
# **Tip:** Another way to see if any cell is running in the notebook is to look at the small circle at the top-right corner, next to the kernel name. If the circle is filled, one or more cells are currently running.

# <div style="border: 4px solid coral; text-align: center; margin: auto;">
#     <h3><i>Try it yourself!</i></h3>
#     <br>
#     <p style="text-align:center;margin:auto;"><img src="images/activity.png" alt="Activity" width="100" /> </p>
#     <p style=" text-align: center; margin: auto;">Select and run the following cell. Notice that the asterisk appears in the brackets for a few seconds.</p>
#     <br>
# </div>

# In[7]:


time.sleep(5)
print("If you didn't see the asterisk, run this cell again.")


# <div style="border: 4px solid coral; text-align: center; margin: auto;">
#     <h3><i>It's time to check your knowledge!</i></h3>
#     <br>
#     <p style=" text-align: center; margin: auto;">To load the question, run the following cell.</p>
#     <br>
# </div> 

# In[8]:


# Run this cell for a knowledge check question
question_1


# ---
# 
# ## Kernel
# 
# In the context of Jupyter notebooks, the kernel is the computational engine that runs the code that is contained in a notebook. The kernel type is displayed in the top-right corner. The kernel is the programming language plus the environment (and dependencies) that the notebook uses to run code.
# 
# Use the **Kernel** menu in the menu bar to make notebook-wide changes to your code, such as restarting every cell or interrupting the kernel (stopping a cell if it takes too long to run).

# You can run the whole notebook in a single step by choosing **Cell** > **Run All** (in JupyterLab, choose **Run** > **Run All Cells**).
# 
# To restart the kernel, choose **Kernel** > **Restart** OR press 0,0. This can be useful to restart a computation (for example, if variables are deleted or open files are closed).
# 
# __Important:__ Restarting the kernel will reset the notebook and remove all variables or methods that you've defined.
# 
# To change the kernel version for a notebook, choose **Kernel** > **Change kernel** and select the kernel to use.
# 
# To interrupt a calculation that is taking too long, choose **Kernel** > **Interrupt** OR press i,i.

# <div style="border: 4px solid coral; text-align: center; margin: auto;">
#     <h3><i>It's time to check your knowledge!</i></h3>
#     <br>
#     <p style=" text-align: center; margin: auto;">To load the question, run the following cell.</p>
#     <br>
# </div> 

# In[9]:


# Run this cell for a knowledge check question
question_2


# ---
# ## Cells
# 
# Cells form the body of a notebook, and they are the atomic units of code in a notebook. A notebook has two main cell types:
# - **Markdown cells:** A Markdown cell contains text that is formatted using Markdown. This type of cell is typically used to display text, images, and equations. You can use Markdown cells to document your work so that you and others can understand the notebook.
# - **Code cells:** A code cell contains code to be run in the kernel. When the code is run, the notebook displays the output after the code cell that generated it.

# ### Markdown cells
# 
# #### Standard Markdown
# 
# To create a new Markdown cell, create a cell. Then, select the cell and choose **Cell** > **Cell Type** > **Markdown** OR choose the Markdown option in the toolbar, as shown in the following image:
# ![toolbar.png](attachment:toolbar.png "Toolbar")
# 
# Markdown cells are used to write text by using Markdown. Markdown is a markup language to format plain text. You can use certain symbols to format or render text in specific ways. For example, the following text:
# 
# `# Level 1 Heading`
# 
# will render as a heading, like this:
# 
# # Level 1 Heading
# 
# And the following text:
# 
# `Add emphasis with **bold** and __bold__, or *italic* and _italic_.`
# 
# will render with bold and italic formatting, like this:
# 
# Add emphasis with **bold** and __bold__, or *italic* and _italic_.
# 
# You can also create lists using:
# 
# - Item 1
# - Item 2
# - Item 3
# 
# or
# 
# 1. Item a
# 1. Item b
# 1. Item c
# 
# A full tutorial for Markdown is outside the scope of this lab, but for more information, see the [Markdown Guide site](https://www.markdownguide.org).

# <div style="border: 4px solid coral; text-align: center; margin: auto;"> 
#     <h4><i>Try it yourself!</i></h4>
#     <p style="text-align:center; margin:auto;"><img src="images/challenge.png" alt="Challenge" width="100" /> </p>
#     <p style="text-align:center; margin:auto;">It's time to practice! In the next cell, use Markdown to replicate the rendered Markdown that is shown in the following screenshot.</p>
#     <br>
# </div>
# 
# <div>
# <img src="attachment:markdown1.png" alt="Rendered Markdown" width="700"/>
# </div>

# ########## EDIT THIS AREA WITH YOUR MARKDOWN SOLUTION ##########
# 
# # I accept the challenge!
# 
# 
# ## We can have headings at several levels
# 
# 
# ### We can have headings at several levels
# 
# 
# #### We can have headings at severals levels
# 
# 
# ##### We can have headings at several levels
# 
# As well as adding emphasis via **bold text** and also _italic text_.
# 
# Using Markdown is useful by:
# 
# - Helping people better understand the code implemented
# - Adding references and additional content to help understand the conceptual context related to the code
# 
# And to master markdown, as any other knownledge, we need to follow these steps:
# 
# 1. Learn the concept
# 1. Practice
# 1. And practice
# 1. And more practice
# 
# 
# ########## END OF MARKDOWN SOLUTION AREA ##########

# #### Writing equations in Markdown
# 
# You can add equations to Markdown by writing LaTeX inside of `$` symbols. For example:
# 
# `$ y = \beta_{0} + 2\beta_1^2 $`
# 
# will render as the following:
# 
# $ y = \beta_{0} + 2\beta_1^2 $
# 
# Jupyter uses MathJax to render equations. For information about the available equations and symbols, see [MathJax TeX and LaTeX Support](https://docs.mathjax.org/en/v2.7-latest/tex.html).

# <div style="border: 4px solid coral; text-align: center; margin: auto;"> 
#     <h4><i>Try it yourself!</i></h4>
#     <p style="text-align:center; margin:auto;"><img src="images/challenge.png" alt="Challenge" width="100" /> </p>
#     <p style="text-align:center; margin:auto;">It's time to practice! In the next cell, try to replicate the explanation of the Drake equation from the following image. (You don't need to replicate the border around the text.)</p>
#     <br>
# </div>
# 
# <div>
# <img src="attachment:DrakeEquation.png" width="900"/>
# </div>

# ########## EDIT THIS AREA WITH YOUR MARKDOWN SOLUTION ##########
# #### The Drake Equation
# 
# The Drake Equation is used to estimate the number of active, communicative extraterrestrial civilizations in the Milky Way Galaxy.
# 
# The Drake equation is:
# 
# $ N = R_* \cdot f_p \cdot n_e \cdot f_1 \cdot f_i \cdot f_c \cdot L $
# 
# where
# 
# - $ N $  = the number of civilizations in the Milky Way galaxy with which communication might be possible (i.e. which are on the current past light cone); 
# 
# and
# 
# - $ R_* $ = the average rate of star formation in our Galaxy
# - $ f_p $ = the fraction of those stars that have planets
# - $ n_e $ = the average number of planets that can potentially support life per star that has planets
# - $f_1 $ = the fraction of planets that could support life that actually develop life at some point
# - $f_i $ = the fraction of planets with life that actually go on to develop intelligent life (civilizations)
# - $f_c $ = the fraction of civilization that develop a technology that releases detectable signs of their existence onto space
# - $ L $ = the length of time for which such civilzations release detectable signals into space
# 
# ########## END OF MARKDOWN SOLUTION AREA ##########

# ### Code cells
# 
# A code cell contains code to be run in the kernel. When the code is run, the notebook displays the output after the code cell that generated it.
# 
# You can write Python code in a code cell. The following cell provides an example:

# In[11]:


# This is a comment in a code cell
# Run this cell to see what it outputs
x = 5
powers_of_five = [x ** i for i in range(5)]
print(powers_of_five)


# <div style="border: 4px solid coral; text-align: center; margin: auto;"> 
#     <h4><i>Try it yourself!</i></h4>
#     <p style="text-align:center; margin:auto;"><img src="images/challenge.png" alt="Challenge" width="100" /> </p>
#     <p style="text-align:center; margin:auto;">It's time to practice! In the next cell, define the <code>myname</code> variable in Python, and give it the value of your name.</p>
#     <br>
# </div>

# In[17]:


# Create the myname variable here
############### CODE HERE ###############
myname = "James"



############## END OF CODE ##############


# To test whether you defined the variable correctly, run the following cell.

# In[19]:


try:
    print(f"Hello, {myname}!")
except NameError as e:
    print(e.args[0] + ". Make sure that you define the variable above.")


# You can use code cells for any common Python tasks. For example, you will often want to load (import) libraries into the kernel. To import a library, use the `import` command, as shown in the following cell.

# In[23]:


# Load Pandas and make a DataFrame for the powers of five
import pandas as pd

powers_of_five_df = pd.DataFrame({"power": powers_of_five})
powers_of_five_df


# Notice that the code cell referred to `powers_of_five`, which was defined in a previous cell. Cells can access values in the global environment that were defined in other cells. Just make sure to run the cells in the correct order!

# Another common task is to load external files. You can load external files as with any other Python script: through relative paths for local files, URL paths for web-hosted files, or Amazon Simple Storage Service (Amazon S3) buckets.
# 
# In the following cell, you will open a local file, which is in the same folder as this notebook, and load it into a Pandas DataFrame.
# 
# **Note:** The dataset in the file was adapted from the [Austin Animal Center Shelter Intakes and Outcomes dataset](https://www.kaggle.com/datasets/aaronschlegel/austin-animal-center-shelter-intakes-and-outcomes).

# In[24]:


# Use Pandas, which you imported earlier, to load a .csv file of a pet adoption dataset into a Pandas DataFrame
petsDataframe = pd.read_csv("data/review_dataset.csv")

# Display the first seven rows of the Pandas DataFrame
petsDataframe.head(7)


# Pandas has useful functionality for working with data. You can easily subset, reshape, calculate statistics, carry out feature engineering, or even plot data easily.
# 
# In the following cell, you will display a scatterplot for two selected columns in the Pandas DataFrame that you loaded previously.

# In[25]:


# How does the age at intake comare to the outcome age
petsDataframe.plot.scatter(
    x="Age upon Intake Days",
    y="Age upon Outcome Days",
    title="Pet Intake Age Compared to Outcome Age",
)


# <div style="border: 4px solid coral; text-align: center; margin: auto;"> 
#     <h4><i>Try it yourself!</i></h4>
#     <p style="text-align:center; margin:auto;"><img src="images/challenge.png" alt="Challenge" width="100" /> </p>
#     <p style=" text-align: center; margin: auto;">In the next cell, use <code>petsDataframe</code> to calculate the <code>mean Age upon Outcome Days</code> for each <code>Intake Condition</code>.</p>
#         <br>
#     <p style=" text-align: center; margin: auto;"><b>Tip:</b> Read the <a href="https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html">Getting Started Tutorials for Pandas</a>.</p>
#     <br>
# </div>

# In[34]:


# Use petsDataframe to calculate the mean Age upon Outcome Days for each Intake Condition
############### CODE HERE ###############
petsDataframe[["Age upon Outcome Days", "Intake Condition"]].mean(axis=1)



############## END OF CODE ##############


# ---
# ## Jupyter notebook run flow
# 
# An important note about Jupyter notebooks is that you can run the cells in any order. Typically, you want to run code cells from top to bottom because cells toward the end of the notebook will likely require variables that were defined earlier in the notebook.
# 
# Recall that Jupyter includes a number in square brackets to the left of a code cell to indicate the order in which the cells were run. Use the numbers to check that you run cells in the correct order.
# 
# When you create your own notebooks, make sure that cells are in order from top to bottom so that anyone who runs your notebook can run the cells in order from the top of the notebook to the bottom without getting any errors.
# 
# It's helpful to include Markdown cells at the beginning of a notebook to provide details about what the notebook does. In this section, you can also let people know if any code segments will take a long time to run (such as code to train a model).

# <div style="border: 4px solid coral; text-align: center; margin: auto;"> 
#     <h3><i>Try it yourself!</i></h3>
#     <p style="text-align:center;margin:auto;"><img src="images/activity.png" alt="Activity" width="100" /> </p>
#     <p style=" text-align: center; margin: auto;">Choose <b>Kernel</b> > <b>Restart</b>. Then, run the following cell.</p>
#     <br>
# </div>

# In[ ]:


# Restart the kernel, and then run this cell
petsDataframe.head(3)


# What happened?
# 
# Because you restarted the kernel, the cell had an error. This is because restarting the kernel cleared all the defined variables out of memory, including `petsDataframe`.

# Find the cell that has the commands to fix the error, run it, and rerun the `head` command to see if it works now.
# 
# ### Best practice
# 
# Although running cells out of order should work, don't rely on your memory for that. Always run all cells to make sure you don't miss anything!

# ---
# ## Conclusion
# 
# This notebook provided an introduction to what Jupyter notebooks are, how to interact with them, and how to use them for the labs in this course. You should now be able to operate effectively in any lab of this course.
# 
# ## Next lab
# 
# In the next lab, you will learn about a few additional features of Jupyter notebooks.
