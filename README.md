### **MUSIC-OVERLOADED**
Music Overloaded is a local server based simple django app that uses MySQL database.
It is a music storage and management app. Currently, it has support only for MacOS
and Linux Distros.

Music-Overloaded is written using Python, HTML, and CSS.

### **INSTALLATION**

1. Create a new MySQL database using the following code.(Replace db_name with the name you want to give to you database)

  ```
    sudo mysql -u root
  ```
  You will enter the MySQL prompt now. Write following code:
  
  ```
    CREATE DATABASE db_name;
  ```

2. Create a new, empty folder. Let us assume the name of the folder is 'folder name'. 

3. Navigate to it. (`cd _'folder name'_`)

4. Fork and clone the Music-Overloaded repo. This will create a new folder named `_'folder name'_/Music-Overloaded`.

5. Navigate to `_'folder name'_/Music-Overloaded` and run:

  ```
    git checkout master
    bash scripts/start.sh
  ```
