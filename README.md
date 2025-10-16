<h1 align="center">

[![Shuffle Logo](https://github.com/Shuffle/Shuffle/blob/main/frontend/public/images/Shuffle_logo_new.png)](https://shuffler.io)

Shuffle Automation

</h1><h4 align="center">

[Shuffle](https://shuffler.io) is an open source automation platform, built for and by the security professionals. Security operations is complex, but it doesn't have to be. Built to work well with MSSP's and other service providers in mind.


</h4>

## Risebroadband workflow (SOC)


![Risebroadband SOC Workflow](images/SOC.png)  

You can use the pre-built workflow for Rise. Simply download the JSON file containing the workflow from the Google Drive folder: `"Marvel Documents -> Backups -> Shuffle-workflow"`.  
Once you have the file, go to your Shuffle instance, navigate to "Org Workflows" -> "Import Workflow", and paste the JSON content.


## How to use test alerts  

We have created some test alerts that you can use to test the SOC workflow. These alerts simulate real incidents without needing to trigger actual alerts from Wazuh.  
To view the examples, go to `../Shuffle-fork/functions/kubernetes/alerts-format/example_input_alerts.txt`, where you will find different sample alerts typically received from Rise Broadband.  


## Cronjob   

We have a cronjob that runs every three days to delete the workflow memory, as it can grow too large and cause issues with Shuffle's persistent volumes (PVs). Make sure this cronjob is always running! You can find the code in `Shuffle-fork/functions/kubernetes/all-in-one.yaml` under the name `delete-workflowexecution-index`.

![Example Shuffle webhook integration](https://github.com/shuffle/Shuffle/blob/main/frontend/src/assets/img/github_shuffle_img.png)

## Try it
* Self-hosted: Check out the [installation guide](https://github.com/shuffle/shuffle/blob/master/.github/install-guide.md)
* Cloud: Register at https://shuffler.io/register and get cooking

Please consider [sponsoring](https://github.com/sponsors/frikky) the project if you want to see more rapid development.

## Support
* [Discord](https://discord.gg/B2CBzUm)
* [Twitter](https://twitter.com/shuffleio)
* [Email](mailto:frikky@shuffler.io)
* [Open issue](https://github.com/shuffle/Shuffle/issues/new)
* [Shuffler.io](https://shuffler.io/contact)

## Documentation
[Documentation](https://shuffler.io/docs) can be found on [https://shuffler.io/docs](https://shuffler.io/docs) and is written here: [https://github.com/shuffle/shuffle-docs](https://github.com/shuffle/shuffle-docs).

### Setting up a local development environment

Please follow the steps mentioned [here](https://github.com/Shuffle/Shuffle/blob/main/.github/install-guide.md#local-development-installation)!

## Related repositories
* OpenAPI apps: [https://github.com/shuffle/security-openapis](https://github.com/shuffle/security-openapis)
* Documentation: [https://github.com/shuffle/shuffle-docs](https://github.com/shuffle/shuffle-docs)
* Workflows: [https://github.com/shuffle/shuffle-workflows](https://github.com/shuffle/shuffle-workflows)
* Python apps: [https://github.com/shuffle/shuffle-apps](https://github.com/shuffle/python-apps)

## Features
* Simple, feature rich [workflow editor](https://shuffler.io/docs/workflows)
* App creator using [OpenAPI](https://github.com/shuffle/OpenAPI-security-definitions)
* Premade apps for your security tools
* Organization and sub-organization control
* Hybrid resource sharing with shuffler.io (optional)




## License
All modular information related to Shuffle will be under MIT (anyone can use it for whatever purpose), with Shuffle itself using AGPLv3. 

Workflows: MIT
Documentation: MIT
Shuffle backend: AGPLv3 
Apps, specification and App SDK: MIT

## Architecture
![Shuffle Architecture](https://github.com/shuffle/Shuffle/blob/main/frontend/src/assets/img/shuffle_architecture.png)


### Repository overview 
Below is the folder structure with a short explanation
```bash
├── README.md				# What you're reading right now
├── backend					# Contains backend related code.
│   ├── go-app 			# The backend golang webserver
│   └── app_sdk			# The SDK used for apps
├── frontend				# Contains frontend code. ReactJS, Material UI and cytoscape
├── functions				# Has execution and extension resources, such as the Wazuh integration
│   ├── onprem				# Code for onprem solutions
│   │   ├── Orborus 	# Distributes execution locations
│   │   ├── Worker		# Runs a workflow
└ docker-compose.yml 	# Used for deployments
```
