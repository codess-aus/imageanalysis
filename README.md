# imageanalysis

Get started with the Image Analysis REST API or client libraries to set up a basic image tagging script. The Analyze Image service provides you with AI algorithms for processing images and returning information on their visual features. Follow these steps to install a package to your application and try out the sample code.

Use the Image Analysis client library for Python to analyze a remote image for content tags.

The Analyze API can do many different operations other than generate image tags. See the Image Analysis how-to guide for examples that showcase all of the available features.

- [Reference documentation](https://learn.microsoft.com/en-us/python/api/azure-cognitiveservices-vision-computervision/azure.cognitiveservices.vision.computervision)
- [Library source code](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/cognitiveservices/azure-cognitiveservices-vision-computervision) 
- [Package PiPy](https://pypi.org/project/azure-cognitiveservices-vision-computervision/) 
- [Samples](https://learn.microsoft.com/en-us/samples/browse/?products=azure&terms=computer-vision)


Prerequisites
An Azure subscription - Create one for free

Python 3.x

Your Python installation should include pip. You can check if you have pip installed by running pip --version on the command line. Get pip by installing the latest version of Python.
Once you have your Azure subscription, create a Vision resource in the Azure portal to get your key and endpoint. After it deploys, select Go to resource.

You need the key and endpoint from the resource you create to connect your application to the Azure AI Vision service.
You can use the free pricing tier (F0) to try the service, and upgrade later to a paid tier for production.
Create environment variables
In this example, write your credentials to environment variables on the local machine that runs the application.

Go to the Azure portal. If the resource you created in the Prerequisites section deployed successfully, select Go to resource under Next Steps. You can find your key and endpoint under Resource Management in the Keys and Endpoint page. Your resource key isn't the same as your Azure subscription ID.

 Tip

Don't include the key directly in your code, and never post it publicly. See the Azure AI services security article for more authentication options like Azure Key Vault.

Analyze image
Install the client library.

You can install the client library with:

pip install --upgrade azure-cognitiveservices-vision-computervision

Also install the Pillow library.

pip install pillow