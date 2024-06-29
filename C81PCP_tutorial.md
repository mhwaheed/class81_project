Authentication System with Blockchain
=====================================

In this activity, you will get the user details and store them in the block.


<img src= "https://media.slid.es/uploads/1525749/images/10625691/C81PCP.gif" width = "521" height = "281">


Follow the given steps to complete this activity:
1. Create a signup() function


* Open file `app.py`.


* Create a route `'/signup'` with methods `GET` and `POST` .

```sh
    @app.route('/signup', methods=['GET', 'POST'])
```
    


* Define `signup()` function to sign up to the page.

```sh
    def signup():
```
    
* Access global `blockData`.

```sh
    global blockData
```
    
* Check if the request method is `POST`.

```sh
    if request.method == 'POST':
```


* Get `username, email, password` from the signup form in the respective variables.

```sh
    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")
```
    

* Create a new block with `username, `email` and `password``.

```sh
    blockData = {
    'username': username,
    'email': email,
    'password': password
    }
```
    
       
*  Redirect the user to the `signin` page.

```sh
    return redirect('/signin')
```
   
* If the request is not `POST` request then redirect to the signup page.

```sh
    return render_template('signup.html')
```
    
* Check if blockData's username and password is the same as variable `username` and `password`.

```sh
    if blockData['username'] == username and blockData['password'] == password:
```
    

* Return the `profile.html` and variable block containing `blockData`.

```sh
    return render_template('profile.html', block= blockData)
```
    

2. Display the Username and Password.


* Display `username`, `email` and `password` from block.

```sh
    <h5>{{block['username']}}</h5>


    <p class="text-muted">{{block['email']}}</p>


    <p class="text-muted">{{block['password']}}</p>
```
    

* Save and run the code to check the output.




