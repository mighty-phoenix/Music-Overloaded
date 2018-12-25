### **MUSIC-OVERLOADED**
Music Overloaded is a local server based simple django app that uses MySQL database.
It is a music storage and management app. Currently, it has support only for MacOS
and Linux Distros. Make sure you have MySQL installed properly on your system.

Music-Overloaded is written using Python, HTML, and CSS.

### **INSTALLATION**

1. Create a new MySQL database using the following code.(Replace db_name with the name you want to give to you database)

  ```
    mysql -u root -p
  ```
  You will be asked for your password. Then, you will enter the MySQL prompt now. Write following code:
  
  ```
    CREATE DATABASE db_name;
  ```
  Press Ctrl+Z to exit MySQL.
 
2. Create a new, empty folder. Let us assume the name of the folder is `'folder name'`. 

3. Navigate to it. (`cd 'folder name'`)

4. Fork and clone the Music-Overloaded repo. This will create a new folder named `'folder name'/Music-Overloaded`.

5. Navigate to `'folder name'/Music-Overloaded` and run:

  ```
    git checkout master
    bash scripts/start.sh
  ```

To know more about this project, [Click here](https://drive.google.com/file/d/1VWP1aIjNr19wmqbGKN_jUJ1iuUwsZwYE/view?usp=sharing)
