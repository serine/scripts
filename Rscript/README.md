# Running R notes

- `vector()` to create a vector
- `attributes()` gives all attributes. Looks like you can use `attributes` to flatten the matrix (or any other data.frames),
refere to help `?attributes` for more information
- `names()` wil give you coluumn names

- `cat("\014")` will clear the screen. need to find a way to map it to character c
- `as.numeric()` or `as.character()` `as.logical()` to convert to another object type

- `cbind` is column bind also can bind by rows

Factors are used to represent cattegorrical data

- `str(apply)` stands for 'structure'  and it looks like this is simmilar to pythons `dir()` function

- `apply(X, MARGIN, FUN)` where:
                          * x is the object to operate on e.g data.frame or a matrix
                          * MARGIN can be either row == 1 or column == 2 or both == c(1,2)
                          * FUN any R functions 
                           e.g apply(x, 1, max)
                           
_Design matrix is used tto describes how the data was collected_ ? 
