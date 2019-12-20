# Restful application programming interface

This was used in a Mess.is community related project, which was abandoned.

## How to build, with Docker?

1. After cloning the repository to your local machine and going to that directory.
2. Rename config.py.default to config.py in app/main.  
3. Install Docker, if it's not yet.
4. Run the following to build the project in the project root directory:
```docker buiild . -t samip537/restful-api```
5. Start the built container with:
```docker run samip537/restful-api```
(Will most likely fail without a config file.)