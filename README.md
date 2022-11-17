# Readme

* [docs](docs/index.md)
* [iot.skillplot.org](https://iot.skillplot.org/)


## Instructions to upload to repo

### Project work


* **Project** is to be uploaded under respective year session directory. For session `sem-1-2022-23` create a directory with `<name>-<studentID>` in this format: `projects/sem-1-2022-23/<name>-<studentID>`.
    * Example: `projects/sem-1-2022-23/mohan-2019phxp0119p`
* All the code, configuration, required setup and usage instructions to be made available in the directory itself.
* Documentation is to be created in the markdown (.md) format
* Any project reports, research reports can be in  markdown (.md) format, but preferrably in LaTeX format


```bash
├── projects
│   └── sem-1-2022-23 ## proejcts for Semester-1, 2022-23 session
│       ├── shivam-2021phxp0469p
│       └── <name>-<studentID> ## add project directory in this naming convetion
```

### TAship Work items


* **TAship** work items are to be uploaded under `apps` directory with topic-wise directory as illustrated.
    ```bash
    ├── apps
    │   ├── basics
    │   ├── <coap-1> ## add 
    │   └── <mqtt-1>
    ```
* All the code, configuration, required setup and usage instructions to be made available in the directory itself.
* Documentation is to be created in the markdown (.md) format




### Labseets items



* **Lab code** is to be uploaded under respective year session directory. For session `sem-1-2022-23` create a directory with `<name>-<studentID>` in this format: `labs/sem-1-2022-23/<name>-<studentID>`.
    * Example: `lab/sem-1-2022-23/mohan-2019phxp0119p`
* All the code, configuration, required setup and usage instructions to be made available in the directory itself.
* Documentation is to be created in the markdown (.md) format


## Directory Structure

```bash
├── apps
│   ├── basics
│   ├── <coap-1> ## add 
│   └── <mqtt-1>
├── assets
│   └── images
├── csg518iot
├── demo
├── docs
│   └── _posts
├── labs
│   └── sem-1-2022-23 ## labs for Semester-1, 2022-23 session
├── projects
│   └── sem-1-2022-23 ## proejcts for Semester-1, 2022-23 session
│       ├── shivam-2021phxp0469p
│       └── <name>-<studentID> ## add project directory in this naming convetion
├── requirements
├── scripts
├── src
└── tests
```



## Getting Started

1. Clone the repo and configure it
    ```bash
    git clone https://github.com/skillplot/cs-g518-iot.git
    git config user.name <user_name>
    git config user.email <user_email>
    git config -l
    ```
2. To add new/updates changes
    ```bash
    git status
    ## put add all the changes
    git add -A
    ## example to add particular file
    git add README.md
    git status
    git commit -m'put some details on the changes'
    git push
    git status
    ```

```bash
wget -O - https://raw.githubusercontent.com/skillplot/cs-g518-iot/main/scripts/codehub.setup.sh | bash
wget -O - https://raw.githubusercontent.com/skillplot/cs-g518-iot/main/scripts/install.sh | bash
wget -O - https://raw.githubusercontent.com/skillplot/cs-g518-iot/main/scripts/cs-g518-iot.clone.sh | bash
```