# Developer guideline to collaborate
The goal of this guiline is to make a smooth collaboration process, teaching steps to collaborate succesfully following industry practices.

## Table of contents:
- [(Recommended) Work using github codespaces.](#recommended-workflow)
  - [Pre-requisites](#recommended-workflow-pre-requisites) 
  - [Open the project in code editor](#recommended-workflow-open-project)
  - [Run the project](#recommended-workflow-run-project)
- [Create a pull request to merge your changes in the main branch](#create-pr)
- [Work with your local computer](#local-workflow)
  - [Pre-requisites](#local-workflow-pre-requisites)
  - [Set-up the project in your local computer](#local-workflow-project-setup)

## (Recommended) Work using github codespaces.  <a name="recommended-workflow"></a>

### Pre-requisites <a name="recommended-workflow-pre-requisites"></a>
- (Recommended) Install [Visual Studio Code](https://code.visualstudio.com/Download).

### Open the project in code editor  <a name="recommended-workflow-open-project"></a>
  
  1. Select your branch <br/>
    <img width="888" alt="image" src="https://github.com/jela3105/compiler/assets/46289656/fa4bf882-28ac-4fcb-bc25-3191cd78dd30"><br/><br/>

 
  2. Open your codespace in your preferred editor (Recommended Visual Studio Code)<br/>
  <img width="878" alt="image" src="https://github.com/jela3105/compiler/assets/46289656/ac9d24a1-0073-4a42-9be9-badf2e321fc1">
<img width="650" alt="image" src="https://github.com/jela3105/compiler/assets/46289656/59680152-b9c6-4420-a938-f370a9351cc3"> <br/><br/>
  
  3. Click "Open" <br/>
  <img width="959" alt="image" src="https://github.com/jela3105/compiler/assets/46289656/8e18982e-c596-4a8f-b77d-092cb6b791e6"><br/><br/>
 
  4. Congratulations!, you can now edit the code. <br/>
  <img width="960" alt="image" src="https://github.com/jela3105/compiler/assets/46289656/a8d6d817-3907-466f-a723-0bd7722aa69f"> <br/>
  
### Run the project <a name="recommended-workflow-run-project"></a>

1. Open the terminal <br/>
   <img width="960" alt="image" src="https://github.com/jela3105/compiler/assets/46289656/4865864c-f07b-4a2d-b1ee-33894f515f25">

2. To "compile" (create the docker image) run the following command: <br/>
   ```docker build -t compiler .```<br/> 
  You will see the following output: <br/>
   <img width="664" alt="image" src="https://github.com/jela3105/compiler/assets/46289656/0e7ba4e8-61a1-469c-99f1-cdd01c4cda83"> <br/>

3. To "Run the project" run the following command: <br/>
   ```docker run compiler```</br>
   The program will run succesfully: <br/>
   <img width="664" alt="image" src="https://github.com/jela3105/compiler/assets/46289656/d9b3ec03-86a5-4a45-a0b5-6ba5abf0d497"> <br/>

## Create a pull request to merge your changes in the main branch <a name="create-pr"></a>

## Work with your computer locally<a name="local-workflow"></a>
### Pre-requisites<a name="local-workflow-pre-requisites"></a>
- (Recomended) Install [Visual Studio Code](https://code.visualstudio.com/Download).
- Install [Docker Destkop](https://www.docker.com/get-started/).
  - When open the installer maker sure to select the option "Install required Windows components for WSL 2".
  - This [Tutorial to set-up docker in windows](https://www.youtube.com/watch?v=2ezNqqaSjq8) can help.
- (for Windows) [Install WSL](https://learn.microsoft.com/en-us/windows/wsl/install).

### Set-up the project in your local computer<a name="local-workflow-project-setup"></a>
