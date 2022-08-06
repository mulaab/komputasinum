

# Using R in Jupyter Nobebook

This is all of step by step to use R in jupyter notebook. I implement it for developing my jupyterbook in mulaab.github.io/ datasain. I need it for datasain exploring. 



1. If Anaconda is installed and the Jupyter-Notebook with it (should be the standard install), open up the Anaconda prompt, not the Windows command prompt or the Anaconda Navigator
2. Look up the executable of R (not Rgui or Rstudio), it should be somewhere like C:\Program Files\R\R-3.5.1\bin and remember the path typing `cd C:\Program Files\R\R-3.5.1\bin` and start R by typing `R`
3. typing `IRkernel::installspec()`
4. Now you can start an R kernel within Jupyter-Notebook

 for more information please check https://stackoverflow.com/questions/44056164/jupyter-client-has-to-be-installed-but-jupyter-kernelspec-version-exited-wit



Or you can do this procedure for  implement it

## Steps to Add R to Jupyter Notebook

### Step 1: Open the Anaconda Prompt

To start, open the *Anaconda Prompt*.

You’ll then see the following screen with your user name:

(base) C:\Users\Ron>

### Step 2: Add R to Jupyter

Next, type/copy the following command in order to add R to Jupyter:

```
conda install -c r r-irkernel
```

The command would look like this in the Anaconda Prompt (press ENTER to proceed with the installation):

(base) C:\Users\Ron>conda install -c r r-irkernel

Next, type ‘**y**‘ and then press ENTER to proceed:

Proceed ([y]/n)? y

After a short period of time, your installation would be completed.

### Step 3: Launch Jupyter Notebook

To launch Jupyter Notebook, first open the **Anaconda Navigator**.

Then, click on the button to launch **Jupyter**.

### Step 4: Create a new Notebook

To create a new Notebook for R:

1. First, click on ‘**New**‘ on the top right-hand-side of your screen
2. Finally, select ‘**R**‘ from the drop-down list

### Step 5: Run your Code

You can now run your desired R code.

For example, you can create a simple [DataFrame in R](https://datatofish.com/create-dataframe-in-r/) using this syntax:

```
df <- data.frame(product = c('Oven', 'Microwave', 'Toaster'),
                 price = c(850, 300, 120)
                 )
print (df)
```

Click on ‘Run’ and you’ll get the following DataFrame:

```
    product  price
1      Oven    850
2 Microwave    300
3   Toaster    120
```

Categories[R](https://datatofish.com/category/r/)



https://notebook.community/pioneers/topgear/ipython-in-depth/examples/Builtin%20Extensions/R%20Magics

