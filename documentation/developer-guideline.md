# Developer guideline to collaborate
The goal of this guiline is to make a smooth collaboration process, teaching steps to collaborate succesfully following industry practices.

## Table of contents:
- [(Recommended) Work using github codespaces.](#recommended-workflow)
  - [Pre-requisites](#recommended-workflow-pre-requisites) 
  - [Open the project in code editor](#recommended-workflow-open-project)
  - [Run the project](#recommended-workflow-run-project)
- [Update your code to the project](#update-code)
  - [Upload your changes to github](#upload-changes)
  - [Create a pull request to merge your changes in GitHub](#create-pr)
  - [Fix comments in your pull request](#fix-comments)
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

## Update your code to the project <a name="update-code"></a>
*Important: Before start woking with the code, run the command ```git pull origin main``` to make sure you have the latest changes in your working directory.

### Upload your changes to github <a name="upload-changes"></a>
One you have done working with one functionality, make sure to save your changes and create a commit:
1. Go to "Source control" icon <br/>
<img width="223" alt="image" src="https://github.com/jela3105/compiler/assets/46289656/9bbef1c6-e796-4a18-ab7a-28c6ab44e900"><br/>
2. Click on "stage all changes" to add all the changes that you made in your commit.<br/>
<img width="272" alt="image" src="https://github.com/jela3105/compiler/assets/46289656/1e4542c1-872e-4386-a77f-697e08bf3bac"><br/>
3. Enter a brief description of *WHAT* you did.<br/>
<img width="226" alt="image" src="https://github.com/jela3105/compiler/assets/46289656/dfefac43-6092-41f2-b13c-47df9ccc0087"><br/>
4. Click "Commit".<br/>
<img width="256" alt="image" src="https://github.com/jela3105/compiler/assets/46289656/b4065b04-80a6-46da-8e4f-2ca099d140cf"><br/>
5. Click "Sync Changes".<br/>
<img width="235" alt="image" src="https://github.com/jela3105/compiler/assets/46289656/361417d5-006d-495a-9ede-c31f02ff4709"><br/>

### Create a pull request to merge your changes in GitHub. <a name="create-pr"></a>
1. Select your branch <br/>
<img width="622" alt="image" src="https://github.com/jela3105/compiler/assets/46289656/830bed7e-cdc8-4e0e-9498-0c4129bf67c1"><br/>
2. In case you have upload your changes, you will be able to create a new pull request <br/>
<img width="630" alt="image" src="https://github.com/jela3105/compiler/assets/46289656/a27ef3e7-29a6-41ba-ab6e-a5987cafd50a"><br/>
3. You must see this message. In case you dont see it, fix the problem that it shows. <br/>
<img width="887" alt="image" src="https://github.com/jela3105/compiler/assets/46289656/35a819a9-b9d7-4cc0-adc6-870554b75cde"><br/>
4. Click "assign yourself" <br/>
<img width="887" alt="image" src="https://github.com/jela3105/compiler/assets/46289656/ec7e3ec4-7fdf-47da-867e-6d852882a1ee"><br/>
5. Add Jela3105 as reviewer <br/>
<img width="887" alt="image" src="https://github.com/jela3105/compiler/assets/46289656/e305100b-49dd-4280-ba13-a340cc2f67e1"><br/>
6. If you scroll-down the page, you will see your changes and commits<br/>
<img width="916" alt="image" src="https://github.com/jela3105/compiler/assets/46289656/f1012d3b-ef94-4d37-8b05-270cf82b0a1a"> <br/>
7. Click "Create pull request" <br/>
<img width="789" alt="image" src="https://github.com/jela3105/compiler/assets/46289656/c940a8a1-79cb-4542-bad5-e1bf3cd77146"> <br/>
8. Congratulations!, you have created a pull request, now wait until it's approved or get comments.

### Fix comments in your pull request.<a name="fix-comments"></a>
Check if you have pending comments in your pull request.
1. Click the "Pull requests" tab. <br/>
<img width="904" alt="image" src="https://github.com/jela3105/compiler/assets/46289656/eff70d79-dd23-4eb0-8be4-c157ce9abe5f"> <br/>


## Work with your computer locally<a name="local-workflow"></a>
### Pre-requisites<a name="local-workflow-pre-requisites"></a>
- (Recomended) Install [Visual Studio Code](https://code.visualstudio.com/Download).
- Install [Docker Destkop](https://www.docker.com/get-started/).
  - When open the installer maker sure to select the option "Install required Windows components for WSL 2".
  - This [Tutorial to set-up docker in windows](https://www.youtube.com/watch?v=2ezNqqaSjq8) can help.
- (for Windows) [Install WSL](https://learn.microsoft.com/en-us/windows/wsl/install).

### Set-up the project in your local computer<a name="local-workflow-project-setup"></a>
